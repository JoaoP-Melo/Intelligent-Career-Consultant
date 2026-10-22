import pandas as pd
import streamlit as st

from conhecimento import diagnosticar, listar_regras
from perguntas import QUESTOES, TRILHAS
from personas import PERSONAS

st.set_page_config(page_title="Consultor de Carreiras em TI", page_icon="🧭", layout="wide")

RESP_KEYS = [q["chave"] for q in QUESTOES]


def preencher_persona():
    nome = st.session_state.get("persona_sel")
    for p in PERSONAS:
        if p["nome"] == nome:
            for k, v in p["respostas"].items():
                st.session_state[k] = v


def mostrar_resultado(res):
    info = TRILHAS[res["trilha"]]
    st.success(f"### {info['icone']} Trilha recomendada: {info['nome']}")
    st.write(info["descricao"])

    if res["hibrido"]:
        segunda = TRILHAS[res["ranking"][1][0]]["nome"]
        st.info(f"Seu perfil é híbrido: **{segunda}** ficou muito próxima "
                f"(diferença de {res['margem']} ponto(s)). Vale explorar as duas.")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("Por que essa trilha?")
        for m in res["motivos"]:
            st.markdown(f"- **{m['regra']}** (+{m['pontos']}): {m['motivo']}")
        contra = [e for e in res["evidencias"] if e["trilha"] == res["trilha"] and e["pontos"] < 0]
        for e in contra:
            st.markdown(f"- ⚠️ **{e['regra']}** ({e['pontos']}): {e['motivo']}")
    with col2:
        st.subheader("Ranking das trilhas")
        df = pd.DataFrame(
            [(TRILHAS[t]["nome"], p) for t, p in res["ranking"]], columns=["Trilha", "Pontos"]
        ).set_index("Trilha")
        st.bar_chart(df)

    with st.expander("Todas as regras disparadas"):
        st.dataframe(
            pd.DataFrame([{"Regra": e["regra"], "Trilha": TRILHAS[e["trilha"]]["nome"],
                           "Pontos": e["pontos"], "Motivo": e["motivo"]} for e in res["evidencias"]]),
            hide_index=True)


tab1, tab2, tab3 = st.tabs(["🧭 Consultor", "🧪 Validação com personas", "📋 Matriz de decisão"])

with tab1:
    st.title("🧭 Consultor Inteligente de Carreiras em TI")
    st.caption("Sistema especialista baseado em regras (Experta) – responda à entrevista e receba uma "
               "recomendação justificada entre 10 trilhas.")

    with st.sidebar:
        st.header("Modo demonstração")
        st.selectbox("Persona de teste", [p["nome"] for p in PERSONAS], key="persona_sel")
        st.button("Preencher com persona", on_click=preencher_persona)

    with st.form("entrevista"):
        cols = st.columns(2)
        for i, q in enumerate(QUESTOES):
            with cols[i % 2]:
                st.radio(q["titulo"], list(q["opcoes"]), format_func=q["opcoes"].get,
                         index=None, key=q["chave"])
        enviado = st.form_submit_button("Descobrir minha trilha", type="primary")

    if enviado:
        respostas = {k: st.session_state.get(k) for k in RESP_KEYS}
        faltando = [q["titulo"] for q in QUESTOES if not respostas[q["chave"]]]
        if faltando:
            st.warning("Responda todas as perguntas. Faltam: " + "; ".join(faltando))
        else:
            mostrar_resultado(diagnosticar(respostas))

with tab2:
    st.subheader("Validação com personas de teste")
    linhas = []
    for p in PERSONAS:
        r = diagnosticar(p["respostas"])
        linhas.append({"Persona": p["nome"], "Perfil": p["descricao"],
                       "Esperada": TRILHAS[p["esperada"]]["nome"],
                       "Recomendada": TRILHAS[r["trilha"]]["nome"],
                       "Resultado": "✅" if r["trilha"] == p["esperada"] else "❌"})
    df = pd.DataFrame(linhas)
    st.metric("Acertos", f"{(df['Resultado'] == '✅').sum()} / {len(df)}")
    st.dataframe(df, hide_index=True)

with tab3:
    st.subheader("Matriz de decisão: regras da base de conhecimento")
    st.dataframe(pd.DataFrame(listar_regras(), columns=["Regra", "Efeito (pontos)", "Condição"]),
                 hide_index=True)
