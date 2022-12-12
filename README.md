# M2Morse - Aplicação de Conversor de Morse com o Uso de Sockets

<p align="center">
✅ Projeto Concluído ✅
</p>

- [💬 Descrição do projeto](#-descrição-do-projeto)

- [🔢 Funcionalidades](#-funcionalidades)

- [⚙ Ferramentas utilizadas](#-ferramentas-utilizadas)

- [🖥 Abrir e rodar o projeto](#-abrir-e-rodar-o-projeto)

- [👩🏻‍💻👨🏻‍💻 Desenvolvedores](#-desenvolvedores)

## 💬 Descrição do projeto 

<p align="justify">
 Projeto desenvolvido para disciplina Redes de Computadores do curso de Engenharia de Software/Ciências da Computação da Universidade Federal do Ceará. 
 
Como inspiração para a escolha do tema tivemos em mente uma aplicação de requisição e resposta, então imaginamos um cenário onde seria possível tal ação. Depois de pensarmos a respeito, decidimos desenvolver uma aplicação de conversor de português para morse, onde posteriormente adicionamos a possibilidade de ser uma espécie de tradutor, executando a ida (traduzindo de português para morse) e a volta da conversão (morse para português), utilizando o protocolo TCP.

Por afinidade da dupla optamos pela linguagem Python. Foram realizados dois códigos, um para o servidor e outro para o cliente. Para os códigos importamos as bibliotecas: Os, Time e Socket. Utilizamos a biblioteca  os para conseguirmos limpar o terminal e o time para usarmos um temporizador de tela. A biblioteca socket foi utilizada para realizar as principais funcionalidades necessárias da aplicação, já que permite a comunicação entre dois processos. 

Para a aplicação fazer a conversão e a desconversão, a dupla pensou em uma lógica onde o uso de listas foi necessário. Na imagem abaixo, é possível analisar como a conversão é feita:

![Modelo de Conversão e Desconversão](https://user-images.githubusercontent.com/84748508/206965991-cc79452c-2989-44d7-ba81-e659b57a7a5a.png)

Para a desconversão segue a mesma lógica, a única diferença é que inverte qual lista é usada para a troca de caracteres.

Podemos concluir com esse projeto, que implementar de forma “braçal” um cliente e servidor torna o entendimento bem mais claro de como funciona a conexão via rede no nosso dia-a-dia. Tivemos dificuldades em saber como utilizar as funcionalidades da biblioteca socket, mas ao estudarmos a documentação ficou mais claro e bem dinâmica a sua implementação, quanto a aplicação em si não tivemos dificuldade.

</p>

## 🔢 Funcionalidades

:heavy_check_mark: `Funcionalidade 1:` Realiza a conversão de português para morse.

:heavy_check_mark: `Funcionalidade 2:` Realiza a conversão de morse para português.

:heavy_check_mark: `Funcionalidade 0:` Fecha a conexão.

## ⚙ Ferramentas utilizadas

- ``Python 3.10.7``

## 🖥 Abrir e rodar o projeto

Após baixar o projeto, você pode abrir com o proprio Prompt de Comando do Windows (deverá ter o python instalado!).

- Ao fazer o download do projeto, escolha uma pasta de fácil acesso;
- Pelo Prompt de Comando encontre a pasta onde os scripts estão e execute primeiro o servidor.py;
- Em seguida, em um novo Prompt de Comando repita o processo e execute o cliente.py.
- Agora poderá usar todas as funções do M2Morse! 🏆

⚠⚠⚠ Atenção: caso você tenha alguma distribuição Linux, é recomendado fazer algumas alterações no código, para que rode corretamente na sua máquina:

- Substituir a linha 27 do código cliente.py, que se encontra com:

<div align="center">

```python
os.system('cls')
```

Pelo termo aceitado no Linux:

```python
os.system('clear')
```

  </div>

Gif com a execução das três funcionalidades:

<div align="center">

 ![exemple-execution](https://user-images.githubusercontent.com/84748508/206972380-813ae566-21b3-45d8-969f-52d986f369dc.gif)

  </div>


## 👩🏻‍💻👨🏻‍💻 Desenvolvedores

| [<img src="https://avatars.githubusercontent.com/u/84748508?v=4" width=115><br><sub>Mateus Andrade</sub>](https://github.com/eumateusdev) |  [<img src="https://avatars.githubusercontent.com/u/69697277?v=4" width=115><br><sub>Milene Cavalcante</sub>](https://github.com/Milene01)  |
| :---: | :---: 
