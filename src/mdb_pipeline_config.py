"""Paths and MDB lists for the GitHub MDB-SDG Dashboard build."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import List

from ogh_income_groups import FY26_INCOME_GROUPS_FILENAME

PROJECT_ROOT = str(Path(__file__).resolve().parent.parent)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
FY26_INCOME_GROUPS_JSON = os.path.join(DATA_DIR, FY26_INCOME_GROUPS_FILENAME)

MDB_ORGANIZATIONS: List[str] = [
    "WBG", "ADB", "AfDB", "IsDB", "IDB", "EIB", "EBRD", "AIIB", "NDB", "CEB", "IFC",
]

MDB_SIDEBAR_ORDER: List[str] = [
    "WBG", "IFC", "ADB", "AfDB", "IsDB", "IDB", "CEB", "EBRD", "EIB", "AIIB", "NDB",
]


@dataclass(frozen=True)
class PipelineConfig:
    mdb_organizations: List[str]
    output_suffix: str = ""

    def out_path(self, base: str) -> str:
        return os.path.join(DATA_DIR, f"{base}{self.output_suffix}.json")


CONFIG = PipelineConfig(mdb_organizations=MDB_ORGANIZATIONS)
