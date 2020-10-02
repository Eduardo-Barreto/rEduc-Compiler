import os

files = os.listdir('./src')

if 'output' not in os.listdir('./'):
    os.mkdir('./output')

out = open('./output/main.sBoticsR', 'w')

out.write('inicio\n\n')

for file in files:
    if 'sBoticsR' in file:
        a = open('./src/' + file, 'r')
        for linha in a:
            if '#' in linha:
                pass
            else:
                print(linha, end='')
                out.write('\t' + linha)
        a.close()
        
    else:
        print('-'*20, 'Arquivo inválido','-'*20, end='')
    print('\n','-'*20, 'fim do arquivo','-'*20)
    out.write('\n')

out.write('\nfim\n')
out.close()