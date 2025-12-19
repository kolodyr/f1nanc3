import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_PATH = ROOT_DIR / "src"

src_str = str(SRC_PATH)
if src_str not in sys.path:
    sys.path.insert(0, src_str)
