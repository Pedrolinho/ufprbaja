def separar_linhas(arquivo_entrada, arquivo_saida1, arquivo_saida2):
    with open(arquivo_entrada, 'r') as entrada:
        linhas = entrada.readlines()

    linhas_arquivo1 = [linha for i, linha in enumerate(linhas) if i % 2 == 0]
    linhas_arquivo2 = [linha for i, linha in enumerate(linhas) if i % 2 != 0]

    with open(arquivo_saida1, 'w') as saida1:
        saida1.writelines(linhas_arquivo1)

    with open(arquivo_saida2, 'w') as saida2:
        saida2.writelines(linhas_arquivo2)

arquivo_entrada = 'DropTest/DROPTEST-2.TXT'
arquivo_saida1 = 'DropTest/Drop3.TXT'
arquivo_saida2 = 'DropTest/Drop4.TXT'

separar_linhas(arquivo_entrada, arquivo_saida1, arquivo_saida2)