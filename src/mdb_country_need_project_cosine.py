"""Country need–project cosine similarity for the MDB-SDG dashboard."""

from __future__ import annotations

import math
from typing import Dict, List, Optional


def _safe_float(value) -> Optional[float]:
    try:
        x = float(value)
        if not math.isfinite(x):
            return None
        return x
    except (TypeError, ValueError):
        return None


def _l2_normalize(vec: List[float]) -> Optional[List[float]]:
    norm = math.sqrt(sum((x * x) for x in vec))
    if norm <= 0:
        return None
    return [x / norm for x in vec]


def build_country_need_project_cosine(
    country_totals: dict,
    sdg_index: dict,
    years: List[int],
    *,
    include_vectors: bool = False,
) -> List[dict]:
    """
    Cosine similarity between:
    - project vector: country_totals per-SDG project counts (multi-label, all MDBs)
    - demand vector: max(0, 100 - avg SDG Index score) per goal

    Returns cosine_similarity=None when either vector cannot be normalized (e.g. no
    valid SDG Index goal scores in the selected years, or no projects).
    """
    out: List[dict] = []
    by_country = (country_totals or {}).get("by_country", {}) or {}
    sdg_countries = (sdg_index or {}).get("countries", {}) or {}

    for code, c in by_country.items():
        per_sdg = (c or {}).get("per_sdg") or []
        if not per_sdg or len(per_sdg) < 17:
            continue

        proj_vec: List[float] = []
        for s in range(17):
            rec = per_sdg[s] if s < len(per_sdg) else None
            proj_vec.append(float((rec or {}).get("total_project_count") or 0.0))

        country_idx_data = sdg_countries.get(code, {}) or {}
        year_rows = country_idx_data.get("years", []) or []
        sdg_sums = [0.0] * 17
        sdg_counts = [0] * 17
        for yr in year_rows:
            y = yr.get("year")
            if y not in years:
                continue
            sdg_scores = yr.get("sdg_scores") or {}
            for s in range(17):
                val = _safe_float(sdg_scores.get(f"SDG{s + 1}"))
                if val is None:
                    continue
                sdg_sums[s] += val
                sdg_counts[s] += 1

        demand_vec: List[float] = []
        for s in range(17):
            if sdg_counts[s] > 0:
                avg_score = sdg_sums[s] / sdg_counts[s]
                demand_vec.append(max(0.0, 100.0 - avg_score))
            else:
                demand_vec.append(0.0)

        proj_n = _l2_normalize(proj_vec)
        demand_n = _l2_normalize(demand_vec)
        if proj_n is None or demand_n is None:
            cosine = None
        else:
            cosine = sum((proj_n[i] * demand_n[i]) for i in range(17))

        row: Dict[str, object] = {"country_code": code, "cosine_similarity": cosine}
        if include_vectors:
            row["project_vector"] = [round(v, 6) for v in proj_vec]
            row["demand_vector"] = [round(v, 6) for v in demand_vec]
            row["valid_sdg_index_year_counts"] = sdg_counts
        out.append(row)

    out.sort(
        key=lambda r: (
            r["cosine_similarity"] is None,
            -(r["cosine_similarity"] if r["cosine_similarity"] is not None else -1.0),
            str(r["country_code"]),
        )
    )
    return out
