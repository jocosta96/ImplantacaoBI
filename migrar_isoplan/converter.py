import pandas as pd
from pandas.tseries.offsets import MonthEnd


class Converter:

    def __init__(self):
        self.origem = "EG-FORM-HUM.000435 - Cronograma de Instrumentos e Equipamentos para Calibração"
        self.destino = "Planilha_IsoplanV4.2"
        self.sep = ";"
        self.enc = "ISO-8859-1"
        self.df1 = None
        self.df2 = None
        self.ri = None

    def ler_origem(self):
        df = pd.DataFrame(pd.read_csv(f"c:/{self.origem}.csv", sep=self.sep, encoding=self.enc))
        df = df.sort_values(["Setor", "Cadastro", "Tag", "RI"])
        """RI´s duplicados referem-se ao mesmo instrumento, o que não é aceito no novo BD,
         a exclusão da duplicação não acarretará na perda de informações importantes"""
        df.drop_duplicates(subset=['RI'], inplace=True)
        """Campos com RI e Instrumento em branco referem-se a RI´s reservado para certo instrumento,
         mas que ainda não foi cadastrado"""
        df.dropna(subset=['Instrumento'], inplace=True)
        self.df1 = df
        return self.df1

    def periodo(self):
        periodo_unidade = self.df1["Validade "].str.split(" ")
        periodo = periodo_unidade.str.get(0)
        self.df1["Periodo"] = periodo
        return self.df1

    def proxima(self):
        self.df1['date'] = pd.to_datetime(self.df1['Próxima calibração'], format='%m/%Y', errors="coerce") +\
                           MonthEnd(1)

    def setor(self):
        self.df1['Setor2'] = self.df1['Setor'].map({"AMBULATÓRIO": "DHO",
                                                    "CQ - FÍSICO QUÍMICO": "CQ",
                                                    "CQ - MICROBIOLOGIA": "CQ",
                                                    "DENTISTA": "DHO",
                                                    "EMBALAGEM": "PRODUÇÃO",
                                                    "EQFAR FISICO": "EQFAR",
                                                    "EQFAR MICROBIOLOGIA": "EQFAR",
                                                    "INJETÁVEIS AGENER 3": "PRODUÇÃO",
                                                    "INJETÁVEIS HORMONAL AGENER 1": "PRODUÇÃO",
                                                    "INJETÁVEIS PENICILÂNICOS AGENER 2": "PRODUÇÃO",
                                                    "INJETÁVEIS PÓS": "PRODUÇÃO",
                                                    "LOGISTICA": "LOGISTICA",
                                                    "P&D DA": "P&D DA",
                                                    "PENICILANICOS": "PRODUÇÃO",
                                                    "PESAGEM": "PRODUÇÃO",
                                                    "QUALIFICAÇÃO": "GARANTIA DA QUALIDADE",
                                                    "REFEITÓRIO": "DHO",
                                                    "RESIDUOS": "MEIO AMBIENTE",
                                                    "SEMISSÓLIDOS E LÍQUIDOS": "PRODUÇÃO",
                                                    "SEMISSÓLIDOS HORMONAL": "PRODUÇÃO",
                                                    "SISTEMA DE AR CONDICIONADO": "UTILIDADES",
                                                    "SISTEMA DE ÁGUA LINHA HUMANA": "UTILIDADES",
                                                    "SISTEMA DE ÁGUA LINHA VET": "UTILIDADES",
                                                    "SÓLIDOS": "PRODUÇÃO",
                                                    "SÓLIDOS - UROVIT": "PRODUÇÃO",
                                                    "UTILIDADES": "MANUTENÇÃO",
                                                    "MANUTENÇÃO": "MANUTENÇÃO"},
                                                   na_action=None)
        return self.df1

    def subsetor(self):
        self.df1['Subset'] = self.df1['Setor'].map({"AMBULATÓRIO": "AMBULATÓRIO",
                                                    "CQ - FÍSICO QUÍMICO": "FÍSICO QUÍMICO",
                                                    "CQ - MICROBIOLOGIA": "MICROBIOLÓGICO",
                                                    "DENTISTA": "DENTISTA",
                                                    "EMBALAGEM": "EMBALAGEM",
                                                    "EQFAR FISICO": "FÍSICO QUÍMICO",
                                                    "EQFAR MICROBIOLOGIA": "MICROBIOLOGIA",
                                                    "INJETÁVEIS AGENER 3": "INJETÁVEIS",
                                                    "INJETÁVEIS HORMONAL AGENER 1": "INJETÁVEIS HORMONAIS",
                                                    "INJETÁVEIS PENICILÂNICOS AGENER 2":
                                                        "INJETÁVEIS PENICILÂNICOS",
                                                    "INJETÁVEIS PÓS": "INJETÁVEIS PÓS",
                                                    "LOGISTICA": "LOGISTICA",
                                                    "P&D DA": "P&D DA",
                                                    "PENICILANICOS": "PENICILANICOS",
                                                    "PESAGEM": "PESAGEM",
                                                    "QUALIFICAÇÃO": "QUALIFICAÇÃO",
                                                    "REFEITÓRIO": "REFEITÓRIO",
                                                    "RESIDUOS": "RESÍDUOS",
                                                    "SEMISSÓLIDOS E LÍQUIDOS": "SEMISSÓLIDOS E LÍQUIDOS",
                                                    "SEMISSÓLIDOS HORMONAL": "SEMISSÓLIDOS HORMONAIS",
                                                    "SISTEMA DE AR CONDICIONADO": "SISTEMA DE AR CONDICIONADO",
                                                    "SISTEMA DE ÁGUA LINHA HUMANA": "SISTEMA DE ÁGUA LINHA HUMANA",
                                                    "SISTEMA DE ÁGUA LINHA VET": "SISTEMA DE ÁGUA LINHA VET",
                                                    "SÓLIDOS": "SÓLIDOS",
                                                    "SÓLIDOS - UROVIT": "SÓLIDOS - UROVIT",
                                                    "UTILIDADES": "MANUTENÇÃO UTILIDADES",
                                                    "MANUTENÇÃO": "MANUTENÇÃO INDUSTRIAL"},
                                                   na_action=None)

    def procedimento(self):
        self.df1['Proced'] = self.df1['Setor'].map({"AMBULATÓRIO": "EG-F.0079",
                                                    "CQ - FÍSICO QUÍMICO": "EG-F.0079",
                                                    "CQ - MICROBIOLOGIA": "EG-F.0079",
                                                    "DENTISTA": "EG-F.0079",
                                                    "EMBALAGEM": "EG-F.0079",
                                                    "EQFAR FISICO": "EG-F.0079",
                                                    "EQFAR MICROBIOLOGIA": "EG-F.0079",
                                                    "INJETÁVEIS AGENER 3": "VET-EG-F.0101",
                                                    "INJETÁVEIS HORMONAL AGENER 1": "VET-EG-F.0101",
                                                    "INJETÁVEIS PENICILÂNICOS AGENER 2": "VET-EG-F.0101",
                                                    "INJETÁVEIS PÓS": "EG-F.0079",
                                                    "LOGISTICA": "EG-F.0079",
                                                    "P&D DA": "P&D DA",
                                                    "PENICILANICOS": "VET-EG-F.0101",
                                                    "PESAGEM": "EG-F.0079",
                                                    "QUALIFICAÇÃO": "EG-F.0079",
                                                    "REFEITÓRIO": "EG-F.0079",
                                                    "RESIDUOS": "EG-F.0079",
                                                    "SEMISSÓLIDOS E LÍQUIDOS": "EG-F.0079",
                                                    "SEMISSÓLIDOS HORMONAL": "VET-EG-F.0101",
                                                    "SISTEMA DE AR CONDICIONADO": "EG-F.0079",
                                                    "SISTEMA DE ÁGUA LINHA HUMANA": "EG-F.0079",
                                                    "SISTEMA DE ÁGUA LINHA VET": "VET-EG-F.0101",
                                                    "SÓLIDOS": "EG-F.0079",
                                                    "SÓLIDOS - UROVIT": "VET-EG-F.0101",
                                                    "UTILIDADES": "EG-F.0079",
                                                    "MANUTENÇÃO": "EG-F.0079"},
                                                   na_action=None)

    def ler_destino(self):
        df = pd.DataFrame(pd.read_excel(f"c:/{self.destino}.xls", engine='openpyxl'))
        self.df2 = df
        return self.df2

    def chave(self):
        self.ri = self.df1["RI"]
        self.df2["Número de Registro"] = self.ri
        return self.df2

    def merge(self):
        self.df2["Tipo de Instrumento"] = self.df1["Instrumento"]
        self.df2["Modelo"] = self.df1["Modelo"]
        self.df2["Fabricante"] = self.df1["Fabricante"]
        self.df2["Tag"] = self.df1["Tag"]
        self.df2["Função no Processo"] = self.df1["Função"]
        self.df2["Periodo (meses)"] = self.df1["Periodo"]
        self.df2["Setor"] = self.df1["Setor2"]
        self.df2["Sub-Setor"] = self.df1["Subset"]
        self.df2["Procedimento"] = self.df1["Proced"]
        self.df2["Proxima Calibração"] = self.df1["date"]

        self.df2.set_index(["Número de Registro"], inplace=True)
        return self.df2

    def salva(self):
        arquivo = "Planilha_IsoplanV4.2"
        sep = ";"
        enc = "ISO-8859-1"
        na = "---"
        self.df2.to_csv(f"c:/{arquivo}.1.csv",
                        sep=sep,
                        encoding=enc,
                        na_rep=na)

    def ler_criticidade(self):
        df3 = pd.read_excel("c:\\TABELA_CRITICIDADE.xlsx", engine='openpyxl')
        return df3

    def criticidade(self):
        pass
