from omega.cvar import cvar
from omega.gate import omega_gate
from ledger.hashchain import Ledger


def main():
    losses = [0.01, 0.02, 0.5, 0.9]
    risk = cvar(losses, alpha=0.95)

    decision = omega_gate(
        cvar_value=risk,
        threshold_allow=0.1,
        threshold_block=0.3
    )

    ledger = Ledger()
    record = ledger.append({
        "risk": risk,
        "decision": decision
    })

    print("Decision:", decision)
    print("Ledger entry:", record)


if __name__ == "__main__":
    main()
