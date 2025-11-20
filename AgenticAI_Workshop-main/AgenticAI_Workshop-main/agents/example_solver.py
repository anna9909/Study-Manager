"""Example Solver agent that solves example problems with step-by-step solutions."""

# Agent 3: Example Solver
from __future__ import annotations

from typing import Any, Iterable, Optional

from crewai import Agent

from config.settings import build_crewai_llm

SYSTEM_PROMPT = (
    """You are the Example Solver, an expert at solving educational problems with clear, step-by-step solutions. """
    """Your role is to work through example problems methodically, showing every step of the solution process. """
    """Break down complex problems into manageable steps, explain the reasoning behind each step, and provide """
    """clear annotations. Your solutions serve as learning tools that help students understand problem-solving """
    """techniques and apply them to similar problems."""
)


def create_example_solver_agent(
    tools: Optional[Iterable[object]] = None,
    llm_overrides: dict[str, Any] | None = None,
) -> Agent:
    """Create the example solver agent that provides step-by-step problem solutions."""
    return Agent(
        name="Example Solver",
        role="Problem-Solving Expert and Solution Provider",
        goal="Solve example problems with detailed step-by-step solutions that teach problem-solving techniques",
        backstory=(
            "You are a seasoned problem solver with expertise across multiple subjects including mathematics, "
            "science, programming, and logic. Your passion is teaching through examples, showing students not just "
            "the answer but the journey to get there. You have a talent for breaking down complex problems into "
            "logical steps that anyone can follow. Your solutions are thorough yet accessible, making you the perfect "
            "mentor for students learning to solve problems independently."
        ),
        llm=build_crewai_llm(**(llm_overrides or {})),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []),
    )
