import pandas as pd

carregar_dados = pd.read_csv('dataset_ciencia_dados.csv')

print(carregar_dados.head())

#Gráfico ramo e fola (Stem and leaf)
dados = carregar_dados["nota_estatistica"]

#ordenar os valore
stem_leaf = {} #inicialização vazia do dicionário
# Exemplo: organizar os números 12, 15, 23
# stem_leaf = {1: [2, 5], 2: [3]}

for valor in dados:
    stem = int(valor)               #parte interira
    leaf = int((valor - stem) * 10)   #Parte decimal Exemplo: (15.7 - 15) * 10 = 0.7 * 10 = 7.0. O int() converte para 7. Isso é a "folha".

    if stem not in stem_leaf:
        stem_leaf[stem] = []  # Verifica se o stem (ex: 15) já existe como chave no dicionário stem_leaf. Se não existir, cria a chave e associa uma lista vazia ([]) a ela
    
    stem_leaf[stem].append(leaf) #.append é usado para adicionar um elemento no final de uma lista
    #Adiciona a leaf atual à lista correspondente à sua raiz no dicionário.

print("\nGráfico Ramo e folha:\n")

for stem in stem_leaf:
    folhas = " ".join(map(str, stem_leaf[stem])) 
    #" ".join(...): Une essas strings de folhas separando-as por um espaço
    #map(str, ...): Converte todos os números das folhas (que estão como int) em strings.
    print(f"{stem} | {folhas}")