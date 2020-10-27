import os


file_name = input('Digite o nome do arquivo final (sem a extensão): ')


while True:

    directory = os.listdir('./src')

    if 'out' not in os.listdir('./'):
        os.mkdir('./out')

    out = open('./out/'+file_name+'.sboticsC', 'w')

    os.system('cls')

    for source_file in directory:
        if 'sboticsc' in source_file.lower() or 'cs' in source_file.lower():
            current_file = open('./src/' + source_file, 'r')
            for line in current_file:
                if '//' in line:
                    pass
                else:
                    out.write(line)
            current_file.close()
            out.write('\n\n')

        else:
            print('-'*20, 'Arquivo inválido:', source_file,'-'*20, end='')
        print('\n', '-'*20, 'Arquivo', source_file[:source_file.lower().find('.sboticsc')], 'compilado com sucesso', '-'*20)

    out.close()

    print('\nDigite compilar para compilar novamente\n')
    while input() != 'compilar':
        pass
