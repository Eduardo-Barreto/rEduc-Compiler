import os


# Utils ----------------------------------------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# Classes ----------------------------------------------------------------


class MainFileManager():
    def __init__(self):
        self.watch_dirs = ['out', 'src']
        self.name = ""
        self.command = ""
        self.extension = ""
        self.comment = ""

    def checkExtension(self, name):
        self.name = name
        try:
            self.extension = str(self.name.split('.')[1]).lower()
        except IndexError:
            print(
                'Please restart the program and enter the name of the final ' +
                'file as the example, with the extension.'
            )
            quit()

    def language(self):
        if(self.extension.lower() in ['sboticsr', 're']):
            self.command, self.extension, self.comment = (
                'importar', self.extension, '#'
            )
        else:
            self.command, self.extension, self.comment = (
                'import', self.extension, '//'
            )

    def diretory(self):
        root = os.listdir('./')
        for folder in self.watch_dirs:
            if folder not in root:
                os.mkdir(f'./{folder}')


class ImporterManager():
    def include(self, out_name, import_name):
        print("importing:", import_name)
        out_file = open(out_name, 'w', encoding='utf-8')
        try:
            file_to_import = open(import_name, 'r', encoding='utf-8')
        except FileNotFoundError:
            print(f'File {import_name} not found')
            return

        for line in file_to_import.readlines():
            if line.startswith(MainFile.command):
                file_imported = line.replace(MainFile.command, '')
                file_imported = file_imported.strip()[
                    2:file_imported.find('")')]
                file_imported = (
                    f'./src/{file_imported}.' +
                    f'{MainFile.extension}'
                )
                self.include(out_name, file_imported)
            else:
                out.write(line)

        out_file.write(f'{MainFile.comment} file "{import_name}"\n')
        out_file.write(str(file_to_import.read()))
        out_file.write(f'\n{MainFile.comment} end file\n\n\n')
        out_file.close()
        file_to_import.close()


# Instances ----------------------------------------------------------------
MainFile = MainFileManager()
MainFile.checkExtension(
    input(
        'Enter the name of the final file' +
        '(with the extension, such as "main.sboticsr"): '
    )
)
MainFile.diretory()
MainFile.language()

Importer = ImporterManager()
# Init ----------------------------------------------------------------
clear()


while True:
    clear()

    source_main = open(
        f'./src/main.{MainFile.extension}',
        'r',
        encoding='utf-8'
    )

    out = open(f'./out/{MainFile.name}', 'w', encoding='utf-8')

    for line in source_main.readlines():
        if line.startswith(MainFile.command):
            file_to_import = line.replace(MainFile.command, '')
            file_to_import = file_to_import.strip()[
                2:file_to_import.find('")')]
            file_to_import = (
                f'./src/{file_to_import}.' +
                f'{MainFile.extension}'
            )
            Importer.include(
                f'./out/{MainFile.name}', file_to_import)
        else:
            out.write(line)

    out.close()
    source_main.close()
    print('\nPress Enter to compile again or "C" to exit\n')
    if input().lower() == 'c':
        exit()

# TODO: verificação de loop de importação
