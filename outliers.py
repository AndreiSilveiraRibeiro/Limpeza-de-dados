import pandas as pd
import numpy as np

#Usei essa configuração por precaução dos dados serem longos e terem muitos dados
pd.set_option('display.width', None)
leitura = pd.read_csv('projeto_limpeza_limpo.csv')

#Usei para analisar se tem outliers
print(leitura.describe())
print(leitura)

#Defini a porcetagem baixa e alta e o IQR
Q1 = leitura['Valor_Venda'].quantile(0.25)
Q3 = leitura['Valor_Venda'].quantile(0.75)
IQR = Q3 - Q1

#Defini o limite superior e inferior
limite_superior = Q3 + (1.5 * IQR)
limite_inferior = Q1 - (1.5 * IQR)

#Analise de quantas outliers tem e se sobro alguma
print(f"Quantidade de outliers identificados: {len(leitura[leitura['Valor_Venda'] > limite_superior])}")
leitura_limpa = leitura[leitura['Valor_Venda'] <= limite_superior]
print(leitura_limpa.describe())

#Por falta de Informação nao da para saber ao certo oque foi esse outliers, se é erro de digitação, bug do sistema ou alguma tentativa de hacker
print(f"Quantidade de outliers identificados: {leitura[leitura['Valor_Venda'] > limite_superior]}")

leitura_limpa.to_csv('projeto_finalizado_sem_outliers.csv', index=False)
print("Salvo com sucesso!")