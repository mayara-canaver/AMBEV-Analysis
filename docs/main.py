import pandas as pd
import yfinance as yf
import seaborn as sns

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima.model import ARIMA

acao_ambev = yf.Ticker("ABEV3.SA")

data_ambev = acao_ambev.history(start="2011-01-01", end="2021-01-01", interval="1d")

data_ambev.reset_index(level=0, inplace=True)

data_ambev.columns = [x.upper() for x in data_ambev.columns]

data_ambev = data_ambev.dropna()

sns.lineplot(data=data_ambev, x="DATE", y="OPEN")

# Temos que as ações da Ambev tem a tendência de crescimento, com algumas estabilizações em alguns meses de alguns anos, como por exemplo de 2013 a 2015, onde teve uma forte estabilização
# das ações. Há uma queda grotesca no início de 2020, o que pode ser indicado por alguns motivos, como por exemplo o início da pandemia do COVID-19, o que impactou em paradas de eventos
# pessoas em bares e restaurantes, assim diminuindo o consumo de bebidas alcoolicas no geral.
# Também vemos que após alguns meses ao acontecimento do COVID, a tendência novamente é se manter crescente o valor das ações da empresa, pois temos a reabertura de eventos e festas.

data_ambev.columns

plot_acf(data_ambev["DATE"])

