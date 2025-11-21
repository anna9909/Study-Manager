"""Entrypoint for running the Study Companion pipeline end-to-end."""
from __future__ import annotations

import argparse
import logging
import os
import sys

from dotenv import load_dotenv

from crew import run_educational_pipeline
from config.logging_config import configure_logging


def run_pipeline(topic: str) -> str:
    """Run the configured educational crew against the provided study topic."""
    load_dotenv()
    
    # Validate API key is present
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    if not api_key:
        error_msg = (
            "❌ OPENROUTER_API_KEY not found!\n\n"
            "Please set your API key:\n"
            "1. Create a .env file in the project root\n"
            "2. Add this line: OPENROUTER_API_KEY=your-api-key-here\n"
            "3. Get your key from: https://openrouter.ai/keys\n"
        )
        print(error_msg, file=sys.stderr)
        raise ValueError("OPENROUTER_API_KEY is missing")
    
    configure_logging()
    logging.getLogger(__name__).info("Starting Study Companion for topic: %s", topic)
    return run_educational_pipeline(topic)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Study Companion: Generate comprehensive study materials using AI agents."
    )
    parser.add_argument(
        "--topic",
        default="Introduction to Python Programming",
        help="Study topic to generate educational materials for (e.g., 'Calculus: Derivatives and Integration')",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    print("\n" + "="*70)
    print("📚 Study Companion - AI-Powered Study Pack Generator")
    print("="*70)
    print(f"\n🎯 Generating study materials for: {args.topic}")
    print("\n⏳ This may take 2-5 minutes. AI agents are working...\n")
    
    output = run_pipeline(args.topic)
    
    print("\n" + "="*70)
    print("✅ Study Pack Generated Successfully!")
    print("="*70 + "\n")
    print(output)
    print("\n" + "="*70)
    print("💡 Tip: Save this output to a .md file for easy reading!")
    print("="*70 + "\n")
