import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;

nomes_colunas = ['tempo1', 'esq', 'dir']

# Associa um arquivo .txt a uma variável
dados = pd.read_csv('DropTest/Drop2.txt', delimiter=';', names=nomes_colunas)

# Associa cada coluna da planilha a uma variável diferente
tempo = dados["tempo1"];
accX = dados["esq"];
accY = dados["dir"];
accZ = (dados["esq"]+dados['dir'])/2;
#accRes = np.sqrt(accX**2 + accY**2 + accZ**2)

dadosOriginais = pd.DataFrame({'tempo':tempo, 'accX':accX, 'accY':accY, 'accZ':accZ})
window_size = 200

dadosSuavizados = dadosOriginais.rolling(window=window_size).mean()
dadosSuavizados = dadosSuavizados.ewm(span=10).mean()

print(tempo);

# Faz o plot dos dados no gráfico
#plt.plot(dadosOriginais['tempo'], dadosSuavizados['accX'], color='red', label='Amortecedor Esquerdo');
plt.plot(dadosOriginais['tempo'], dadosSuavizados['accY'], color='blue');
#plt.plot(dadosOriginais['tempo'], dadosSuavizados['accZ'], color='green', label='Amortecedores Traseiros');
#plt.plot(tempo, accResultante, color='purple');

# Seta informações mostradas no gráfico
plt.title('DropTest 1: Curso do Amortecedor x Tempo');
plt.xlabel('Tempo (ms)');
plt.ylabel('Curso do Amortecedor (mm)');
plt.legend();

# Finaliza a plotagem do gráfico e o mostra
plt.grid();
plt.show();