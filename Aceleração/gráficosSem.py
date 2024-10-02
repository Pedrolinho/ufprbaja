import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;

nomes_colunas = ['tempo', 'x', 'y', 'z', 'xyz']

# Associa um arquivo .txt a uma variável
dados = pd.read_csv('Aceleração/DadosSemBarra.txt', delimiter='\t', names=nomes_colunas)

# Associa cada coluna da planilha a uma variável diferente
tempo = dados["tempo"];
accX = dados["x"];
accY = dados["y"];
accZ = dados["z"];
accRes = dados["xyz"];

dadosOriginais = pd.DataFrame({'tempo':tempo, 'accX':accX, 'accY':accY, 'accZ':accZ, 'accRes':accRes})
window_size = 5000

dadosSuavizados = dadosOriginais.rolling(window=window_size).mean()

# Faz o plot dos dados no gráfico
#plt.plot(dadosOriginais['tempo'], dadosSuavizados['accX'], color='red', label='Eixo X', lw = 2);
#plt.plot(dadosOriginais['tempo'], dadosSuavizados['accY'], color='blue', label='Eixo Y', lw = 2);
#plt.plot(dadosOriginais['tempo'], dadosSuavizados['accZ'], color='green', label='Eixo Z', lw = 2);
plt.plot(tempo, dadosSuavizados['accRes'], color='purple', label = 'Eixo Resultante', lw = 2);

# Seta informações mostradas no gráfico
plt.title('Aceleração x Tempo (Sem Barra)');
plt.xlabel('Tempo (s)');
plt.ylabel('Aceleração (m/s²)');
plt.legend()

# Finaliza a plotagem do gráfico e o mostra
plt.grid();
plt.show();