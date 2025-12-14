def omega_gate(cvar_value, threshold_allow, threshold_block):
    """
    Gate decisório automático.
    Nenhuma decisão humana.
    """
    if cvar_value <= threshold_allow:
        return "ALLOW"

    if cvar_value >= threshold_block:
        return "BLOCK"

    return "DEGRADE"
