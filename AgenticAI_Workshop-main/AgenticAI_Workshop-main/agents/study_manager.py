"""Study Manager agent responsible for controlling the entire educational workflow."""

# Agent 1: Study Manager
from __future__ import annotations

from typing import Any, Iterable, Optional

from crewai import Agent

from config.settings import build_crewai_llm

SYSTEM_PROMPT = (
    """You are the Study Manager, the orchestrator of the entire educational workflow. """
    """Your primary responsibility is to coordinate all study material creation activities """
    """and define the overall learning plan. You work with specialized agents (Notes Generator, """
    """Example Solver, Quiz Maker) to ensure comprehensive coverage of the study topic. """
    """You ensure consistency, completeness, and quality across all educational materials."""
)


def create_study_manager_agent(
    tools: Optional[Iterable[object]] = None,
    llm_overrides: dict[str, Any] | None = None,
) -> Agent:
    """Create the study manager agent that orchestrates the educational workflow."""
    return Agent(
        name="Study Manager",
        role="Educational Workflow Coordinator and Study Plan Architect",
        goal="Orchestrate the creation of comprehensive study materials and define the learning plan and structure",
        backstory=(
            "You are an experienced educational coordinator with expertise in curriculum design and learning outcomes. "
            "You excel at breaking down complex topics into manageable learning units and coordinating multiple "
            "specialized agents to create cohesive study materials. Your attention to detail and organizational skills "
            "make you perfect for managing the entire educational workflow from planning to final integration."
        ),
        llm=build_crewai_llm(**(llm_overrides or {})),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []),
    )
