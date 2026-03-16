import pandas as pd
import matplotlib.pyplot as plt

carregar_dados = pd.read_csv('dataset_ciencia_dados.csv')

print(carregar_dados.head())

#histograma histogrma básico
plt.hist(carregar_dados["nota_estatistica"])

plt.title("Histograma das Notas de Estatística")
plt.xlabel("Nota")
plt.ylabel("Frequência")

plt.show()

#Histograma melhor (mais usado em ciência de dados)
plt.hist(
#Aqui definimos intervalos (bins) e aparência melhor.
    carregar_dados["nota_estatistica"],
    bins=15 #dividir o intervalo total dos dados em 15 faixas iguais e contar quantos dados caem em cada
)

plt.title("Hitograma das Notas de Estatística")
plt.xlabel("Notas")
plt.ylabel("Quantidade")

plt.show()

#Histograma mais profissional
plt.hist(
    carregar_dados["nota_estatistica"],
    bins=20,
    edgecolor="black"
)

plt.title("Histigrama das Notas de Estatística")
plt.xlabel("Notas")
plt.ylabel("Frequência")

plt.show()

#histograma de outra variavel
plt.hist(
    carregar_dados["idade"],
    bins=20,
    edgecolor="black"
)

plt.title("Histograma das idades")
plt.xlabel("Idade")
plt.ylabel("Frequência")

plt.show()

#Histograma comparando duas variavei
plt.hist(
    carregar_dados["horas_estudo"],
    bins=20,
    alpha=0.6, #Controla a transparência da cor das barras do gráfico. O valor vai de 0.0 (totalmente invisível/transparente) até 1.0 (cor sólida).
    edgecolor="black"
)
plt.hist(
    carregar_dados["sono"],
    bins=20,
    alpha=0.6, #Controla a transparência da cor das barras do gráfico. O valor vai de 0.0 (totalmente invisível/transparente) até 1.0 (cor sólida).
    edgecolor="red"
)

plt.legend()
plt.title("Comparação entre Horas de Estudos VS Sono")

plt.show()