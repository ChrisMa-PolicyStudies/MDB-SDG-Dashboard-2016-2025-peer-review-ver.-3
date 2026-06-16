"""World Bank FY26 income groups from OGHIST, with documented gap fills."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Union

FY26_INCOME_GROUPS_FILENAME = "world_bank_fy26_income_groups.json"
OGHIST_XLSX_FILENAME = "OGHIST_2026_03_10.xlsx"

# FY26 cell blank in OGHIST (2026-03-10 export); use last consistent pre-gap classification.
OGHIST_FY26_INCOME_OVERRIDES: Dict[str, str] = {
    "ETH": "L",  # FY00–FY25 consistently L
    "VEN": "UM",  # FY00–FY21 consistently UM; FY22–FY26 blank
}

GROUP_CODE_LABELS: Dict[str, str] = {
    "L": "Low income (L)",
    "LM": "Lower-middle income (LM)",
    "UM": "Upper-middle income (UM)",
    "H": "High income (H)",
    "Unknown": "Unknown",
}

ProjectRoot = Union[str, Path]


def fy26_income_groups_json_path(project_root: ProjectRoot) -> Path:
    return Path(project_root) / "data" / FY26_INCOME_GROUPS_FILENAME


def oghist_xlsx_path(project_root: ProjectRoot) -> Path:
    return Path(project_root) / "data" / OGHIST_XLSX_FILENAME


def _parse_oghist_xlsx(xlsx_path: Path) -> Dict[str, str]:
    """Parse FY26 income group column from OGHIST Country Analytical History sheet."""
    import pandas as pd

    out: Dict[str, str] = {}
    raw = pd.read_excel(xlsx_path, sheet_name="Country Analytical History", header=None)
    fy_row_idx = None
    for i in range(min(30, raw.shape[0])):
        v = raw.iloc[i, 1]
        if isinstance(v, str) and "Bank's fiscal year" in v:
            fy_row_idx = i
            break
    if fy_row_idx is None:
        return out
    fy26_col = None
    for c in range(2, raw.shape[1]):
        val = raw.iloc[fy_row_idx, c]
        if isinstance(val, str) and val.strip() == "FY26":
            fy26_col = c
            break
    if fy26_col is None:
        return out
    data_start = fy_row_idx + 7
    for r in range(data_start, raw.shape[0]):
        iso3 = raw.iloc[r, 0]
        if not isinstance(iso3, str):
            continue
        code = iso3.strip().upper()
        if len(code) != 3:
            continue
        g = raw.iloc[r, fy26_col]
        if isinstance(g, str):
            gg = g.strip()
            out[code] = gg if gg else "Unknown"
        else:
            out[code] = "Unknown"
    return out


def _apply_overrides(countries: Dict[str, str]) -> Dict[str, str]:
    out = dict(countries)
    out.update(OGHIST_FY26_INCOME_OVERRIDES)
    return out


def build_fy26_income_groups_payload(
    countries: Dict[str, str],
    *,
    source_xlsx: str = OGHIST_XLSX_FILENAME,
) -> dict:
    merged = _apply_overrides(countries)
    return {
        "description": "World Bank FY26 income group per ISO alpha-3 (OGHIST + documented overrides).",
        "fiscal_year": "FY26",
        "source_xlsx": source_xlsx,
        "group_codes": GROUP_CODE_LABELS,
        "overrides": dict(OGHIST_FY26_INCOME_OVERRIDES),
        "country_count": len(merged),
        "countries": dict(sorted(merged.items())),
    }


def write_fy26_income_groups_json(project_root: ProjectRoot, *, xlsx_path: Path | None = None) -> Path:
    """Build world_bank_fy26_income_groups.json from OGHIST xlsx (or overrides only if missing)."""
    root = Path(project_root)
    src = xlsx_path or oghist_xlsx_path(root)
    if src.is_file():
        countries = _parse_oghist_xlsx(src)
        source_name = src.name
    else:
        countries = {}
        source_name = OGHIST_XLSX_FILENAME
    payload = build_fy26_income_groups_payload(countries, source_xlsx=source_name)
    out_path = fy26_income_groups_json_path(root)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    return out_path


def load_fy26_income_groups(project_root: ProjectRoot) -> Dict[str, str]:
    """FY26 income group per ISO alpha-3. Prefers data/world_bank_fy26_income_groups.json."""
    root = Path(project_root)
    json_path = fy26_income_groups_json_path(root)
    if json_path.is_file():
        with json_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        countries = data.get("countries") or {}
        return _apply_overrides({str(k).upper(): v for k, v in countries.items()})

    xlsx_path = oghist_xlsx_path(root)
    if xlsx_path.is_file():
        try:
            return _apply_overrides(_parse_oghist_xlsx(xlsx_path))
        except Exception:
            return {**OGHIST_FY26_INCOME_OVERRIDES}

    return {**OGHIST_FY26_INCOME_OVERRIDES}
