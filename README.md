# R-EducCompiler
Um compilador de R-Educ para quem quer usar uma estrutura multifile (uma cópia do [sbotics compiler](https://github.com/GRFreire/sboticscompiler), porém pra R-Educ.
# Requerimentos
Para usar, você tem que ter o python instalado, pra isso basta fazer o download [aqui](python.org/download) e seguir as instruções na tela de instalação
# Uso
Você precisa ter uma estrutura de arquivos como essa abaixo, onde main.py é o que você baixa deste repositório.
📂src
 └ arquivo1.sBoticsR
 └ arquivo2.sBoticsR
 └ arquivo3.sBoticsR
main.py
```
Pra rodar, é só escrever `python main.py` no terminal/console e pronto
O programa junta todos os arquivos em um só, o resultado final é algo como isso:
```
📂src
 └ arquivo1.sBoticsR
 └ arquivo2.sBoticsR
 └ arquivo3.sBoticsR
📂output
 └ main.sBoticsR
main.py
```
e é esse `main.sBoticsR` que você importa no simulador :)

Aqui embaixo tem uma demonstração:
![Como usar](./ComoUsar.gif)