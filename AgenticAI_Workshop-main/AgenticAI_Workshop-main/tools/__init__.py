"""Educational tool factories for the Study Companion system."""
from __future__ import annotations

from pathlib import Path
from typing import List

from crewai.tools import BaseTool

from .calculator import EducationalCalculator
from .rag_tool import EducationalKnowledgeRetriever
from .web_search import create_web_search_tool

__all__ = [
    "create_knowledge_retriever",
    "create_web_search_tool",
    "create_calculator_tool",
    "get_default_toolkit",
]


DEFAULT_VECTORSTORE_DIR = Path(__file__).resolve().parents[1] / "rag" / "vectorstore"


def create_knowledge_retriever(vectorstore_path: Path | None = None, *, top_k: int = 4) -> EducationalKnowledgeRetriever:
    """Instantiate the educational knowledge retrieval tool (RAG)."""
    target_path = vectorstore_path or DEFAULT_VECTORSTORE_DIR
    return EducationalKnowledgeRetriever(vectorstore_path=target_path, top_k=top_k)


def create_calculator_tool() -> EducationalCalculator:
    """Instantiate the educational calculator tool for mathematical problem-solving."""
    return EducationalCalculator()


def get_default_toolkit() -> List[BaseTool]:
    """Provide the standard set of educational tools for Study Companion agents."""
    return [
        create_knowledge_retriever(),
        create_web_search_tool(),
        create_calculator_tool(),
    ]
