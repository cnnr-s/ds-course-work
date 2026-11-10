# ds-course-work

My work for a self-paced data science course: practice exercises and one project per chapter, built with Python and [uv](https://docs.astral.sh/uv/).

## Projects

| Chapter | Project | What it does |
|---|---|---|
| P1 Ch2 | [Transaction Log Parser](P1-python-foundations/ch02-project/) | Cleans a messy corporate card export, totals spend by category, and reports lines it couldn't read. |

## Repository layout

```
ds-course-work/
├── P1-python-foundations/
│   └── ch02-project/
│       ├── parse_transactions_script.py       # final script
│       └── parse_transactions_notebook.ipynb  # notebook used while building it
├── pyproject.toml   # project settings and dependencies
├── uv.lock          # exact dependency versions
└── README.md
```

## Running a project

```powershell
uv sync                                   # create the .venv from uv.lock
cd P1-python-foundations\ch02-project
uv run parse_transactions_script.py
```

## Tools

- Python 3.14
- uv for environments and dependencies
- Git and GitHub for version control
