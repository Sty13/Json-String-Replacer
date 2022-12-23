import sys
from termcolor import colored
import pip
import subprocess

# Instala dependências 

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def install_deps():
    with open('requirements.txt') as f:
        deps = f.read().splitlines()
    for dep in deps:
        install(dep)

if __name__ == '__main__':
    install_deps()
# Instala dependências 

# Coloque o nome dos arquivos que você deseja alterar as strings aqui:
json_files = [
'1.json',
'2.json', 
'3.json', 
'4.json'
]
# Você pode separar os itens em linha (apertando enter depois da ,). Caso você tenha múltiplos arquivos, você pode dar ctrl c nos arquivos da pasta e ctrl v aqui no código (exemplo: https://gyazo.com/5793dfddd45a6b66dac97b2578cab34e.gif), 
# com isso você pode apertar ctrl + alt + flecha para baixo para adicionar múltiplos cursores e adicionar a formatação correta (que é: ['arquivo.json', 'arquivo2.json'])


#A string que você quer alterar
antiga_string = 'String Antiga'

#A string que você quer que seja colocada no lugar 
nova_string = 'String Nova'


for json_file in json_files:
  try:
    with open(json_file, "r+", encoding="utf8") as f:
      contents = f.read()
      f.seek(0)
      f.write(contents.replace(antiga_string, nova_string))
      print(colored('Feito', 'green'))
      f.truncate()
  except Exception as err:
    print(colored(f'Erro no {json_file}: {err}', 'red'))
