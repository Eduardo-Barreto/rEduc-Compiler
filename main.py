import os

os.system('code --install-extension maptz.regionfolder')

file_name = input('Digite o nome do arquivo final (sem a extensão): ')


while True:

    directory = os.listdir('./src')

    if 'output' not in os.listdir('./'):
        os.mkdir('./output')

    out = open('./output/'+file_name+'.sBoticsR', 'w')

    os.system('cls')

    for source_file in directory:
        if 'sBoticsR' in source_file:
            current_file = open('./src/' + source_file, 'r')
            out.write('#region ' +
                      source_file[:source_file.find('.sBoticsR')] +
                      '\n')
            for line in current_file:
                out.write('\t' + line)
            current_file.close()
            out.write('\n#endregion\n\n')

        else:
            print('-'*20, 'Arquivo inválido:', source_file, '-'*20, end='')
        print('\n', '-'*20, 'Arquivo',
              source_file[:source_file.find('.sBoticsR')],
              'compilado com sucesso', '-'*20)

    out.write('fim\n')
    out.close()
    print('\nDigite compilar para compilar novamente\n')
    while input() != 'compilar':
        pass
