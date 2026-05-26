# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`thesis_writing_agent` is a Python project. The repository is in early stages — no source code exists yet.

## Environment

- Use `uv` to create virtual environments and install packages (preferred over `pip`/`venv`):
  ```bash
  uv venv .venv
  source .venv/bin/activate
  uv pip install <packages>
  ```
- The `.gitignore` covers Streamlit (`.streamlit/secrets.toml`) and Jupyter (`.ipynb_checkpoints`), suggesting the app may use one or both.
