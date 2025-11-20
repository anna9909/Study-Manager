"""Educational knowledge retrieval tool using FAISS-backed RAG for study material creation."""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

from langchain_core.documents import Document
from crewai.tools import BaseTool
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from pydantic import Field, PrivateAttr

DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_VECTORSTORE_DIR = Path(__file__).resolve().parents[1] / "rag" / "vectorstore"


class EducationalKnowledgeRetriever(BaseTool):
    name: str = "educational_knowledge_search"
    description: str = (
        "Search the educational knowledge base for accurate information, learning principles, "
        "and subject matter content. This tool retrieves relevant educational material from the "
        "Study Companion's curated knowledge base. Use it to find: definitions, key concepts, "
        "learning strategies, subject-specific information, and educational best practices. "
        "Perfect for creating accurate study notes, examples, and assessments."
    )
    vectorstore_path: Path = Field(default_factory=lambda: DEFAULT_VECTORSTORE_DIR)
    top_k: int = 4
    embedding_model: str = DEFAULT_EMBEDDING_MODEL

    _vectorstore: Optional[FAISS] = PrivateAttr(default=None)
    _logger = logging.getLogger(__name__)

    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.vectorstore_path = Path(self.vectorstore_path)

    def _load_vectorstore(self) -> FAISS:
        if self._vectorstore is not None:
            return self._vectorstore

        if not self.vectorstore_path.exists():
            self._logger.error(
                "Vector store missing at %s. Did you run rag/build_vector_db.py?",
                self.vectorstore_path,
            )
            raise FileNotFoundError(
                f"Vector store not found at {self.vectorstore_path}. Run 'python rag/build_vector_db.py' first."
            )

        embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model)
        self._vectorstore = FAISS.load_local(
            folder_path=str(self.vectorstore_path),
            embeddings=embeddings,
            allow_dangerous_deserialization=True,
        )
        self._logger.info(
            "Loaded FAISS vector store from %s using embedding model %s",
            self.vectorstore_path,
            self.embedding_model,
        )
        return self._vectorstore

    def _run(self, query: str) -> str:
        """Retrieve educational content from the knowledge base."""
        store = self._load_vectorstore()
        docs = store.similarity_search(query, k=self.top_k)
        if not docs:
            return (
                "No relevant information found in the educational knowledge base for this query. "
                "Consider using web search for additional information."
            )

        formatted = self._format_docs(docs)
        self._logger.info(
            "Educational knowledge retriever found %d relevant passages for: '%s'", 
            len(docs), query
        )
        return formatted

    @staticmethod
    def _format_docs(docs: list[Document]) -> str:
        """Format retrieved documents for educational context."""
        formatted = []
        for idx, doc in enumerate(docs, start=1):
            content = doc.page_content.strip()
            formatted.append(
                f"📚 Educational Resource {idx}:\n{content}\n"
                f"{'─' * 60}"
            )
        return "\n\n".join(formatted)
