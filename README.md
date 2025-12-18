# OpenBox — Governança de Sistemas Caixa-Preta

> **Este repositório ensina por que explicar modelos não governa sistemas —  
> e mostra o que governa.**

A indústria de IA investe bilhões tentando responder **“por que o modelo fez isso?”**  
Essa curiosidade não mitiga erros, não reduz risco extremo e não impede falhas.

Este repositório existe para demonstrar, com **engenharia executável**, que:

> **Governança não é explicação.  
> Governança é decisão, contenção e prova.**

---

## O problema real

> **O problema da caixa-preta não é não saber como o modelo funciona.  
> É não saber se ele pode rodar, com qual risco, e quem responde se falhar.**

---

## O que é Governança (definição prática)

Neste projeto, governança significa:

- medir risco real (especialmente risco de cauda),
- testar robustez sob perturbação,
- decidir automaticamente se algo pode rodar,
- registrar prova auditável do ocorrido,
- conter falhas antes que virem dano.

> **No proof, no run.**

---

## O que este repositório implementa

### 1. Governança Operacional — Ω-MIN / OpenBox
- CVaR para risco extremo  
- Testes metamórficos  
- Gate automático: `ALLOW · DEGRADE · BLOCK`  
- Ledger append-only com hash encadeado  
- Replay determinístico  

### 2. Governança Dinâmica — UMJAM
- Controle afim externo  
- Estabilidade garantida se `λ_max(K) < 1`  
- Envelopes: `RUN · SAFE · FREEZE · QUARANTINE`

### 3. Governança Verificável — MatVerseChain
- Prova pública (PoSE / PoLE)
- Indexação e auditoria externa
- Não-repúdio

---

## O que este projeto NÃO promete

- ❌ Explicar pesos internos  
- ❌ Justificar decisões para humanos  
- ❌ Controle total do modelo  
- ❌ Zero risco  

> Este projeto **reduz dano esperado, contém falhas e prova decisões**.

---

## Como ler este repositório

1. `OPEN_LETTER.md`  
2. `WHY_NOT_XAI.md`  
3. `diagrams/why_vs_governance.md`
4. `GOVERNANCE.md`
5. Código em `openbox/`
6. Visão epistêmica e comercial em `SYMBIOS.md`

---

## Frase-âncora

> **Explicar um modelo não governa um sistema.  
> Governar um sistema não exige explicar o modelo.**

---

Se você discorda, ótimo.  
Leia os documentos acima e abra uma issue técnica.
