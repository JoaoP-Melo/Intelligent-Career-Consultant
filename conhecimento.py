import collections
import collections.abc


for _nome in ("Mapping", "MutableMapping", "Sequence", "Iterable", "Callable"):
    if not hasattr(collections, _nome):
        setattr(collections, _nome, getattr(collections.abc, _nome))

from experta import Fact, KnowledgeEngine, P, Rule  
from perguntas import TRILHAS  


def em(*valores):
    """Padrão Experta: o valor do campo pertence ao conjunto informado."""
    return P(lambda x: x in valores)


class Perfil(Fact):
    """Respostas da entrevista (um campo por pergunta)."""


class Evidencia(Fact):
    """Pontos atribuídos a uma trilha por uma regra disparada."""


class Recomendacao(Fact):
    """Conclusão final do sistema."""


class ConsultorCarreira(KnowledgeEngine):
    def _ev(self, regra, trilha, pontos, motivo):
        self.declare(Evidencia(regra=regra, trilha=trilha, pontos=pontos, motivo=motivo))

    @Rule(Perfil(atuacao="algoritmos"))
    def r01(self):
        """R01 | Back-end +4 | Prefere escrever algoritmos e regras de negócio"""
        self._ev("R01", "backend", 4, "Você prefere escrever algoritmos e regras de negócio.")

    @Rule(Perfil(entrega="regras_servidor"))
    def r02(self):
        """R02 | Back-end +3 | Valoriza a lógica que roda por trás do sistema"""
        self._ev("R02", "backend", 3, "Você valoriza a lógica que sustenta o sistema por trás dos panos.")

    @Rule(Perfil(atuacao="algoritmos", ferramenta=em("java_csharp_go", "sql")))
    def r03(self):
        """R03 | Back-end +3 | Algoritmos + Java/C#/Go/PHP ou SQL"""
        self._ev("R03", "backend", 3, "Sua afinidade com linguagens de servidor/SQL combina com lógica de negócio.")

    @Rule(Perfil(plataforma="servidores", programacao=em("intermediario", "avancado")))
    def r04(self):
        """R04 | Back-end +2 | Atua em servidores/APIs + programação intermediária ou avançada"""
        self._ev("R04", "backend", 2, "Você quer atuar em servidores/APIs e já programa com segurança.")

    @Rule(Perfil(atuacao="layouts"))
    def r05(self):
        """R05 | Front-end +4 | Prefere criar layouts e interfaces visuais"""
        self._ev("R05", "frontend", 4, "Você prefere criar layouts e interfaces visuais.")

    @Rule(Perfil(entrega="produto_usuario", plataforma="web"))
    def r06(self):
        """R06 | Front-end +3 | Entrega ao usuário final + ambiente web"""
        self._ev("R06", "frontend", 3, "Você quer entregar o produto que o usuário vê, na web.")

    @Rule(Perfil(ferramenta="javascript", estilo="criativo"))
    def r07(self):
        """R07 | Front-end +3 | JavaScript + estilo criativo"""
        self._ev("R07", "frontend", 3, "JavaScript aliado a um perfil criativo é a base de interfaces reativas.")

    @Rule(Perfil(atuacao="layouts", estilo="criativo"))
    def r08(self):
        """R08 | Front-end +2 | Layouts + estilo criativo (UX/UI)"""
        self._ev("R08", "frontend", 2, "Seu lado criativo favorece o trabalho de UX/UI.")

    @Rule(Perfil(atuacao="apps_celular"))
    def r09(self):
        """R09 | Mobile +5 | Prefere construir aplicativos para celular"""
        self._ev("R09", "mobile", 5, "Você quer construir aplicativos para celular.")

    @Rule(Perfil(plataforma="celular"))
    def r10(self):
        """R10 | Mobile +3 | Ambiente preferido: celulares e tablets"""
        self._ev("R10", "mobile", 3, "Seu ambiente preferido são dispositivos móveis.")

    @Rule(Perfil(ferramenta="dart_kotlin_swift"))
    def r11(self):
        """R11 | Mobile +3 | Afinidade com Dart/Kotlin/Swift"""
        self._ev("R11", "mobile", 3, "Dart, Kotlin e Swift são as linguagens do ecossistema mobile.")

    @Rule(Perfil(entrega="produto_usuario", plataforma="celular"))
    def r12(self):
        """R12 | Mobile +2 / Front-end −1 | Entrega ao usuário final + celular (desempata Mobile × Front-end)"""
        self._ev("R12", "mobile", 2, "Entregar produto ao usuário em dispositivos móveis aponta para Mobile.")
        self._ev("R12", "frontend", -1, "O foco em celular afasta do front-end web puro.")

    @Rule(Perfil(ferramenta="javascript", plataforma="celular"))
    def r13(self):
        """R13 | Mobile +2 | JavaScript + celular (React Native)"""
        self._ev("R13", "mobile", 2, "JavaScript + celular abre caminho para React Native.")

    @Rule(Perfil(atuacao="analisar_dados", matematica="alta"))
    def r14(self):
        """R14 | Ciência de Dados +5 | Analisar dados + alta afinidade com matemática"""
        self._ev("R14", "ds", 5, "Você gosta de analisar dados e tem alta afinidade com matemática/estatística.")

    @Rule(Perfil(atuacao="analisar_dados", ferramenta="python", matematica=em("media", "alta")))
    def r15(self):
        """R15 | Ciência de Dados +2 | Analisar dados + Python + matemática média/alta"""
        self._ev("R15", "ds", 2, "Python é a principal ferramenta de modelagem e análise de dados.")

    @Rule(Perfil(entrega="insights"))
    def r16(self):
        """R16 | Ciência de Dados +3 | Valoriza decisões e previsões baseadas em dados"""
        self._ev("R16", "ds", 3, "Você se motiva com decisões e previsões baseadas em dados.")

    @Rule(Perfil(objetivo="pesquisa_ia"))
    def r17(self):
        """R17 | Ciência de Dados +3 | Objetivo: pesquisa e inteligência artificial"""
        self._ev("R17", "ds", 3, "Seu objetivo é trabalhar com pesquisa e inteligência artificial.")

    @Rule(Perfil(matematica="baixa"))
    def r18(self):
        """R18 | Ciência de Dados −3 | Baixa afinidade com matemática"""
        self._ev("R18", "ds", -3, "Ciência de Dados exige base sólida de estatística, e sua afinidade é baixa.")

    @Rule(Perfil(atuacao="pipelines_dados"))
    def r19(self):
        """R19 | Engenharia de Dados +5 | Prefere montar pipelines de coleta, limpeza e armazenamento"""
        self._ev("R19", "de", 5, "Você prefere construir fluxos que coletam, limpam e armazenam dados.")

    @Rule(Perfil(atuacao="pipelines_dados", plataforma="dados", ferramenta=em("sql", "python")))
    def r20(self):
        """R20 | Engenharia de Dados +3 | Pipelines + plataformas de dados + SQL/Python"""
        self._ev("R20", "de", 3, "SQL/Python em plataformas de dados é o dia a dia de um engenheiro de dados.")

    @Rule(Perfil(entrega="dados_confiaveis"))
    def r21(self):
        """R21 | Engenharia de Dados +4 | Valoriza dados organizados e confiáveis para os outros"""
        self._ev("R21", "de", 4, "Você valoriza entregar dados organizados e confiáveis para outras pessoas.")

    @Rule(Perfil(atuacao="pipelines_dados", matematica=em("baixa", "media")))
    def r22(self):
        """R22 | Eng. de Dados +2 / Ciência de Dados −1 | Pipelines + matemática baixa/média (desempata DE × DS)"""
        self._ev("R22", "de", 2, "O foco em infraestrutura de dados exige menos estatística avançada.")
        self._ev("R22", "ds", -1, "Foco em pipelines (e não em modelagem) afasta de Ciência de Dados.")

    @Rule(Perfil(atuacao="analisar_dados", matematica=em("baixa", "media"), ferramenta="sql"))
    def r23(self):
        """R23 | Eng. de Dados +2 | Analisar dados + SQL + matemática baixa/média (perfil de dados sem foco em modelagem)"""
        self._ev("R23", "de", 2, "SQL com estatística moderada aproxima você da engenharia/analítica de dados.")

    @Rule(Perfil(atuacao="seguranca"))
    def r24(self):
        """R24 | Cibersegurança +5 | Prefere procurar falhas e proteger sistemas"""
        self._ev("R24", "seguranca", 5, "Você quer procurar falhas e proteger sistemas contra invasões.")

    @Rule(Perfil(entrega="seguranca"))
    def r25(self):
        """R25 | Cibersegurança +4 | Valoriza a segurança contra invasões"""
        self._ev("R25", "seguranca", 4, "A segurança contra invasões é a entrega de valor que mais te motiva.")

    @Rule(Perfil(estilo="investigativo"))
    def r26(self):
        """R26 | Cibersegurança +2 | Estilo investigativo (mentalidade de atacante)"""
        self._ev("R26", "seguranca", 2, "Curiosidade em ver como as coisas falham é a mentalidade de um pentester.")

    @Rule(Perfil(atuacao="seguranca", ferramenta="linux_redes"))
    def r27(self):
        """R27 | Cibersegurança +3 | Segurança + Linux/Redes"""
        self._ev("R27", "seguranca", 3, "Conhecimento de Linux e redes é base para segurança ofensiva e defensiva.")

    @Rule(Perfil(atuacao="automatizar"))
    def r28(self):
        """R28 | DevOps +5 | Prefere automatizar build, deploy e operação"""
        self._ev("R28", "devops", 5, "Você prefere automatizar processos de build, deploy e operação.")

    @Rule(Perfil(estilo="automatizador"))
    def r29(self):
        """R29 | DevOps +3 | Estilo automatizador"""
        self._ev("R29", "devops", 3, "Aversão a tarefas repetitivas é a essência de DevOps/SRE.")

    @Rule(Perfil(atuacao="automatizar", ferramenta="linux_redes"))
    def r30(self):
        """R30 | DevOps +3 | Automatizar + Linux/Redes/Shell"""
        self._ev("R30", "devops", 3, "Shell script e Linux são a base de pipelines CI/CD e contêineres.")

    @Rule(Perfil(atuacao="automatizar", entrega="infra"))
    def r31(self):
        """R31 | DevOps +2 / Nuvem −1 | Automatizar + infraestrutura (desempata DevOps × Cloud)"""
        self._ev("R31", "devops", 2, "Automatizar a infraestrutura que sustenta o sistema é DevOps/SRE.")
        self._ev("R31", "cloud", -1, "O foco em automação (e não em desenho de arquitetura) afasta de Cloud.")

    @Rule(Perfil(atuacao="infra_cloud"))
    def r32(self):
        """R32 | Nuvem +5 | Prefere planejar e migrar infraestrutura para a nuvem"""
        self._ev("R32", "cloud", 5, "Você quer planejar e migrar infraestruturas para a nuvem.")

    @Rule(Perfil(plataforma="nuvem"))
    def r33(self):
        """R33 | Nuvem +3 | Ambiente preferido: nuvem"""
        self._ev("R33", "cloud", 3, "Seu ambiente preferido é a nuvem (AWS/Azure/GCP).")

    @Rule(Perfil(objetivo="arquiteto", atuacao=em("infra_cloud", "automatizar")))
    def r34(self):
        """R34 | Nuvem +3 | Objetivo de arquiteto + infraestrutura/automação"""
        self._ev("R34", "cloud", 3, "Seu objetivo de desenhar soluções de grande escala favorece Arquitetura Cloud.")

    @Rule(Perfil(atuacao="infra_cloud", entrega="infra"))
    def r35(self):
        """R35 | Nuvem +2 | Infra em nuvem + valoriza a infraestrutura que sustenta o sistema"""
        self._ev("R35", "cloud", 2, "Você valoriza a infraestrutura que sustenta o sistema.")

    @Rule(Perfil(entrega="infra", atuacao=em("algoritmos", "layouts", "apps_celular", "analisar_dados",
                                              "pipelines_dados", "seguranca", "testar", "produto")))
    def r36(self):
        """R36 | Nuvem +1 / DevOps +1 | Valoriza infraestrutura mesmo sem atuação principal nela"""
        self._ev("R36", "cloud", 1, "Você valoriza infraestrutura, o que aponta para áreas de nuvem.")
        self._ev("R36", "devops", 1, "Você valoriza infraestrutura, o que aponta para DevOps.")

    @Rule(Perfil(atuacao="testar"))
    def r37(self):
        """R37 | QA +5 | Prefere testar software e garantir qualidade"""
        self._ev("R37", "qa", 5, "Você prefere testar software e garantir que ele funcione bem.")

    @Rule(Perfil(entrega="qualidade"))
    def r38(self):
        """R38 | QA +4 | Valoriza confiabilidade e qualidade do software"""
        self._ev("R38", "qa", 4, "Confiabilidade e qualidade do software são o que mais te motiva.")

    @Rule(Perfil(estilo="meticuloso"))
    def r39(self):
        """R39 | QA +3 | Estilo detalhista"""
        self._ev("R39", "qa", 3, "Perceber erros que ninguém viu é a principal virtude de quem trabalha com QA.")

    @Rule(Perfil(atuacao="testar", programacao=em("basico", "intermediario", "avancado")))
    def r40(self):
        """R40 | QA +1 | Testar + alguma base de programação (automação de testes)"""
        self._ev("R40", "qa", 1, "Alguma base de programação permite automatizar testes.")

    @Rule(Perfil(atuacao="produto"))
    def r41(self):
        """R41 | Produto +5 | Prefere decidir o que construir, equilibrando negócio, design e tecnologia"""
        self._ev("R41", "pm", 5, "Você quer decidir o que será construído, equilibrando negócio, design e tecnologia.")

    @Rule(Perfil(entrega="estrategia"))
    def r42(self):
        """R42 | Produto +4 | Valoriza o valor de negócio e o sucesso do produto"""
        self._ev("R42", "pm", 4, "O sucesso do produto no mercado é o que mais te motiva.")

    @Rule(Perfil(objetivo="lider_negocio"))
    def r43(self):
        """R43 | Produto +3 | Objetivo: liderar produtos e decisões de negócio"""
        self._ev("R43", "pm", 3, "Seu objetivo é liderar produtos e decisões de negócio.")

    @Rule(Perfil(pessoas="alta", estilo="organizador"))
    def r44(self):
        """R44 | Produto +3 | Muito contato com pessoas + estilo organizador/comunicativo"""
        self._ev("R44", "pm", 3, "Comunicação e organização são competências centrais de Product Management.")

    @Rule(Perfil(pessoas="baixa"))
    def r45(self):
        """R45 | Produto −3 | Prefere pouco contato com pessoas"""
        self._ev("R45", "pm", -3, "Gestão de produto exige alinhamento constante com pessoas.")

    @Rule(Perfil(programacao="nenhuma"))
    def r46(self):
        """R46 | Back-end −3 / Mobile −2 / Eng. de Dados −2 / Ciência de Dados −2 / DevOps −2 | Nenhuma experiência com programação"""
        for t, p in (("backend", -3), ("mobile", -2), ("de", -2), ("ds", -2), ("devops", -2)):
            self._ev("R46", t, p, "Esta trilha exige programação e você ainda não começou a programar.")

    @Rule(Perfil(ferramenta="nenhuma", programacao=em("nenhuma", "basico")))
    def r47(self):
        """R47 | QA +1 / Produto +1 / Front-end +1 | Iniciante sem ferramenta definida (trilhas de entrada mais suave)"""
        for t in ("qa", "pm", "frontend"):
            self._ev("R47", t, 1, "Trilha com porta de entrada mais acessível para iniciantes.")

    @Rule(Perfil(pessoas="alta", programacao=em("intermediario", "avancado"), objetivo="lider_negocio"))
    def r48(self):
        """R48 | Produto +2 | Perfil técnico + muito contato com pessoas + objetivo de liderança (PM técnico)"""
        self._ev("R48", "pm", 2, "Perfil técnico que lidera é muito valorizado em Product Management.")

    @Rule(Perfil(), salience=-100)
    def r99(self):
        """R99 | Todas | Consolida as evidências e emite a recomendação (menor prioridade)"""
        totais = {t: 0 for t in TRILHAS}
        n_regras = {t: 0 for t in TRILHAS}
        for f in self.facts.values():
            if isinstance(f, Evidencia):
                totais[f["trilha"]] += f["pontos"]
                if f["pontos"] > 0:
                    n_regras[f["trilha"]] += 1
        ranking = sorted(totais, key=lambda t: (-totais[t], -n_regras[t]))
        self.declare(Recomendacao(trilha=ranking[0], pontos=totais[ranking[0]]))
        self.ranking = [(t, totais[t]) for t in ranking]


def diagnosticar(respostas: dict) -> dict:
    """Executa o motor de inferência para um conjunto de respostas."""
    engine = ConsultorCarreira()
    engine.reset()
    engine.declare(Perfil(**respostas))
    engine.run()

    evidencias = sorted(
        (dict(f) for f in engine.facts.values() if isinstance(f, Evidencia)),
        key=lambda e: (e["regra"], e["trilha"]),
    )
    ranking = engine.ranking
    recomendada = ranking[0][0]
    margem = ranking[0][1] - ranking[1][1]
    return {
        "trilha": recomendada,
        "ranking": ranking,
        "evidencias": evidencias,
        "margem": margem,
        "hibrido": margem <= 2,
        "motivos": [e for e in evidencias if e["trilha"] == recomendada and e["pontos"] > 0],
    }


def listar_regras():
    """Retorna [(id, efeito, condição)] a partir dos docstrings das regras."""
    linhas = []
    for regra in ConsultorCarreira().get_rules():
        doc = getattr(regra, "_wrapped", regra).__doc__ or ""
        partes = [p.strip() for p in doc.split("|")]
        if len(partes) == 3:
            linhas.append(tuple(partes))
    return sorted(linhas)
