import unittest

from thesis_writing_agent import ThesisWritingAgent


class ThesisWritingAgentTests(unittest.TestCase):
    def test_build_plan_returns_expected_structure(self) -> None:
        agent = ThesisWritingAgent()

        plan = agent.build_plan(
            title="AI Assisted Writing",
            research_question="How can LLMs support thesis drafting quality?",
            key_points=["scope", "method", "evaluation"],
        )

        self.assertEqual(plan.title, "AI Assisted Writing")
        self.assertIn("1. Introduction", plan.outline)
        self.assertIn("Research question: How can LLMs support thesis drafting quality?", plan.draft)
        self.assertIn("scope, method, evaluation", plan.revision_notes)

    def test_build_plan_rejects_empty_inputs(self) -> None:
        agent = ThesisWritingAgent()

        with self.assertRaises(ValueError):
            agent.build_plan(title="", research_question="rq", key_points=["point"])

        with self.assertRaises(ValueError):
            agent.build_plan(title="title", research_question="", key_points=["point"])

        with self.assertRaises(ValueError):
            agent.build_plan(title="title", research_question="rq", key_points=[" "])


if __name__ == "__main__":
    unittest.main()
