import argparse
from omega.cvar import cvar
from omega.gate import omega_gate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--losses", nargs="+", type=float, required=True)
    parser.add_argument("--allow", type=float, default=0.1)
    parser.add_argument("--block", type=float, default=0.3)
    args = parser.parse_args()

    risk = cvar(args.losses)
    decision = omega_gate(risk, args.allow, args.block)

    print("CVaR:", risk)
    print("DECISION:", decision)


if __name__ == "__main__":
    main()
