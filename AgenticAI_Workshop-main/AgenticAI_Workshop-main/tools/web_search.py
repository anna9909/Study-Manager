"""Educational web search tool powered by DuckDuckGo for study material research."""
from __future__ import annotations

import logging
from typing import Any

from crewai.tools import BaseTool
from duckduckgo_search import DDGS
from pydantic import Field


class EducationalWebSearch(BaseTool):
    """Web search tool optimized for educational content and study material research."""

    name: str = "educational_web_search"
    description: str = (
        "Search the web for educational content, definitions, examples, and current information. "
        "Use this tool to find: detailed explanations of concepts, real-world examples, "
        "recent developments in a subject, verified facts and statistics, learning resources, "
        "and educational references. Provide a clear, specific search query related to the study topic. "
        "Example queries: 'photosynthesis process explained', 'quadratic equation examples', "
        "'Python list comprehension tutorial'."
    )
    max_results: int = Field(default=5, ge=1, description="Number of hits to return")
    backend: str = Field(
        default="text",
        description="DuckDuckGo backend to use (text, news, images).",
    )

    _logger = logging.getLogger(__name__)

    def _run(self, query: str) -> str:
        """Search the web for educational content."""
        self._logger.info("Educational web search for: %s", query)
        results = self._search(query)
        if not results:
            return (
                f"No web results found for '{query}'. Try rephrasing the search query "
                "or use more specific educational terms."
            )

        formatted = []
        for index, item in enumerate(results, start=1):
            title = item.get("title") or item.get("heading") or "Untitled result"
            url = item.get("href") or item.get("url") or ""
            summary = (
                item.get("body")
                or item.get("snippet")
                or item.get("description")
                or "No summary provided."
            )
            formatted.append(
                f"🔍 Source {index}: {title}\n"
                f"📎 URL: {url}\n"
                f"📄 Summary: {summary.strip()}\n"
                f"{'─' * 60}"
            )

        serialized = "\n\n".join(formatted)
        self._logger.info("Found %d educational web results for: %s", len(results), query)
        return serialized

    def _search(self, query: str) -> list[dict[str, Any]]:
        try:
            with DDGS() as ddgs:
                if self.backend == "news":
                    iterator = ddgs.news(query, max_results=self.max_results)
                elif self.backend == "images":
                    iterator = ddgs.images(query, max_results=self.max_results)
                else:
                    iterator = ddgs.text(query, max_results=self.max_results)
                return list(iterator)
        except Exception as exc:  # pragma: no cover - network variability
            self._logger.exception("DuckDuckGo search failed for '%s'", query)
            raise ValueError(f"DuckDuckGo search failed: {exc}") from exc


def create_web_search_tool() -> EducationalWebSearch:
    """Create an educational web search tool optimized for study material research."""
    return EducationalWebSearch(max_results=5)
