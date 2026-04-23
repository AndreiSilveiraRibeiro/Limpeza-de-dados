# Projeto de Saneamento de Dados:

## StreamFlix

#### 1. **Objetivo do Projeto**:
Este projeto tem como finalidade realizar o saneamento e a análise de dados de uma
plataforma de streaming (StreamFlix). O foco principal é a identificação de comportamentos
atípicos e a limpeza de inconsistências para garantir que as métricas de engajamento reflitam a
realidade dos usuários.

#### 2. **Etapas de Saneamento**:

O processo de limpeza foi estruturado para tratar diferentes tipos de ruídos nos dados:
● Padronização de Texto: Ajuste das categorias de planos (Básico e Premium) para evitar
duplicidade causada por diferenças de caixa (maiúsculas/minúsculas).
● Tratamento de Datas: Conversão de múltiplos formatos de data para o padrão datetime
do Pandas.
● Saneamento de Negativos: Identificação e tratamento de valores impossíveis (como
minutos assistidos negativos) utilizando a função .mask().

#### 3. **Análise de Outliers**:
Para este projeto, utilizamos técnicas estatísticas avançadas para isolar anomalias que
distorcem os resultados globais:
Z-Score
Utilizado para identificar desvios padrão em relação à média. É ideal para detectar anomalias
extremas em grandes volumes de dados onde a distribuição é aproximadamente normal.

**Z-Score:** Ideal para grandes volumes de dados com distribuição normal.

```python
from scipy import stats
import numpy as np
z_scores = np.abs(stats.zscore(df['Minutos_Assistidos']))
df_limpo = df[z_scores < 3]
```

IQR (Interquartile Range): Abordagem robusta baseada em quartis (Q1 e Q3), ideal para dados com valores extremos.

```Python
Q1 = df['Minutos_Assistidos'].quantile(0.25)
Q3 = df['Minutos_Assistidos'].quantile(0.75)
IQR = Q3 - Q1
limite_superior = Q3 + 1.5 * IQR
df_limpo_iqr = df[df['Minutos_Assistidos'] <= limite_superior]
```

#### 4. **Tecnologias Utilizadas**:
##### **Tecnologia Finalidade**:

- **Python Linguagem principal do projeto.**
- **Pandas Manipulação e limpeza de DataFrames.**
- **NumPy Operações matemáticas e tratamento de nulos (NaN).**
- **SciPy Cálculos estatísticos para Z-Score.**

#### 5. **Conclusão e Insights**:
A aplicação dessas técnicas permite diferenciar um erro de sistema (bug) ou uma possível
fraude (Cybersecurity) de um comportamento de usuário real de alto engajamento (Heavy
User). A limpeza correta garante que decisões de negócio sejam tomadas sobre bases sólidas,
evitando que métricas como o tempo médio de visualização sejam infladas artificialmente.