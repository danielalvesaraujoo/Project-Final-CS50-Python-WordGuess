# Word Guess - Harry Potter Edition 🧙‍♂️

#### Video Demo:  <URL HERE>
#### Description:
This is the final project for [CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/) from Harvard University, developed in Python.  
The game is a themed version of the classic word-guessing game, set in the magical universe of **Harry Potter**.

## 🎮 About the Game

The player must guess a secret word related to the Harry Potter world, one letter at a time. The goal is to figure out the entire word before running out of attempts.

- Each word is randomly selected from a predefined list.
- The player has **5 chances** to make incorrect guesses before losing.
- Already used letters are stored and displayed to avoid repetition.

## 🧠 Words from the Magical Universe

Some examples of words used in the game:
- "harry"
- "hermione"
- "ron"
- "hogwarts"
- "wand"
- "gryffindor"
- "slytherin"
- ... and others!

## 🧾 How the Code Works

The game is composed of the following main functions:

- "main()": Manages the game’s core logic, including user input, remaining attempts, and win/lose conditions.
- "escolher_palavra(palavras)": Randomly selects a word from the list.
- "atualizar_palavra_escondida(palavra_sorteada, palavra_escondida, letra)": Updates the hidden word with the correctly guessed letters.
- "jogada(letras_adivinhadas, letra, palavra_sorteada, palavra_escondida)": Processes a guess and returns the updated state of the word, whether the guess was correct, and if it was a missed attempt.

## ▶️ How to Play

1. Run the "project.py" file.  
2. The game will prompt you to enter a letter — keep typing letters whenever asked until you guess the word.

<img width="494" height="619" alt="image" src="https://github.com/user-attachments/assets/c2f1bd3b-2dbf-4b44-936c-291765419033" />

