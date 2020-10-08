import os

os.system('code --install-extension maptz.regionfolder')

while True:

    directory = os.listdir('./src')

    if 'output' not in os.listdir('./'):
        os.mkdir('./output')

    out = open('./output/main.sboticsC', 'w')
    
    os.system('cls')

    for source_file in directory:
        if 'sboticsc' in source_file.lower() or 'cs' in source_file.lower():
            current_file = open('./src/' + source_file, 'r')
            out.write('//' + source_file[:source_file.find('.sboticsC')] + '\n\n')
            for line in current_file:
                if '// ' in line:
                    pass
                else:
                    out.write('\t' + line)
            current_file.close()
            out.write('\n\n//\n\n')
            
        else:
            print('-'*20, 'Arquivo inválido:', source_file,'-'*20, end='')
        print('\n','-'*20, 'concluído', '-'*20)

    out.close()

    while input() != 'compilar':
        pass
