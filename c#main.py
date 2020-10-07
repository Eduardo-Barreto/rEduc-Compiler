import os

os.system('code --install-extension maptz.regionfolder')

while True:

    diretorio = os.listdir('./src')

    if 'output' not in os.listdir('./'):
        os.mkdir('./output')

    out = open('./output/main.sboticsC', 'w')
    
    os.system('cls')

    for arquivo in diretorio:
        if 'sboticsc' in arquivo.lower() or 'cs' in arquivo.lower():
            arquivoAtual = open('./src/' + arquivo, 'r')
            out.write('//' + arquivo[:arquivo.find('.sboticsC')] + '\n\n')
            for linha in arquivoAtual:
                if '// ' in linha:
                    pass
                else:
                    out.write('\t' + linha)
            arquivoAtual.close()
            out.write('\n\n//\n\n')
            
        else:
            print('-'*20, 'Arquivo inválido:', arquivo,'-'*20, end='')
        print('\n','-'*20, 'concluído', '-'*20)

    out.close()

    while input() != 'compilar':
        pass
