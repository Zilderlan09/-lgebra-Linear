import numpy as np

def gauss(A, B):

    n = len(A)  # Tamanho da matriz A
    A = np.array(A, dtype=np.float64)  # Converte A para um array de floats
    B = np.array(B, dtype=np.float64)  # Converte B para um array de floats

    A = np.hstack([A, B.reshape(-1, 1)])  # Cria a matriz estendida A|B

    for i in range(n):
        p = np.argmax(np.abs(A[i:, i])) + i  # Seleciona o maior pivot
        if A[p, i] == 0:
            raise Exception("Sistema singular ou indefinido.")  # Caso o sistema seja singular

        if p != i:
            A[[i, p]] = A[[p, i]]  # Troca as linhas da matriz

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]  # Calcula o fator de eliminação
            A[j, i:] -= factor * A[i, i:]  # Atualiza as linhas da matriz

    # Substituição Reversa
    X = np.zeros(n)  # Vetor solução inicializado com zeros
    for i in range(n - 1, -1, -1):
        X[i] = (A[i, -1] - np.sum(A[i, i + 1:n] * X[i + 1:])) / A[i, i]  # Calcula a solução

    return X

def combinacao(vetores, vetor_alvo):

    n = len(vetor_alvo)  # Obtém o tamanho do vetor alvo
    A = np.array(vetores)  # Matriz composta pelos vetores fornecidos
    B = np.array(vetor_alvo)  # Vetor alvo
    # A função tentará resolver o sistema pelo método de eliminação gaussiana
    # Se houver solução, determina-se que o vetor alvo é uma combinação linear

    try:
        # Tentar resolver o sistema usando a função gauss
        coef = gauss(A, B)
        resultado = True  # Se o sistema foi resolvido, há combinação linear
    except Exception as e:
        # Caso contrário, não há combinação linear
        resultado = False
        coef = None

    return resultado, coef


print('Caso 1')
vetores = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])  # Vetores de base padrão
vetor_alvo = np.array([1, 2, 3])  # Vetor alvo a ser testado

resultado, coef = combinacao(vetores, vetor_alvo)

if resultado:
    print(coef)
else:
    print("Não é combinação linear")

print('Caso 2')
vetores = np.array([[3.5, 2.1, 2, 4], [5.25, 3.15, 3.0, 6.0], [4.2, 2.52, 2.4, 4.8], [-4.9, -2.94, -2.8, -5.6]])  # Vetores
vetor_alvo = np.array([1, 2, 3, 4])  # Outro vetor alvo

resultado, coef = combinacao(vetores, vetor_alvo)

if resultado:
    print(coef)
else:
    print("Não é combinação linear")

print('Caso 3')
vetores = np.array([
    [np.exp(3), np.exp(-2), np.exp(-4), np.sin(np.pi/2), np.cos(np.pi/6), 0],
    [5.43, 13, 2.5, 1, 1, 2],
    [8.145, 19.5, 3.75, 1.5, 1.5, 3.],
    [1, 4, 7.8, np.tan(np.pi/6), np.tanh(1), 3],
    [1, 4, 7.8, np.tan(np.pi/6), np.tanh(1), 3]
])  # Vetores mais complexos
vetor_alvo = np.array([1, 2, 3, 4, 5, 6])  # Vetor alvo

resultado, coef = combinacao(vetores, vetor_alvo)

if resultado:
    print(coef)
else:
    print("Não é combinação linear")
