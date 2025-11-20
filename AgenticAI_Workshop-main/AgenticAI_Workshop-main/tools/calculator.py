"""Educational calculator tool for solving mathematical problems in study materials."""
from __future__ import annotations

import ast
import logging
import operator
import math
from typing import Any, Dict

from crewai.tools import BaseTool

_ALLOWED_OPERATORS: Dict[type[ast.AST], Any] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

# Safe mathematical functions for educational calculations
_ALLOWED_FUNCTIONS = {
    'sqrt': math.sqrt,
    'abs': abs,
    'round': round,
    'pow': pow,
}


class EducationalCalculator(BaseTool):
    name: str = "educational_calculator"
    description: str = (
        "Perform mathematical calculations for educational problems and examples. "
        "Supports arithmetic operations (+, -, *, /, %, **), square roots, absolute values, and rounding. "
        "Perfect for solving practice problems, verifying solutions, and creating step-by-step examples. "
        "Example: '2 + 2', '5 * 10 / 2', '2 ** 3' (2 to the power of 3)."
    )

    _logger = logging.getLogger(__name__)

    def _run(self, query: str) -> str:
        """Evaluate a mathematical expression for educational purposes."""
        try:
            # Clean the query
            query = query.strip()
            expression = ast.parse(query, mode="eval").body
            result = self._eval(expression)
            
            # Format result nicely for educational context
            if isinstance(result, float):
                # Round to 4 decimal places for cleaner output
                if result == int(result):
                    result = int(result)
                else:
                    result = round(result, 4)
            
            self._logger.info("Educational calculator: '%s' = %s", query, result)
            return f"Calculation: {query} = {result}"
        except Exception as exc:  # pragma: no cover - defensive layer
            self._logger.exception("Calculator failed for expression '%s'", query)
            return f"Error: Unable to calculate '{query}'. Please check the expression format."

    def _eval(self, node: ast.AST) -> float:
        if isinstance(node, ast.Num):  # type: ignore[attr-defined]
            return float(node.n)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
            return _ALLOWED_OPERATORS[type(node.op)](self._eval(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
            left = self._eval(node.left)
            right = self._eval(node.right)
            return _ALLOWED_OPERATORS[type(node.op)](left, right)
        raise ValueError(f"Unsupported expression: {ast.dump(node, include_attributes=False)}")
