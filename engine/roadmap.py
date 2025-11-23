from typing import Dict, List


def build_roadmap(primary_domain: str, dim_scores: Dict[str, int]) -> Dict[str, List[str]]:
    """
    Very simple, generic roadmap builder.
    Returns a dict with keys: quick_wins, mid_term, long_term
    """
    quick_wins: List[str] = []
    mid_term: List[str] = []
    long_term: List[str] = []

    # Prioritize dimensions with highest scores
    sorted_dims = sorted(dim_scores.items(), key=lambda x: x[1], reverse=True)
    top_dims = [d for d, s in sorted_dims if s > 0][:2]

    # Generic building blocks
    if not top_dims:
        quick_wins.append("Run a 2–3 week diagnostic: process walkthroughs, data sampling, and stakeholder interviews to clarify the real root causes.")
        mid_term.append("Design a target-state process and operating model for the selected finance area.")
        long_term.append("Implement enabling technology (ERP / automation / reporting) once process and ownership are clarified.")
    else:
        for dim in top_dims:
            if dim == "Process":
                quick_wins.append("Map the current end-to-end process (AS-IS) with SIPOC / swimlanes and highlight bottlenecks and rework.")
                mid_term.append("Design and approve a simplified TO-BE process with standard work, clear inputs/outputs, and fewer handoffs.")
                long_term.append("Embed continuous improvement (Kaizen) cadence with KPIs on cycle time, touchless rate, and error rate.")
            elif dim == "Technology":
                quick_wins.append("List all systems, tools, and manual spreadsheets currently used for this process.")
                mid_term.append("Define requirements and perform a light fit-gap to existing ERP / automation / reconciliation / planning tools.")
                long_term.append("Implement or expand standardized tooling, decommission shadow Excel solutions, and integrate data flows.")
            elif dim == "Organization":
                quick_wins.append("Clarify RACI for the process and agree interim owners for critical activities.")
                mid_term.append("Redesign team structure / roles to align with the TO-BE process and centralize or standardize where possible.")
                long_term.append("Build capability plans (training, hiring, upskilling) to sustain the new operating model.")
            elif dim == "Data":
                quick_wins.append("Identify the 2–3 most painful data issues (e.g., COA mapping, master data, duplicate vendors) and quantify impact.")
                mid_term.append("Define data ownership, quality rules, and cleansing approach for the target state.")
                long_term.append("Implement ongoing data governance and monitoring with clear KPIs and tooling.")
            elif dim.startswith("Policy"):
                quick_wins.append("List key policies and controls touching this process; identify obvious overlaps and gaps.")
                mid_term.append("Rationalize policies and controls to match the redesigned process and risk appetite.")
                long_term.append("Automate control execution and monitoring where feasible (system-based controls, workflows, audit trails).")

    # Domain-specific sentence to add flavor
    domain_note = f"Roadmap is focused on strengthening {primary_domain}."

    return {
        "quick_wins": quick_wins,
        "mid_term": mid_term,
        "long_term": long_term,
        "note": [domain_note],
    }
