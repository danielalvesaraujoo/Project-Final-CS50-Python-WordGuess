# 🧙‍♂️ Word Guessing Game - Harry Potter Edition

## 📽️ Video Demonstration

*(Add the demo link here if available)*

---

## 📌 Description

This project was developed as the final assignment for the course **Introduction to Programming with Python**, part of the **CS50** program offered by **Harvard University**.

The game is a themed version of the classic word guessing game, set in the magical world of **Harry Potter**. Fully developed in Python, its purpose is to reinforce programming concepts learned throughout the course, such as loops, lists, functions, and string manipulation.

---

## 🎮 About the Game

The game offers a simple and fun challenge: guess a secret word related to the Harry Potter universe, one letter at a time.

### Basic Rules:

* The word is randomly chosen from a list of magical terms.
* The player has **five chances** to make mistakes. If they exceed this limit, the game is lost.
* Already used letters are tracked and displayed to avoid repetition.
* The game is **case-insensitive** (no distinction between uppercase and lowercase letters).

The challenge is to guess the entire word before running out of incorrect attempts!

---

## 🧠 Words from the Magical Universe

The words are carefully selected from the Harry Potter world. Some examples include:

* "harry"
* "hermione"
* "ron"
* "hogwarts"
* "wand"
* "gryffindor"
* "slytherin"
* "patronum"
* "dementor"
* "hippogriff"
* "horcrux"
* "broomstick"
  ...and many more!

---

## 🧾 How the Code Works

The project is organized into functions, keeping the code clean and reusable. Below is an overview of the main components:

* `main()`: The main function that controls the game flow, including logic for attempts, user input, and displaying results.
* `choose_word(words)`: Randomly selects a word from the provided list.
* `update_hidden_word(chosen_word, hidden_word, letter)`: Updates the visible word with the correctly guessed letters.
* `make_guess(...)`: Processes each guess, checks if the letter is correct, and updates the word and attempt state accordingly.

These functions work together to provide an interactive and engaging experience.

---

## ▶️ How to Play

1. Make sure Python is installed on your machine.
2. Run the `project.py` file in your terminal or Python editor.
3. The game will display the hidden word as a series of dashes (e.g., `---` for a 3-letter word).
4. Enter one letter at a time when prompted.
5. If the letter is correct, it will be revealed in the word. If not, you lose one attempt.
6. You have **five chances** to make mistakes.
7. If you guess all the letters, you’ll see the message:
   **`Congratulations! 🎉 You guessed the word: 'ron'`**
8. If you use up all your chances, you’ll see:
   **`You lost. 💀 The word was: 'ron'`**

💡 Previously guessed letters are shown to help you avoid repeating guesses.

> Example:
> Suppose the word to guess is `ron`.
> The initial message will be: `word: ---`
> If you type the letter `o`, it will display: `word: -o-`.
> The game continues until you guess all letters correctly or make 5 mistakes.

<img width="494" height="619" alt="image" src="https://github.com/user-attachments/assets/c2f1bd3b-2dbf-4b44-936c-291765419033" />

---

## 💻 Technologies Used

* Python 3.x
* Terminal/Console for input and output
* Native `random` library

---

## 🎯 Learning Objectives

* Apply programming logic and flow control.
* Work with lists, strings, and functions in Python.
* Create an interactive terminal-based project.
* Practice good code organization and structure.

---
