"""Crew assembly for the Educational Workflow System."""
from __future__ import annotations

import logging
from typing import Any

from crewai import Crew, Process

from agents import (
    create_study_manager_agent,
    create_notes_generator_agent,
    create_example_solver_agent,
    create_quiz_maker_agent,
)
from config.settings import OpenRouterLLMConfig
from tasks import build_educational_tasks
from tools import get_default_toolkit

logger = logging.getLogger(__name__)


def create_educational_crew(llm_overrides: dict[str, Any] | None = None) -> Crew:
    """Instantiate educational workflow crew with all 4 specialized agents."""
    tools = get_default_toolkit()
    
    # Create all 4 educational agents
    study_manager = create_study_manager_agent(tools=tools, llm_overrides=llm_overrides)
    notes_generator = create_notes_generator_agent(tools=tools, llm_overrides=llm_overrides)
    example_solver = create_example_solver_agent(tools=tools, llm_overrides=llm_overrides)
    quiz_maker = create_quiz_maker_agent(tools=tools, llm_overrides=llm_overrides)
    
    # Create tasks for all agents
    tasks = build_educational_tasks(
        study_manager,
        notes_generator,
        example_solver,
        quiz_maker,
        tools=tools
    )

    return Crew(
        agents=[study_manager, notes_generator, example_solver, quiz_maker],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )


def _build_llm_attempts(config: OpenRouterLLMConfig) -> list[dict[str, Any]]:
    """Construct an ordered list of LLM override attempts from config."""

    attempts: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()

    base_urls = [config.base_url, *config.fallback_base_urls]
    models = [config.model, *config.fallback_models]

    base_urls = list(dict.fromkeys(base_urls))
    models = list(dict.fromkeys(models))

    for provider in ("openrouter", "openai"):
        for model in models:
            for base_url in base_urls:
                key = (provider, model, base_url)
                if key in seen:
                    continue
                seen.add(key)

                override: dict[str, Any] = {}

                if base_url != config.base_url:
                    override["base_url"] = base_url

                if provider == "openrouter":
                    if model != config.model:
                        override["model"] = model
                else:
                    override["provider"] = "openai"
                    override["model"] = model
                    if config.headers:
                        override["default_headers"] = dict(config.headers)
                        override["extra_headers"] = dict(config.headers)

                attempts.append(override)

    if not attempts:
        attempts.append({})

    return attempts


def _sanitize_overrides(overrides: dict[str, Any]) -> dict[str, Any]:
    """Remove verbose or sensitive values before logging overrides."""

    sanitized = dict(overrides)
    for key in ("extra_headers", "default_headers", "api_key"):
        if key in sanitized:
            sanitized[key] = "[set]"
    return sanitized


def _execute_crew(
    topic: str, overrides: dict[str, Any], config: OpenRouterLLMConfig
) -> str:
    crew = create_educational_crew(llm_overrides=overrides)
    provider_label = overrides.get("provider", "openrouter-liteLLM")
    model_label = overrides.get("model", config.model)
    base_url_label = overrides.get("base_url", config.base_url)
    logger.info(
        "Educational crew kickoff started for topic: %s (provider=%s model=%s base_url=%s)",
        topic,
        provider_label,
        model_label,
        base_url_label,
    )
    result = crew.kickoff(inputs={"topic": topic})

    for task in crew.tasks:
        task_output = getattr(task, "output", None)
        if task_output:
            logger.info("Task '%s' output:\n%s", task.name, task_output)

    if isinstance(result, str):
        logger.info("Crew completed with final output length=%d characters", len(result))
        return result

    candidate = getattr(result, "raw_output", None) or getattr(result, "output", None)
    if candidate:
        output_text = str(candidate)
        logger.info("Crew completed with final output length=%d characters", len(output_text))
        return output_text

    output_text = str(result)
    logger.info("Crew completed with final output length=%d characters", len(output_text))
    return output_text


def run_educational_pipeline(topic: str) -> str:
    """Run the educational crew for a given study topic with OpenRouter fallback attempts."""

    config = OpenRouterLLMConfig()
    attempts = _build_llm_attempts(config)

    last_error: Exception | None = None
    total_attempts = len(attempts)

    for index, overrides in enumerate(attempts, start=1):
        try:
            if overrides:
                logger.info(
                    "Attempt %d/%d using overrides: %s",
                    index,
                    total_attempts,
                    _sanitize_overrides(overrides),
                )
            result = _execute_crew(topic, overrides, config)
            if index > 1:
                logger.info(
                    "Fallback succeeded on attempt %d/%d with overrides: %s",
                    index,
                    total_attempts,
                    _sanitize_overrides(overrides),
                )
            return result
        except Exception as exc:  # pragma: no cover - runtime resilience path
            last_error = exc
            logger.exception(
                "Crew run failed on attempt %d/%d with overrides %s",
                index,
                total_attempts,
                _sanitize_overrides(overrides),
            )

    assert last_error is not None  # defensive: should be set if all attempts failed
    raise last_error
