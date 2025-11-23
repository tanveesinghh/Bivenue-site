from typing import Dict, List, Tuple

FINANCE_DOMAINS = {
    "Record to Report (R2R)": [
        "month end", "month-end", "close", "closing", "journals",
        "reconciliation", "reconciliations", "gl", "general ledger",
        "fixed asset", "fa register", "trial balance"
    ],
    "Intercompany (IC)": [
        "intercompany", "i/c", "ic mismatch", "ic mismatches", "ic recon",
        "due to", "due from", "ic balance", "ic elimination"
    ],
    "Consolidation & Group Reporting": [
        "consolidation", "group reporting", "group close", "elimination",
        "subsidiary", "ifrs", "us gaap", "statutory", "segment reporting"
    ],
    "Procure to Pay (P2P)": [
        "purchase order", "po", "goods receipt", "grn", "vendor invoice",
        "3-way match", "3 way match", "ap", "accounts payable", "supplier"
    ],
    "Order to Cash (O2C)": [
        "order entry", "order booking", "sales order", "ar", "accounts receivable",
        "billing", "invoice", "collections", "credit note", "dso", "cash application"
    ],
    "FP&A": [
        "budget", "forecast", "variance", "plan vs actual", "planning",
        "driver based", "scenario", "long range plan", "lrp"
    ],
}


def _score_domain(text: str, keywords: List[str]) -> int:
    text_lower = text.lower()
    score = 0
    for kw in keywords:
        if kw in text_lower:
            score += 1
    return score


def classify_domain(problem: str) -> Tuple[str, Dict[str, int]]:
    """
    Very simple keyword-based classifier.
    Returns (primary_domain, scores_by_domain)
    """
    scores: Dict[str, int] = {}
    for domain, kws in FINANCE_DOMAINS.items():
        scores[domain] = _score_domain(problem, kws)

    # Pick domain with highest score; if all zero, mark as "General Finance Transformation"
    primary = max(scores, key=lambda d: scores[d]) if scores else "General Finance Transformation"
    if scores and scores[primary] == 0:
        primary = "General Finance Transformation"

    return primary, scores
