<p align="center">
  <a href="https://discord.gg/PubzWWjzuz">
    <img src="https://github.com/Eduardo-Barreto/rEduc-Compiler/blob/main/assets/zulLingua.png?raw=true" height="200" alt="Zul mostrando a língua" />
  </a>
</p>
<h1 align="center">rEduc Compiler</h1>

<p align="center">Um compilador de rEduc para possibilitar o uso de uma estrutura multifile no <a href="https://sbotics.weduc.natalnet.br">sBotics</a> (ironicamente também funciona pra csharp)<br>


<p align="center">
 <a href="#demonstração">Demonstração</a> • 
 <a href="#requerimentos">Requerimentos</a> • 
 <a href="#uso">Uso</a> • 
 <a href="#contribuição">Contribuição</a>
</p>


# Demonstração
Essa demonstração é baseada no primeiro dos [exemplos](./examples.md)

![demo](https://github.com/Eduardo-Barreto/rEduc-Compiler/blob/main/assets/demo.gif?raw=true)


# Requerimentos
Para usar, você tem que ter o python instalado, pra isso basta fazer o download [aqui](https://www.python.org/downloads/) e seguir as instruções na tela de instalação.

Além disso, você precisa ter o módulo `watchdog` do python instalado, é ele que vai monitorar os arquivos para compilar automaticamente a cada alteração, e para instalar você pode usar o `pip`:
```sh
$ pip install watchdog==2.0.3

# Se der errado, tente:
$ python3 -m pip install -U watchdog==2.0.3
```


# Uso
Você pode baixar o [workspace padrão nas releases](https://github.com/Eduardo-Barreto/rEduc-Compiler/releases/latest) e descompactar na sua pasta de destino, ele terá a estrutura de arquivos que você precisa, que é basicamente essa abaixo:
```
📂src
 └ main.re
 └ outro_arquivo.re
compiler.py
```

Dentro da pasta **src** você coloca os arquivos da sua programação

`main.re` é o arquivo principal do seu código, tudo bem se você quiser usar outra extensão (como `cs` para csharp ou até as extensões antigas como `sBoticsR` e `sBoticsC`), mas você deve manter o nome `main`, pois é a partir dele que o compiler trabalha.

Dentro dele você importa os seus outros arquivos na ordem que quiser, se estiver usando rEduc deve usar o comando `importar("<caminho do arquivo>")`, e em C# deve usar `import("<caminho do arquivo>")`. Estes arquivos importados podem importar outros também, que inclusive podem estar dentro de pastas! Você organiza da maneira que quiser.

O arquivo `compiler.py` é o compilador em si, basta escrever `./compiler.py` no terminal/console para o executar, escrever o nome do seu arquivo final e correr pro abraço.
> **Importante**: Você deve colocar a mesma extensão dos arquivos da `src` quando for definir o nome do arquivo final no compiler, sendo `.re`, `.cs`, `.sBoticsR` ou `.sBoticsC`.

Toda vez que você fizer uma alteração e salvar um arquivo dentro da pasta `src` ele vai compilar tudo para um arquivo (com o nome que você escolheu) na pasta `out`. Sua pasta deve terminar mais ou menos assim:
```
📂src
 └ main.re
 └ outro_arquivo.re
📂out
 └ main.re
compiler.py
```
Nesse caso, o `main.re` da pasta `out` é o importado no simulador

> OBS: Os comandos `inicio` e `fim` devem ser colocados manualmente nos arquivos da pasta `src`

Caso haja qualquer dúvida ou problema sobre o uso do compilador, basta me procurar no [discord do sBotics](https://discord.gg/PubzWWjzuz) :)


## Contribuição
Esses são os atuais contribuintes do projeto, que ajudaram a criar ele do zero!

<div align=center>

  <table style="width:100%">
      <tr align=center>
          <th><strong>Eduardo Barreto</strong></th>
          <th><strong>Vinicios Lugli</strong></th>
          <th><strong>Gabriel de Paula</strong></th>
          <th><strong>Gabriel Schorsch</strong></th>
      </tr>
      <tr align=center>
          <td>
              <a href="https://github.com/Eduardo-Barreto">
                  <img width="100%" src="https://avatars.githubusercontent.com/u/34964398?v=4">
              </a>
          </td>
          <td>
              <a href="https://github.com/ViniciosLugli">
                  <img width="90%" src="https://avatars.githubusercontent.com/u/40807526?v=4">
              </a>
          </td>
          <td>
              <a href="https://github.com/gabrieldp23">
                  <img width="110%" src="https://avatars.githubusercontent.com/u/66735014?v=4">
              </a>
          </td>
          <td>
              <a href="https://github.com/Schorsch003">
                  <img width="100%" src="https://avatars.githubusercontent.com/u/48362215?v=4">
              </a>
          </td>
      </tr>
  </table>

</div>

Além de toda a comunidade do Simulador sBotics!

### Como contribuir
Todos os tipos de contribuição são muito bem vindos e apreciados!
  - Deixar uma star no repositório
  - Encontrar e reportar bugs
  - Enviar PRs para ajudar a resolver problemas ou adicionar novas features
  - Compartilhar!

## **Simulador sBotics**
<a href="https://www.instagram.com/simulador.sbotics/"><img height="64px" src="https://github.com/Eduardo-Barreto/rEduc-Compiler/blob/main/assets/instagram.png?raw=true"/></a>
<a href="https://discord.gg/PubzWWjzuz"><img height="64px" src="https://github.com/Eduardo-Barreto/rEduc-Compiler/blob/main/assets/discord.png?raw=true"/></a>
<a href="https://sbotics.weduc.natalnet.br/"><img height="64px" src="https://github.com/Eduardo-Barreto/rEduc-Compiler/blob/main/assets/sBotics.png?raw=true"/></a>
