def modificar_formato(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r') as entrada:
        linhas = entrada.readlines()

    linhas_modificadas = []
    for linha in linhas:
        # Remover colchetes e espaços em branco
        linha_modificada = linha.replace('[', '').replace(']', '').strip()
        # Substituir o primeiro espaço por vírgula
        linha_modificada = linha_modificada.replace(' ', ',', 1)
        linha_modificada = linha_modificada + '\n'
        linhas_modificadas.append(linha_modificada)

    with open(arquivo_saida, 'w') as saida:
        saida.writelines(linhas_modificadas)

# Exemplo de uso:
arquivo_entrada = 'Vibração/VibSuporteEstatico.TXT'
arquivo_saida = 'Vibração/VibSuporteEstatico1.TXT'

modificar_formato(arquivo_entrada, arquivo_saida)