import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Função para leitura dos arquivos WAV
def read(file):
    sample_rate, data = wav.read(file)
    if len(data.shape) == 2:  # Verifica se tem 2 canais
        data = np.mean(data, axis=1)
    return sample_rate, data

# Leitura dos arquivos de áudio
rate1, audio1 = read("audio1.wav")
rate2, audio2 = read("audio2.wav")
min_len = min(audio1.shape[0], audio2.shape[0])

# Ajustando o tamanho dos áudios para o menor comprimento
audio1 = audio1[:min_len]
audio2 = audio2[:min_len]

# Criando os vetores de tempo
time1 = np.linspace(0., len(audio1) / rate1, len(audio1))
time2 = np.linspace(0., len(audio2) / rate2, len(audio2))

# Definindo os coeficientes da combinação linear
a = 0.7  # Coeficiente para o áudio 1
b = 0.3  # Coeficiente para o áudio 2

# Fazendo a combinação linear dos áudios
result = a * audio1 + b * audio2

# Normalizando o resultado para evitar distorção
result = result / np.max(np.abs(result))  # Mantendo valores entre -1 e 1
result = np.int16(result * 32767)  # Convertendo para int16

# Gerando o vetor de tempo para o resultado
result_time = np.linspace(0., len(result) / rate1, len(result))

# Plot do áudio 1
plt.subplot(3, 1, 1)
plt.plot(time1, audio1, label="Áudio 1")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.legend()

# Plot do áudio 2
plt.subplot(3, 1, 2)
plt.plot(time2, audio2, label="Áudio 2")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.legend()

# Plot do resultado
plt.subplot(3, 1, 3)
plt.plot(result_time, result, label="Resultado")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.legend()

plt.show()

# Salvando o arquivo resultante
wav.write("resultado.wav", rate1, result)
print(f'Coeficiente 1: {a}, Coeficiente 2: {b}')
