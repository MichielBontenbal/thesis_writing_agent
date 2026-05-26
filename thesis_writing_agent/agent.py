"""Core thesis writing agent implementation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class ThesisPlan:
    """Structured output for the generated thesis plan."""

    title: str
    research_question: str
    outline: str
    draft: str
    revision_notes: str


class ThesisWritingAgent:
    """Small, dependency-free thesis writing agent.

    The agent creates a practical first pass by guiding users through:
    1. Defining the title and research question.
    2. Producing a sectioned outline.
    3. Generating a draft from key points.
    4. Producing revision guidance for quality improvement.
    """

    DEFAULT_SECTIONS = (
        "Introduction",
        "Literature Review",
        "Methodology",
        "Results",
        "Discussion",
        "Conclusion",
    )

    def build_plan(
        self,
        *,
        title: str,
        research_question: str,
        key_points: Iterable[str],
    ) -> ThesisPlan:
        cleaned_points = [point.strip() for point in key_points if point.strip()]
        if not title.strip():
            raise ValueError("title must not be empty")
        if not research_question.strip():
            raise ValueError("research_question must not be empty")
        if not cleaned_points:
            raise ValueError("key_points must include at least one non-empty item")

        outline = self._build_outline()
        draft = self._build_draft(title=title, research_question=research_question, key_points=cleaned_points)
        revision_notes = self._build_revision_notes(cleaned_points)

        return ThesisPlan(
            title=title.strip(),
            research_question=research_question.strip(),
            outline=outline,
            draft=draft,
            revision_notes=revision_notes,
        )

    def _build_outline(self) -> str:
        return "\n".join(f"{index}. {section}" for index, section in enumerate(self.DEFAULT_SECTIONS, start=1))

    def _build_draft(self, *, title: str, research_question: str, key_points: list[str]) -> str:
        points = "\n".join(f"- {point}" for point in key_points)
        return (
            f"Title: {title.strip()}\n"
            f"Research question: {research_question.strip()}\n\n"
            "Core points to expand in the thesis:\n"
            f"{points}\n\n"
            "Suggested writing flow:\n"
            "- Open with problem framing and contribution.\n"
            "- Connect each core point to evidence from literature.\n"
            "- Close each chapter with a transition to the next section."
        )

    def _build_revision_notes(self, key_points: list[str]) -> str:
        return (
            "Revision checklist:\n"
            "- Verify each claim has a citation.\n"
            "- Ensure argument progression is explicit between sections.\n"
            "- Validate methods and results alignment.\n"
            f"- Confirm these key points are represented: {', '.join(key_points)}."
        )
