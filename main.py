import os

os.system('code --install-extension maptz.regionfolder')


while True:

    diretorio = os.listdir('./src')

    if 'output' not in os.listdir('./'):
        os.mkdir('./output')

    out = open('./output/main.sBoticsR', 'w')
    
    os.system('cls')

    for arquivo in diretorio:
        if 'sBoticsR' in arquivo:
            arquivoAtual = open('./src/' + arquivo, 'r')
            out.write('#region ' + arquivo[:arquivo.find('.sBoticsR')] + '\n')
            for linha in arquivoAtual:
                if '#' in linha:
                    pass
                else:
                    out.write('\t' + linha)
            arquivoAtual.close()
            out.write('\n#endregion\n\n')
            
        else:
            print('-'*20, 'Arquivo inválido:', arquivo,'-'*20, end='')
        print('\n','-'*20, 'Arquivo', arquivo[:arquivo.find('.sBoticsR')], 'compilado com sucesso', '-'*20)

    out.write('fim\n')
    out.close()
    print('\nDigite compilar para compilar novamente\n')
    while input() != 'compilar':
        pass