from converter import Converter
import pandas as pd



#Data Pipeline
df = Converter()
origem = df.ler_origem()
destino = df.ler_destino()
df.periodo()
df.proxima()
df.chave()
df.setor()
df.subsetor()
df.procedimento()
df3 = df.ler_criticidade()

df2 = df.merge()
df.salva()


#Visualização dos resultados
origem.info()
df3.info()
df2.info()



