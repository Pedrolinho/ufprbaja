def converter_notacao(termo):
    partes = termo.split('E')
    numero = float(partes[0])
    expoente = int(partes[1])
    return numero * (10 ** expoente)

def formatar_termo(termo):
    return "{:.3f}".format(termo)

nome_arquivo_entrada = "DadosComBarra2.txt"
nome_arquivo_saida = "DadosComBarra.txt"

# Abrindo o arquivo de entrada em modo de leitura e o arquivo de saída em modo de escrita
try:
    with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada, \
            open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        # Iterando sobre cada linha do arquivo de entrada
        for linha in arquivo_entrada:
            # Removendo espaços em branco no início e no final da linha e dividindo em termos individuais
            termos = linha.strip().split()
            
            # Aplicando a conversão para cada termo e formatando com 3 casas decimais
            termos_convertidos = [formatar_termo(converter_notacao(termo)) for termo in termos]
            
            # Escrevendo os termos convertidos no arquivo de saída
            linha_convertida = '\t'.join(termos_convertidos) + '\n'
            arquivo_saida.write(linha_convertida)
except FileNotFoundError:
    print("O arquivo de entrada '{}' não foi encontrado.".format(nome_arquivo_entrada))
except Exception as e:
    print("Ocorreu um erro ao processar o arquivo:", e)