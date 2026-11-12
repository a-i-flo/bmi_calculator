# BMI calculator practice

A small Python exercise: one function plus a set of pytest tests.
More exercises in the same style are in `Practice_suggestions.md`.

## Setup with uv

Install uv if you do not have it yet:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

From the project root, create your own virtual environment and activate it.
The `.venv` folder is listed in `.gitignore`, so it is never committed and
everyone creates a fresh one:

```bash
uv venv
source .venv/bin/activate
```

Install the dependencies listed in `requirements.in`:

```bash
uv pip install -r requirements.in
```

## Running the tests

```bash
pytest
```

## Updating dependencies

Add a package name to `requirements.in`, then install again with the command above.
To refresh the pinned `requirements.txt` as well:

```bash
uv pip compile requirements.in -o requirements.txt
```
