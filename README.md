# Tiny Chess 4K

A strong chess engine in one Python file (stdlib only, deterministic).

- PeSTO middlegame eval (packed PST), PVS + alpha-beta, transposition
  table, null-move, LMR, quiescence, MVV-LVA ordering.
- Fixed node budget (no clock, no randomness). UCI over HTTP
  to the Make.fun harness (`MAKEFUN_ENV_URL`).

Run: `python3 main.py` (needs `MAKEFUN_ENV_URL`, `NODE_BUDGET`, `MAX_DEPTH`).
