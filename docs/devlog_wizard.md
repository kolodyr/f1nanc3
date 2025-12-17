# Quest Log — f1nanc3 (wizard r & wizard k)

## ✅ Done (Quest 1–2)

### Quest 1 — dev deps in pyproject
- Added dev dependencies to `pyproject.toml` (pytest, ruff, pre-commit).
- Goal: single command `pip install -e ".[dev]"` works everywhere.

### Quest 2 — CI GitHub Actions
- Added `.github/workflows/tests.yml`
- Pipeline runs:
  - `pip install -e ".[dev]"`
  - `ruff check .`
  - `pytest -q`

## 🔥 Current blocker
- `pytest -q` failing due to typos in test:
  - `FIRECculator` → `FIRECalculator`
  - `annual_expences` → `annual_expenses`
  - missing import `from f1nanc3.fire_calculator import FIRECalculator`

## Next (Quest 3–4)
- Quest 3: add 5–10 meaningful tests for FIRECalculator + Portfolio
- Quest 4: README “Development” section with dev setup commands
