import numpy as np

# Definição de vetores
v = [
    np.array([1, 1j, 1], dtype='complex128'),
    np.array([4, 3, 2], dtype='complex128'),
    np.array([2+3j, complex(np.sqrt(3), np.pi), 3], dtype='complex128'),
    np.array([complex(np.cos(np.pi/2), np.sin(np.pi/2)), 1, complex(np.exp(-2), 0)], dtype='complex128')
]

beta = [
    3 + 4j,
    np.exp(-np.pi/2),
    -12345 + 28413j
]

# Funções
# Axioma 1 - Soma de vetores
def soma(u, v):
    return u + v  # Operação de soma de vetores

def verifica_soma(u, v):
    w = soma(u, v)
    return w.shape == (3,) and w.dtype == 'complex128'  # Verifica se o vetor resultante tem as propriedades esperadas

print('Testando fechamento da soma:')
for i in range(len(v)):
    for k in range(i + 1, len(v)):
        print(verifica_soma(v[i], v[k]), ' => ', v[i], ' , ', v[k])

# Axioma 6 - Produto de vetor por escalar
def produto(beta, u):
    modulo_beta = np.abs(beta)  # Definindo o módulo do escalar complexo
    return modulo_beta * u  # Multiplicação de vetor por escalar

def verifica_produto(beta, u):
    w = produto(beta, u)
    return w.shape == (3,) and w.dtype == 'complex128'

print('--------------------------------------')
print('Testando fechamento do produto escalar:')
for i in range(len(beta)):
    for k in range(len(v)):
        print(verifica_produto(beta[i], v[k]), ' => ', beta[i], ' , ', v[k])

# Axioma 4 - Vetor nulo
nulo = np.zeros(3, dtype='complex128')

def verifica_nulo(v):
    return np.all(soma(v, nulo) == v)

print('--------------------------------------')
print('Testando vetor nulo:')
for i in range(len(v)):
    print(verifica_nulo(v[i]), ' => ', v[i])

# Axioma 5 - Vetor inverso
def inverso(v):
    return -v

def verifica_inverso(v):
    return np.all(soma(v, inverso(v)) == nulo)

print('--------------------------------------')
print('Testando vetor inverso:')
for i in range(len(v)):
    print(verifica_inverso(v[i]), ' => ', v[i])

# Axioma 2 - Comutatividade
def verifica_comutatividade(u, v):
    return np.array_equal(soma(u, v), soma(v, u))

print('--------------------------------------')
print('Testando comutatividade:')
for i in range(len(v)):
    for k in range(i + 1, len(v)):
        print(verifica_comutatividade(v[i], v[k]), ' => ', v[i], ' , ', v[k])

# Axioma 3 - Associatividade
def verifica_associatividade(u, v, w):
    return np.array_equal(soma(u, soma(v, w)), soma(soma(u, v), w))

print('--------------------------------------')
print('Testando associatividade:')
for i in range(len(v)):
    for k in range(i + 1, len(v)):
        for l in range(k + 1, len(v)):
            print(verifica_associatividade(v[i], v[k], v[l]), ' => ', v[i], ' , ', v[k], ' , ', v[l])

# Axioma 7 - Distributividade 1
def verifica_distributividade_1(beta, u, v):
    return np.array_equal(produto(beta, soma(u, v)), soma(produto(beta, u), produto(beta, v)))

print('--------------------------------------')
print('Testando distributividade 1:')
for i in range(len(beta)):
    for k in range(len(v)):
        for l in range(k + 1, len(v)):
            print(verifica_distributividade_1(beta[i], v[k], v[l]), ' => ', beta[i], ' , ', v[k], ' , ', v[l])

# Axioma 8 - Distributividade 2
def verifica_distributividade_2(beta, gama, u):
    return np.array_equal(produto(beta + gama, u), soma(produto(beta, u), produto(gama, u)))

print('--------------------------------------')
print('Testando distributividade 2:')
for i in range(len(beta)):
    for k in range(i + 1, len(beta)):
        for l in range(len(v)):
            print(verifica_distributividade_2(beta[i], beta[k], v[l]), ' => ', beta[i], ' , ', beta[k], ' , ', v[l])

# Axioma 9 - Distributividade 3
def verifica_distributividade_3(beta, gama, u):
    return np.array_equal(produto(beta, produto(gama, u)), produto(beta * gama, u))

print('--------------------------------------')
print('Testando distributividade 3:')
for i in range(len(beta)):
    for k in range(i + 1, len(beta)):
        for l in range(len(v)):
            print(verifica_distributividade_3(beta[i], beta[k], v[l]), ' => ', beta[i], ' , ', beta[k], ' , ', v[l])

# Axioma 10 - Escalar unitário
def verifica_escalar_unitario(u):
    return np.array_equal(produto(1, u), u)

print('--------------------------------------')
print('Testando o axioma do escalar unitário:')
for i in range(len(v)):
    print(verifica_escalar_unitario(v[i]), ' => ', v[i])
