from typing import Dict, List, Tuple

ROOT_CAUSE_DIMENSIONS = ["Process", "Technology", "Organization", "Data", "Policy / Controls"]


PROCESS_KEYWORDS = [
    "manual", "spreadsheet", "excel", "too many steps", "handover",
    "bottleneck", "no standard", "not standardized", "rework", "approval flow"
]

TECH_KEYWORDS = [
    "sap", "oracle", "erp", "system issue", "no integration", "integration",
    "tool", "blackline", "anaplan", "rpa", "automation", "robot"
]

ORG_KEYWORDS = [
    "ownership", "roles", "responsibility", "raci", "capacity",
    "skills", "no accountability", "handoff", "handover"
]

DATA_KEYWORDS = [
    "data quality", "master data", "mapping", "chart of accounts", "coA",
    "duplicate", "inconsistent", "wrong data", "mis-match", "mismatch"
]

POLICY_KEYWORDS = [
    "policy", "control", "sox", "approval limit", "segregation of duties",
    "sod", "compliance", "audit", "threshold"
]


def _score_dimension(text: str, keywords: List[str]) -> int:
    text_lower = text.lower()
    score = 0
    for kw in keywords:
        if kw in text_lower:
            score += 1
    return score


def assess_root_causes(problem: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    Returns:
      scores_by_dimension: Dict[dimension, score]
      narrative_by_dimension: simple explanation text
    """
    dim_scores: Dict[str, int] = {}
    narratives: Dict[str, str] = {}

    dim_scores["Process"] = _score_dimension(problem, PROCESS_KEYWORDS)
    dim_scores["Technology"] = _score_dimension(problem, TECH_KEYWORDS)
    dim_scores["Organization"] = _score_dimension(problem, ORG_KEYWORDS)
    dim_scores["Data"] = _score_dimension(problem, DATA_KEYWORDS)
    dim_scores["Policy / Controls"] = _score_dimension(problem, POLICY_KEYWORDS)

    # Build simple explanations
    for dim, score in dim_scores.items():
        if score == 0:
            narratives[dim] = f"Limited explicit signals in your description. Treat {dim.lower()} as a secondary hypothesis to validate through data and interviews."
        elif score == 1:
            narratives[dim] = f"Some indicators that {dim.lower()} is contributing to the problem. Worth exploring root causes and quick wins."
        else:
            narratives[dim] = f"Strong signals that {dim.lower()} are a major driver of the issue. This should be a primary focus area in the transformation plan."

    return dim_scores, narratives
