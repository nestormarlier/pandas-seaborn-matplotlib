import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')

# print('Hola')
# print(df.head())

# sns.scatterplot(x='total_bill',y='tip', data=df)
# plt.show()

#Si quiero ver el total de los tickets mas la propina
p={'Female': 'Green', 'Male': 'Red'}
# plt.figure(figsize=(20,5))
# sns.scatterplot(x='total_bill',y='tip', data=df,hue='sex',style='smoker', s=200, alpha=0.5, palette=p)
# plt.xlabel('Importe Ticket')
# plt.ylabel('Propinas')
# plt.title('Restaurante',fontsize=20)
# plt.show()

#Si quiero ver el detalle por dia
# plt.figure(figsize=(20,5))
# g=sns.relplot(x='total_bill',y='tip', data=df,hue='sex',style='smoker', s=200, alpha=0.7, palette=p, kind='scatter', col='day')
# g.fig.suptitle('Gráfico basado en días', fontsize=20, y=1.0)
# g.set(xlabel='Total Ticket', ylabel='Propina')
# plt.show()

#2 graficos por columna
# plt.figure(figsize=(20,5))
# g=sns.relplot(x='total_bill',y='tip', data=df,hue='sex',style='smoker', s=200,
# alpha=0.7, palette=p, kind='scatter', col='day',col_wrap=2,)
# g.fig.suptitle('Gráfico basado en días', fontsize=20, y=1)
# g.set(xlabel='Total Ticket', ylabel='Propina')
# plt.show()

#Matriz de interseccion dia + (almuerzo-cena)
# plt.figure(figsize=(15,5)).show()
# g=sns.relplot(x='total_bill',y='tip', data=df,hue='sex',style='smoker', s=200,
# alpha=0.7, palette=p, kind='scatter', col='day',row='time',)
# g.fig.suptitle('Gráfico basado en días', fontsize=20, y=1)
# g.set(xlabel='Total Ticket', ylabel='Propina')
# plt.show()

#Barras y columnas eje X
# plt.figure(figsize=(20,5))
# sns.countplot(x='day', data=df)
# plt.show()

#Barras y columnas eje Y
# plt.figure(figsize=(20,5))
# sns.countplot(y='day', data=df)
# plt.show()

#Barras y columnas eje Y, agrupando el sexo por dia
# plt.figure(figsize=(20,5))
# sns.countplot(y='day', data=df, hue='sex')
# plt.show()

#Displot Histogramas
plt.figure(figsize=(25,10))
sns.displot(df.total_bill, kde= True, bins=30)
plt.show()
