"""Task definitions for the Educational Workflow System."""
from __future__ import annotations

from typing import List

from crewai import Task

from tools import create_calculator_tool, create_knowledge_retriever, create_web_search_tool


def create_study_management_task(agent, tools=None) -> Task:
    """Task 1: Orchestrate the educational workflow and define the study plan."""
    tools = list(tools) if tools is not None else [
        create_knowledge_retriever(),
        create_web_search_tool(),
        create_calculator_tool(),
    ]
    return Task(
        description=(
            "Analyze the study topic '{topic}' and create a comprehensive learning plan. "
            "Define learning objectives, identify key concepts to cover, and establish "
            "the structure for the final study pack. Coordinate with other agents to ensure "
            "complete coverage of notes, examples, quizzes, and visual aids."
        ),
        expected_output=(
            "A detailed study plan outlining: 1) Learning objectives, 2) Key topics and subtopics, "
            "3) Coordination guidelines for other agents, 4) Quality criteria, and 5) Final study pack structure."
        ),
        agent=agent,
        tools=tools,
        name="Study Management & Planning",
    )


def create_notes_generation_task(agent, tools=None) -> Task:
    """Task 2: Generate easy-to-understand notes and summaries."""
    tools = list(tools) if tools is not None else [
        create_knowledge_retriever(),
        create_web_search_tool(),
        create_calculator_tool(),
    ]
    return Task(
        description=(
            "Create comprehensive yet easy-to-understand study notes on '{topic}'. "
            "Use the knowledge base and web search tools to gather accurate information. "
            "Transform complex concepts into clear, bullet-point notes. Include: "
            "1) Key definitions, 2) Core concepts explained simply, 3) Important facts and principles, "
            "4) Concise summaries of each major topic. Organize notes logically with clear headings."
        ),
        expected_output=(
            "Well-structured study notes in bullet-point format with clear section headings. "
            "Each section should include: definitions, key concepts, important points, and a brief summary. "
            "Notes should be concise, easy to read, and suitable for quick review and deep study."
        ),
        agent=agent,
        tools=tools,
        name="Notes Generation",
    )


def create_example_solving_task(agent, tools=None) -> Task:
    """Task 3: Solve example problems with step-by-step solutions."""
    tools = list(tools) if tools is not None else [
        create_calculator_tool(),
        create_knowledge_retriever(),
        create_web_search_tool(),
    ]
    return Task(
        description=(
            "Create and solve example problems related to '{topic}'. "
            "Generate 3-5 relevant example problems that cover key concepts. "
            "For each problem, provide: 1) Clear problem statement, 2) Step-by-step solution "
            "with detailed explanations, 3) Reasoning behind each step, 4) Final answer. "
            "Use the calculator tool for any numerical computations. Problems should range "
            "from basic to intermediate difficulty."
        ),
        expected_output=(
            "A collection of 3-5 solved example problems. Each problem should include: "
            "- Problem Statement (clear and specific), "
            "- Step-by-Step Solution (numbered steps with explanations), "
            "- Annotations explaining the reasoning, "
            "- Final Answer with verification where applicable."
        ),
        agent=agent,
        tools=tools,
        name="Example Problem Solving",
    )


def create_quiz_making_task(agent, tools=None) -> Task:
    """Task 4: Create practice questions including MCQs and short answers."""
    tools = list(tools) if tools is not None else [
        create_knowledge_retriever(),
        create_web_search_tool(),
    ]
    return Task(
        description=(
            "Design a comprehensive practice quiz for '{topic}'. Create: "
            "1) 10 Multiple Choice Questions (MCQs) with 4 options each, "
            "2) 5 Short Answer Questions, "
            "3) A detailed answer key with explanations. "
            "Questions should test different cognitive levels: recall, understanding, "
            "application, and analysis. Ensure questions are clear, fair, and educationally valuable. "
            "The answer key should explain why each answer is correct and address common misconceptions."
        ),
        expected_output=(
            "A complete practice quiz containing: "
            "- Section 1: 10 MCQs with 4 options each (labeled A-D), "
            "- Section 2: 5 Short Answer Questions, "
            "- Section 3: Comprehensive Answer Key with: "
            "  * Correct answers for all questions, "
            "  * Detailed explanations for each answer, "
            "  * Common mistakes to avoid."
        ),
        agent=agent,
        tools=tools,
        name="Quiz Creation",
    )



def build_educational_tasks(
    study_manager,
    notes_generator,
    example_solver,
    quiz_maker,
    tools=None
) -> List[Task]:
    """Create the full educational task list for all agents."""
    return [
        create_study_management_task(study_manager, tools=tools),
        create_notes_generation_task(notes_generator, tools=tools),
        create_example_solving_task(example_solver, tools=tools),
        create_quiz_making_task(quiz_maker, tools=tools),
    ]
