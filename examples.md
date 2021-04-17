# Exemplo
## Estrutura inicial do seu código e arquivos
```
📂src
 └ arquivo1.sBoticsR
 └ arquivo2.sBoticsR
compiler.py
config.txt
```

**`compiler.py`**
Esse é o arquivo responsável por todo o trabalho de compilar, nele você nao precisa mexer


**`config.txt`**
Esse é o arquivo onde você configura a ordem dos seus arquivos da `/src`, lembre-se de manter a primeira linha
```
Here you place the order of your /src files with their names,  with extension one on each line, starting with the second
arquivo1.sboticsr
arquivo2.sboticsr
```

### src
**`arquivo1.sBoticsR`**
Nesse arquivo você coloca uma parte da sua programação
```
escrever(1, "Esse é do primeiro arquivo!")
```
**`arquivo2.sBoticsR`**
Nesse arquivo você coloca uma parte da sua programação
```
escrever(2, "Esse é do segundo arquivo!")
```

## Estrutura final
Após rodar o compilador, seus arquivos devem estar assim
```
📂out
 └ main.sBoticsR
📂src
 └ arquivo1.sBoticsR
 └ arquivo2.sBoticsR
compiler.py
config.txt
```
Esse `main.txt` é o arquivo gerado pelo compilador, que é o que você importa no simulador

> Você também pode usar pastas dentro da `src`, basta configurar com o caminho no `config.txt`
