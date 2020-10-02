import os

os.system('code --install-extension maptz.regionfolder')

files = os.listdir('./src')

if 'output' not in os.listdir('./'):
    os.mkdir('./output')

out = open('./output/VMRT.sBoticsR', 'w')

for file in files:
    if 'sBoticsR' in file:
        a = open('./src/' + file, 'r')
        out.write('#region ' + file.strip('.sBoticsR') + '\n')
        for linha in a:
            if '#' in linha:
                pass
            else:
                out.write('\t' + linha)
        a.close()
        out.write('\n#endregion\n\n')
        
    else:
        print('-'*20, 'Arquivo inválido','-'*20, end='')
    print('\n','-'*20, 'fim do arquivo','-'*20)

out.write('fim\n')
out.close()