"""Agent factory functions for the Educational Workflow System."""
from .study_manager import create_study_manager_agent
from .notes_generator import create_notes_generator_agent
from .example_solver import create_example_solver_agent
from .quiz_maker import create_quiz_maker_agent

__all__ = [
    "create_study_manager_agent",
    "create_notes_generator_agent",
    "create_example_solver_agent",
    "create_quiz_maker_agent",
]
