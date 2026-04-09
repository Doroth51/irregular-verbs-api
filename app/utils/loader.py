import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "irregular_verbs_full.csv"


def load_verbs():
    verbs = []
    with DATA_PATH.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            verbs.append(row)

        return verbs
