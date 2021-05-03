import os
import datetime
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Variables
out = None

# Utils ----------------------------------------------------------


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
# Classes ----------------------------------------------------------------


class colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


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
		print(f'{colors.OKBLUE}importing: {import_name}{colors.ENDC}')
		out_file = open(out_name, 'w', encoding='utf-8')
		try:
			file_to_import = open(import_name, 'r', encoding='utf-8')
		except FileNotFoundError:
			print(f'File {import_name} not found')
			return

		out.write(f'{MainFile.comment} file "{import_name}"\n')

		for line in file_to_import.readlines():
			if line.find(MainFile.command) > -1:
				file_imported = line.replace(MainFile.command, '')
				file_imported = file_imported.replace(f'.{MainFile.extension}', '')
				file_imported = file_imported[file_imported.find('("')+2:file_imported.find('")')]
				file_imported = (
					f'./src/{file_imported}.' +
					f'{MainFile.extension}'
				)
				self.include(out_name, file_imported)
			else:
				out.write(line)
		out.write(f'\n{MainFile.comment} endfile "{import_name}"\n')
		file_to_import.close()


# Instances ----------------------------------------------------------------
MainFile = MainFileManager()
MainFile.checkExtension(
	input(
		'Enter the name of the final file' +
		'(with the extension, such as "main.cs"): '
	)
)
MainFile.diretory()
MainFile.language()

Importer = ImporterManager()
# Init ----------------------------------------------------------------
clear()

print("Waiting modifications...")


def Process():
	global out
	clear()
	data = datetime.datetime.now().replace(microsecond=0)

	out = open(f'./out/{MainFile.name}', 'w', encoding='utf-8')
	Importer.include(f'./out/{MainFile.name}', f'./src/main.{MainFile.extension}')

	print(f'{colors.OKGREEN}Compiled at: {data.time()}{colors.ENDC}')
	out.close()


class Handler(FileSystemEventHandler):

	@staticmethod
	def on_any_event(event):
		if event.is_directory:
			return None

		elif event.event_type == 'modified':
			Process()
			time.sleep(1)


class Watcher:
	DIRECTORY_TO_WATCH = "./src"

	def __init__(self):
		self.observer = Observer()

	def run(self):
		event_handler = Handler()
		self.observer.schedule(
			event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
		self.observer.start()
		try:
			while True:
				time.sleep(5)
		except:
			self.observer.stop()
			print("Error")

		self.observer.join()


if __name__ == '__main__':
	w = Watcher()
	w.run()
