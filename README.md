# 🧭 Consultor Inteligente de Carreiras em TI

Sistema Especialista baseado em regras (Python + [Experta](https://github.com/nilp0inter/experta)) com interface
web em [Streamlit](https://streamlit.io). O sistema entrevista o usuário e recomenda **uma entre 10 trilhas** de
carreira em TI, exibindo as regras que justificam a decisão.

## Demonstração
[▶️ Assistir à demonstração do projeto (40 segundos)](https://github.com/JoaoP-Melo/Intelligent-Career-Consultant/issues/1#issuecomment-6356689938)

## Trilhas
Back-end · Front-end & UI/UX · Ciência de Dados e ML · Engenharia de Dados · Cibersegurança · DevOps & SRE ·
Computação em Nuvem · Mobile · QA · Gestão de Produtos

## Instalação e execução
Requer Python 3.10+.

```bash
git clone https://github.com/JoaoP-Melo/Intelligent-Career-Consultant
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Como funciona
1. **Entrevista** (9 perguntas): afinidade matemática, atuação diária, linguagem/ferramenta, entrega de valor,
   ambiente, estilo de trabalho, contato com pessoas, nível de programação e objetivo profissional.
2. **Motor de inferência** (encadeamento para frente): o perfil vira um fato `Perfil`; cada uma das 48 regras
   (`R01`–`R48`) que casa declara um fato `Evidencia` com pontos (positivos ou negativos) para uma trilha.
3. **Consolidação**: a regra `R99` (menor *salience*) soma as evidências e declara a `Recomendacao`;
   o desempate usa o número de regras positivas.
4. **Justificativa**: a interface lista as regras que favoreceram a trilha, o ranking completo e, se a
   diferença para a 2ª colocada for ≤ 2 pontos, avisa que o perfil é híbrido.

### Desambiguação (exemplos)
- **Ciência de Dados × Eng. de Dados**: DS exige matemática alta + análise (R14); matemática baixa penaliza DS (R18);
  foco em pipelines com matemática baixa/média favorece DE e penaliza DS (R22).
- **DevOps × Cloud**: automação (R28–R31) × planejamento/arquitetura em nuvem (R32–R35).
- **Mobile × Front-end**: ambiente celular reforça Mobile e penaliza Front-end (R12).

## Estrutura
```
app.py              Interface Streamlit (entrevista, resultado, personas, matriz)
conhecimento.py     Fatos e regras Experta + função diagnosticar()
perguntas.py        Perguntas da entrevista e descrição das trilhas
personas.py         11 personas de teste (cobrem as 10 trilhas)
gerar_matriz.py     Gera docs/matriz_decisao.md a partir das regras
```

## Validação (Fase 4)
11 personas (analítica, infra/segurança, visual/front-end, negócios/produto, entre outras) – todas recebem a
trilha esperada (`pytest -q` e aba "Validação com personas" no app).
