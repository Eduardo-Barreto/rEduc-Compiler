import os

os.system('cls' if os.name == 'nt' else 'clear')

file_name = input(
    'Enter the name of the final file' +
    '(with the extension, such as "main.sboticsr"): '
)

try:
    file_extension = str(file_name.split('.')[1]).lower()
except IndexError:
    print(
        'Please restart the program and enter the name of the final ' +
        'file as the example.'
    )
    quit()

root = os.listdir('./')

if 'config.txt' not in root:
    open('config.txt', 'w', encoding='utf-8').write(
        'Here you place the order of your /src files with their names, ' +
        ' with extension one on each line, starting with the second'
    )
    print(
        'Please configure the compiler in ' +
        '"config.txt" and restart the program'
    )
    quit()
if 'out' not in root:
    os.mkdir('./out')
if 'src' not in root:
    os.mkdir('./src')

while True:

    config = open('config.txt', 'r', encoding='utf-8')
    file_order = config.readlines()[1:]
    if file_order == []:
        print(
            'Please configure the compiler in ' +
            '"config.txt" and restart the program'
        )
        quit()

    os.system('cls' if os.name == 'nt' else 'clear')

    out = open(f'./out/{file_name}', 'w', encoding='utf-8')

    for source_file in file_order:
        source_file = source_file.strip('\n').strip()
        if file_extension in source_file.lower():
            try:
                current_file = open(
                    f'./src/{source_file}', 'r', encoding='utf-8')
            except FileNotFoundError:
                print(f'File "{source_file}" not found in /src')
                continue
            for line in current_file:
                out.write(line)
            current_file.close()
            out.write('\n\n')

        print('\n', '-'*20,
              f'"{source_file}" successfully compiled', '-'*20)

    out.close()
    print('\nPress Enter to compile again or "C" to exit\n')
    if input().lower() == 'c':
        exit()
