from conhecimento import listar_regras

linhas = ["# Matriz de Decisão (Fase 1)", "",
          "Gerada automaticamente por `python gerar_matriz.py` a partir das regras em `conhecimento.py`.", "",
          "Cada regra que dispara soma (ou subtrai) pontos das trilhas; vence a trilha com mais pontos "
          "(desempate pelo número de regras positivas).", "",
          "| Regra | Efeito (pontos) | Condição (respostas que ativam a regra) |", "|---|---|---|"]
linhas += [f"| {i} | {e} | {c} |" for i, e, c in listar_regras()]
open("docs/matriz_decisao.md", "w", encoding="utf-8").write("\n".join(linhas) + "\n")
print(f"{len(listar_regras())} regras documentadas")
