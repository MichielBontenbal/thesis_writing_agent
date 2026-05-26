# thesis_writing_agent

A lightweight Python project for a Claude-style thesis writing agent.

## What it does

The agent creates a practical thesis writing plan by producing:
- a sectioned thesis outline
- an initial draft scaffold
- revision notes for final polishing

## Quick usage

```python
from thesis_writing_agent import ThesisWritingAgent

agent = ThesisWritingAgent()
plan = agent.build_plan(
    title="AI Assisted Writing",
    research_question="How can LLMs support thesis drafting quality?",
    key_points=["scope", "method", "evaluation"],
)

print(plan.outline)
print(plan.draft)
print(plan.revision_notes)
```

## Running tests

```bash
python -m unittest discover -s tests -p 'test_*.py'
```
