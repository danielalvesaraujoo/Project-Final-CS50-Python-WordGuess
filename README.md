🧙‍♂️ Word Guessing Game - Harry Potter Edition
📽️ Video Demonstration: https://youtu.be/5Fqr4Bm1nco

📌 Description

This project was developed as the final assignment for the course Introduction to Programming with Python, part of the CS50 program offered by Harvard University.

The game is a themed version of the classic word guessing game, set in the magical world of Harry Potter. Fully developed in Python, its purpose is to reinforce programming concepts learned throughout the course, such as loops, lists, functions, and string manipulation.

Additionally, this version introduces visual feedback using images that change according to the player's progress. This improvement enhances the gameplay experience, allowing players to not only interact via the terminal but also see visual representations of the hangman state, correct guesses, and victory or defeat outcomes.

The project demonstrates practical use of Python standard libraries, including os and shutil for file manipulation, and time for controlling game pacing. It also showcases good coding practices, such as function modularity, input validation, and proper tracking of game state.

Through this project, players reinforce their knowledge of Python programming while enjoying an engaging and thematic game experience, combining text-based gameplay with visual storytelling in the magical Harry Potter universe.

🎮 About the Game

The game offers a simple yet fun challenge: guess a secret word from the Harry Potter universe, one letter at a time.

Basic Rules:

The word is randomly chosen from a curated list of magical terms.

The player has six chances to make mistakes. If this limit is exceeded, the game is lost.

Already used letters are tracked and displayed to avoid repetition.

The game is case-insensitive, so uppercase and lowercase letters are treated the same.

Visual feedback is provided via images stored in the images folder:

inicio.png – the initial screen, displayed only once at the start of the game.
<img width="651" height="751" alt="inicio" src="https://github.com/user-attachments/assets/a8e61ee4-7830-4a3d-aca8-d2693ff05768" />

forca.png – displayed after the first guess to indicate the start of the hangman challenge.
<img width="651" height="751" alt="forca" src="https://github.com/user-attachments/assets/70da3e21-1cee-4753-b023-b15f50d21549" />

1.png to 6.png – updated images that correspond to each incorrect guess.
<img width="1582" height="1219" alt="1a6PNG" src="https://github.com/user-attachments/assets/ed7f9572-43b9-440c-82a7-f29ba5907b1f" />


venceu.png – displayed when the player successfully guesses the word.
<img width="651" height="751" alt="venceu" src="https://github.com/user-attachments/assets/d1cd6c33-be05-4a14-bd37-483ae671e4bc" />

Players must guess the entire word before running out of incorrect attempts. The combination of terminal-based interaction and dynamic images creates a more immersive experience compared to traditional text-based hangman games.

🧠 Words from the Magical Universe

The words are carefully selected from the Harry Potter world. Some examples include:

"harry"

"hermione"

"ron"

"hogwarts"

"wand"

"gryffindor"

"slytherin"

"patronum"

"dementor"

"hippogriff"

"horcrux"

"broomstick"

"dumbledore"

"voldemort"

"draco"

"invisibility"

These words were chosen to not only make the game entertaining but also to immerse players in the magical universe. The word list is easily extensible, allowing for future additions like new characters, spells, magical objects, or creatures, making the game more challenging and dynamic over time.

🧾 How the Code Works

The project is organized into functions, which keeps the code modular, readable, and reusable. Key components include:

main(): Controls the main game loop, manages attempts, validates user input, updates the visible word, and handles image updates. It ensures smooth gameplay by integrating terminal interaction and visual feedback.

choose_word(words): Randomly selects a word from the provided list, guaranteeing a different challenge each time the game is played.

update_hidden_word(chosen_word, hidden_word, letter): Updates the hidden word display whenever a correct letter is guessed.

make_guess(...): Processes each letter guessed by the player, updating both the word display and the attempt counter.

atualiza_imagem(imagem_nome): Copies the corresponding image to jogo.png to visually reflect the current game state.

abrir_imagem_jogo(): Opens the initial image in VS Code only once, ensuring the player sees the starting screen before guessing begins.

Input validation ensures only single alphabetical characters are accepted. Already guessed letters are tracked to prevent repetition, improving both gameplay flow and user experience.

▶️ How to Play

Ensure Python 3.x is installed on your computer.

Run the project.py file in a terminal or Python editor.

The hidden word will be displayed as a series of dashes (e.g., --- for a 3-letter word).

Enter one letter at a time.

Invalid entries (numbers, symbols, multiple letters) are rejected.

Previously guessed letters are displayed to avoid repetition.

After each guess, the terminal and jogo.png image will update to reflect progress.

You have six chances to guess incorrectly. Each wrong guess updates the hangman image sequentially:

First incorrect guess → 1.png

Second → 2.png
…
Sixth → 6.png (last chance before losing)

Correct guesses reveal letters in the word.

If the word is fully guessed, the victory screen (venceu.png) is displayed, along with the message:
Congratulations! 🎉 You guessed the word: 'RON'

If all attempts are used, the last hangman image is shown with the message:
You lost. 💀 The word was: 'RON'

💡 Tip: The game is case-insensitive, so entering H or h produces the same result. Enjoy the combination of terminal gameplay and visual storytelling.

Example Gameplay:

> Example:
> Suppose the word to guess is ron.
> The initial message will be: word: ---
> If you type the letter o, it will display: word: -o-.
> The game continues until you guess all letters correctly or make 5 mistakes.

<img width="494" height="619" alt="image" src="https://github.com/user-attachments/assets/c2f1bd3b-2dbf-4b44-936c-291765419033" />



📷 Visual Flow of the Game

The game uses images to make the experience more engaging:

Start of the game: inicio.png

Displays a welcome screen in VS Code with instructions.

First guess: forca.png

Shows the initial hangman state after the player starts guessing.

Incorrect attempts: 1.png → 6.png

Each wrong guess updates the hangman image, visually representing progress toward losing.

Victory: venceu.png

Displayed when the player successfully guesses all letters.

Defeat: 6.png (last attempt)

Shows the final hangman image along with the correct word revealed.

This flow ensures the game is interactive, dynamic, and visually engaging, going beyond the traditional text-only hangman.

💻 Technologies Used

Python 3.x

Terminal/Console for input and output

Native random library for word selection

Native os and shutil libraries for file and image manipulation

time library for delays and pacing

The project demonstrates the integration of multiple Python libraries to enhance gameplay while keeping dependencies minimal.

🎯 Learning Objectives

Apply programming logic, loops, and conditional statements

Work with lists, strings, and functions

Handle file operations for dynamic visual feedback

Implement input validation and state tracking

Create an interactive, terminal-based, and visually engaging project

Practice modularity and good code organization

Enhance problem-solving skills through gameplay logic

This project illustrates how a simple game concept can be expanded with additional features like images, input validation, and gameplay feedback, making it both educational and fun.
