# Governança Operacional — Definição Formal

## O que é governança neste projeto

Governança é a capacidade de um sistema:

1. Medir risco real
2. Decidir automaticamente
3. Conter falhas
4. Registrar prova
5. Permitir auditoria

Governança **não depende de explicabilidade interna**.

---

## Componentes obrigatórios

- Métrica de risco extremo (CVaR)
- Testes de robustez (metamórficos)
- Gate determinístico
- Ledger imutável
- Replay auditável

---

## O gate

O gate executa políticas humanas explícitas:

- `ALLOW`
- `DEGRADE`
- `BLOCK`

O gate **não decide valores**.  
Ele executa políticas previamente definidas.

---

## Governança dinâmica (UMJAM)

O sistema é tratado como sistema dinâmico:

mₜ₊₁ = (I − K)mₜ + KΘ

Estabilidade garantida se:

λ_max(K) < 1

Isso mantém o sistema dentro de envelope seguro.
