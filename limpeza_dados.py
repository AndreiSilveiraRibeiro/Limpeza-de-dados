import pandas as pd
import numpy as np

#Usei essa configuração por precaução dos dados serem longos e terem muitos dados
pd.set_option("display.width", None)
leitura = pd.read_csv("projeto_limpeza.csv")

#Serve para analisar quantas colunas e linhas tem. Usei para ter uma base de quantos dados tenho no começo para ver quando dados foram tirados e se ouve problemas
print(leitura.shape)
print(leitura)

#Padronizei as colunas que contem palavras para todas terem a primeira palavra em maiusculo
leitura['Nome_Cliente'] = leitura['Nome_Cliente'].str.title()
leitura['Categoria'] = leitura['Categoria'].str.title()
print(leitura['Nome_Cliente'])

#Coloquei a coluna 'data_venda' a partir de agora ter o tipo dela como 'datetime'
leitura['Data_Venda'] = pd.to_datetime(leitura['Data_Venda'], dayfirst=True, errors="coerce")
print(leitura['Data_Venda'])

#fiz uma simples analise aonde, se o valores da coluna "valor_Venda" forem negativas, automaticamente ficarem como nulas ou melhor NaN
leitura['Valor_Venda'] = leitura['Valor_Venda'].mask(leitura['Valor_Venda'] < 0, np.nan)
print(leitura['Valor_Venda'])

#Analisei se tem algum valor nulo, duplicados. Se tivesse limpei
print(leitura.isnull().sum())
print(leitura['Data_Venda'])
leitura = leitura.dropna(subset=['Valor_Venda'])
leitura.drop_duplicates(inplace=True)
print(leitura.isnull().sum())

#Ultima analise, se nao tivesse perdido mais dados que o normal estaria tudo certo
print(leitura.describe())
print(leitura.shape)
print(leitura)

#Salvei o novo DataFrame
leitura.to_csv('projeto_limpeza_limpo.csv', index=False)
print("Salvo com sucesso!")