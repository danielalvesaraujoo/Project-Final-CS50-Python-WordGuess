# Word Guess - Harry Potter Edition 🧙‍♂️

#### Video Demo:  <URL HERE>

Claro! Abaixo está uma versão expandida do seu `README.md`, com mais de **500 palavras**, mantendo clareza, organização e profissionalismo. Também inclui melhorias de formatação e descrição, mantendo o tom amigável e educativo:

---

# 🧙‍♂️ Adivinhação de Palavras - Edição Harry Potter

## 📽️ Demonstração em vídeo

*(Adicione aqui o link da demonstração se houver)*

---

## 📌 Descrição

Este projeto foi desenvolvido como trabalho final da disciplina **Introdução à Programação com Python**, do curso **CS50** oferecido por **Harvard University**.

O jogo é uma versão temática do clássico jogo de adivinhação de palavras, ambientado no universo mágico de **Harry Potter**. Desenvolvido completamente em Python, o objetivo é reforçar os conceitos de programação aprendidos ao longo do curso, como estruturas de repetição, listas, funções e manipulação de strings.

---

## 🎮 Sobre o jogo

O jogo propõe um desafio simples e divertido: adivinhar uma palavra secreta relacionada ao universo de Harry Potter, uma letra por vez.

### Regras básicas:

* A palavra é escolhida aleatoriamente de uma lista com termos mágicos.
* O jogador tem **cinco chances** de errar. Se errar mais do que isso, perde o jogo.
* Letras já utilizadas são registradas e exibidas para evitar repetições.
* O jogo não diferencia entre **letras maiúsculas e minúsculas**.

O desafio está em descobrir a palavra inteira antes que o número de tentativas incorretas se esgote!

---

## 🧠 Palavras do Universo Mágico

As palavras são cuidadosamente selecionadas do mundo de Harry Potter. Alguns exemplos incluem:

* "harry"
* "hermione"
* "ron"
* "hogwarts"
* "varinha"
* "grifinória"
* "sonserina"
* "patronum"
* "dementor"
* "hippogriff"
* "horcrux"
* "broomstick"
  ...e muitas outras!

---

## 🧾 Como o código funciona

O projeto está organizado em funções, o que torna o código limpo e reutilizável. A seguir, uma visão geral das principais partes:

* `main()`: Função principal que gerencia o fluxo do jogo, incluindo a lógica de tentativas, entrada do usuário e exibição dos resultados.
* `escolher_palavra(palavras)`: Seleciona aleatoriamente uma palavra da lista fornecida.
* `atualizar_palavra_escondida(palavra_sorteada, palavra_escondida, letra)`: Atualiza a palavra visível ao jogador com as letras já adivinhadas.
* `jogada(...)`: Processa cada tentativa do jogador, verifica se a letra está correta e atualiza o estado da palavra e das tentativas.

Essas funções trabalham juntas para proporcionar uma experiência interativa e divertida.

---

## ▶️ Como jogar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Execute o arquivo `project.py` em seu terminal ou editor Python.
3. O jogo exibirá a palavra oculta como uma sequência de traços (ex: `---` para uma palavra de 3 letras).
4. Digite uma letra por vez quando solicitado.
5. Se a letra estiver correta, será revelada na palavra. Caso contrário, uma tentativa será descontada.
6. Você tem **cinco chances** de erro.
7. Se acertar todas as letras, verá a mensagem:
   **`Parabéns! 🎉 Você acertou a palavra: 'ron'`**
8. Se errar todas as tentativas, verá:
   **`Você perdeu. 💀 A palavra era: 'ron'`**

💡 Letras digitadas anteriormente são exibidas para ajudá-lo a não repetir palpites.

> Exemplo:
> Suponha que a palavra a ser adivinhada seja `ron`.
> A mensagem inicial será: `palavra: ---`
> Se você digitar a letra `o`, será exibido: `palavra: -o-`.
> O jogo continua até você adivinhar todas as letras corretamente ou errar 5 vezes.

<img width="494" height="619" alt="image" src="https://github.com/user-attachments/assets/c2f1bd3b-2dbf-4b44-936c-291765419033" />

---

## 💻 Tecnologias utilizadas

* Python 3.x
* Terminal/Console para entrada e saída de dados
* Biblioteca `random` (nativa)

---

## 🎯 Objetivos de aprendizado

* Aplicar lógica de programação e controle de fluxo.
* Trabalhar com listas, strings e funções em Python.
* Criar um projeto interativo de terminal.
* Praticar boas práticas de organização e estruturação de código.

---




