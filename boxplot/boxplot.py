import pandas as pd
import matplotlib.pyplot as plt

carregar_dados = pd.read_csv('dataset_ciencia_dados.csv')

print(carregar_dados.head())

#Boxplot simples
plt.boxplot(carregar_dados["nota_estatistica"])

plt.title("Boxplot da Nota de Estatística")
plt.ylabel("Nota")

plt.show()

#Boxplot comparando duas variavel
plt.boxplot([
    carregar_dados["nota_estatistica"],
    carregar_dados["nota_python"]
])

plt.xticks([1,2], ["Estatística", "Python"]) #substitui os valores numéricos no eixo X padrão por rótulos personalizados nos locais especificados

plt.title("Comparação das notas")
plt.ylabel("Nota")

plt.show()  

#Boxplot comparando Três variavel
plt.boxplot([
    carregar_dados["idade"],
    carregar_dados["horas_estudo"],
    carregar_dados["sono"]
])

plt.xticks([1,2,3], ["Idade", "HOras de Estudos", "Horas de sono"])

plt.title("Comparação, idade, Hestudos, Hsono")
plt.ylabel("Dados")

plt.show()

#Boxplt mais profissional
plt.figure(figsize=(8,5))

plt.boxplot(
    carregar_dados["horas_estudo"],
    patch_artist=True # preencher caixas com cor por padral (line2D)
)

plt.title("Distribuição das Horas de Estudos")
plt.ylabel("Horas")

plt.show()

#boxplot mais profissional com duas variaveis
plt.figure(figsize=(8, 5))

plt.boxplot([
    carregar_dados["horas_estudo"],
    carregar_dados["sono"],
],
patch_artist=True
)

plt.xticks([1,2], ["Horas de estudos", "Horas de Sono"])

plt.title("Horas de estudos VS Horas de Sono")
plt.ylabel("Horas")

plt.show()

#Boxplot Dentado (notched Boxplot)
plt.boxplot([
    carregar_dados["nota_estatistica"],
    carregar_dados["nota_python"]
],
notch=True,  #entalhe
patch_artist=True
)

plt.xticks([1,2], ["Notas de Estatística", "Notas de Python"])

plt.title("Boxplot dentado Estatística VS Python")
plt.ylabel("Notas")

plt.grid()
plt.show()

#Boxplot dentado (notched Bocplot) recomendado
plt.figure(figsize=(8,5))

plt.boxplot([
    carregar_dados["nota_estatistica"],
    carregar_dados["nota_python"]
],
patch_artist=True,
notch=True
)

plt.xticks([1,2], ["Notas de Estatística", "Notas de Python"])
plt.ylabel("NOtas")

plt.grid()
plt.show()