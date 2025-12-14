from omega.gate import omega_gate


def execute_or_interdict(cvar_value, allow=0.1, block=0.3):
    decision = omega_gate(
        cvar_value,
        threshold_allow=allow,
        threshold_block=block,
    )

    if decision == "BLOCK":
        raise RuntimeError("Execution interdicted by governance gate")

    return decision
