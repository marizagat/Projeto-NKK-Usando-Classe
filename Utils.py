#arquivo com funções genéricas que auxiliam nos cálculos

#retorna a distância entre 2 pontos considerando n dimensões
#ou seja: pode haver qualquer quantidade de carteiras
#porém todos os clientes devem ter a mesma quantidade de carteiras, para este cálculo
#mas é claro que não há problema se o valor de algumas delas for igual a zero
def calcular_distancia_2_pontos(ponto1, ponto2):
    distancia_euclidiana = 0
    for i in range(len(ponto1)):
        distancia_euclidiana += (ponto1[i] - ponto2[i]) ** 2
    distancia_euclidiana = distancia_euclidiana ** 0.5
    return distancia_euclidiana