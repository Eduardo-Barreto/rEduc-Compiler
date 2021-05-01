# Exemplo 1
Um primeiro exemplo simples, somente para mostrar como funciona.
## Estrutura inicial do seu código e arquivos
```
📂src
 └ main.re
 └ outro_arquivo.re
compiler.py
```

**`compiler.py`**
Esse é o arquivo responsável por todo o trabalho de compilar, nele você não precisa mexer

### Pasta `src`
- **`main.re`**
Nesse arquivo você coloca uma parte da sua programação e importa o outro arquivo
    ```re
    inicio
        escrever(1, "Isso é do primeiro arquivo!")
        importar("outro_arquivo")
    fim
    ```
- **`outro_arquivo.re`**
Nesse arquivo você coloca outra parte da sua programação
    ```re
        escrever(2, "Isso é do segundo arquivo!")
    ```

## Estrutura final
Após rodar o compilador e salvar suas alterações, seus arquivos devem estar assim:
```
📂out
 └ main.re
📂src
 └ main.re
 └ outro_arquivo.re
compiler.py
```
Esse `main.re` na pasta `out` é o arquivo gerado pelo compilador, que é o que você importa no simulador, e ele fica assim:
```re
inicio
    escrever(1, "Isso é do primeiro arquivo!")
# file "./src/outro_arquivo.re"
    escrever(2, "Isso é do segundo arquivo!")

# endfile "./src/outro_arquivo.re"
fim
```

# Exemplo 2
Um exemplo levemente mais complexo, abordando novas pastas dentro da `/src`.
## Estrutura inicial do seu código e arquivos
```
📂src
 └ main.re
 └ 📂devs
    └ julio.re
    └ lucas.re
compiler.py
```

**`compiler.py`**
Esse é o arquivo responsável por todo o trabalho de compilar, nele você não precisa mexer

### Pasta `src`
- **`main.re`**
Nesse arquivo você coloca uma parte da sua programação e importa o outro arquivo
    ```re
    inicio

        escrever(1, "uau essa eh a main")
        importar("devs/julio")

    fim
    ```

- **`/devs/julio.re`**
Nesse arquivo você coloca outra parte da sua programação
    ```re
        escrever(1, "eu sou o julio")
        importar("devs/lucas")
    ```
- **`/devs/lucas.re`**
Nesse arquivo você coloca outra parte da sua programação
    ```re
        escrever(1, "eu sou o lucas")
    ```


## Estrutura final
Após rodar o compilador e salvar suas alterações, seus arquivos devem estar assim:
```
📂src
 └ main.re
 └ 📂devs
    └ julio.re
    └ lucas.re
📂out
 └ out.re
compiler.py
```
Esse `main.re` na pasta `out` é o arquivo gerado pelo compilador, que é o que você importa no simulador, e ele fica assim:
```re
inicio

    escrever(1, "uau essa eh a main")

# file "./src/devs/julio.re"
    escrever(1, "eu sou o julio")
# file "./src/devs/lucas.re"
    escrever(1, "eu sou o lucas")
# endfile "./src/devs/lucas.re"
# endfile "./src/devs/julio.re"

fim
```