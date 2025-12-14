def envelope_state(metrics, limits):
    """
    Determina envelope operacional.
    """
    for key, value in metrics.items():
        if value >= limits["QUARANTINE"].get(key, float("inf")):
            return "QUARANTINE"
        if value >= limits["FREEZE"].get(key, float("inf")):
            return "FREEZE"
        if value >= limits["SAFE"].get(key, float("inf")):
            return "SAFE"
    return "RUN"
