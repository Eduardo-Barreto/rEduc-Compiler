# rEducCompiler
Um compilador de rEduc para quem quer usar uma estrutura multifile no sBotics (ironicamente também funciona pra csharp).
# Demonstração
Essa demonstração é baseada no primeiro dos [exemplos](./examples.md)

![demo](https://i.imgur.com/9tB2Ytx.gif)


# Requerimentos
Para usar, você tem que ter o python instalado, pra isso basta fazer o download [aqui](https://www.python.org/downloads/) e seguir as instruções na tela de instalação.
# Uso
Você pode baixar o [workspace padrão nas releases](https://github.com/Eduardo-Barreto/rEduc-Compiler/releases/latest) e descompactar na sua pasta de destino

Você precisa ter uma estrutura de arquivos como essa abaixo, onde compiler.py é o que você baixa deste repositório.

Dentro da pasta `src` você tem os arquivos da sua programação.
```
📂src
 └ arquivo1.sBoticsR
 └ arquivo2.sBoticsR
compiler.py
config.txt
```
O arquivo `config.txt` é o que você usa para configurar a ordem dos seus arquivos dentro da pasta `src`, basta listar o nome deles (com a extensão) na ordem dentro do arquivo, um por linha

Após realizar a configuração, basta escrever `python compiler.py` no terminal/console para executar o arquivo, escrever o nome do seu arquivo final e correr pro abraço

O compilador juntará os arquivos em um só, que ficará na pasta `out`, de acordo com a ordem configurada. Sua pasta deve terminar mais ou menos assim:
```
📂src
 └ arquivo1.sBoticsR
 └ arquivo2.sBoticsR
📂out
 └ main.sBoticsR
compiler.py
config.txt
```
Nesse caso, o `main.sBoticsR` é o importado no simulador

> OBS: Os comandos `inicio` e `fim` devem ser colocados manualmente nos arquivos da pasta `src`
