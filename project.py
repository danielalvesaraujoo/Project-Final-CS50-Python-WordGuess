import random
import os
import shutil
import time

JOGO_IMG = "images/jogo.png"  # Caminho fixo da imagem principal

def main():

    # Limpa o jogo.png ao iniciar o jogo
    if os.path.exists(JOGO_IMG):
        os.remove(JOGO_IMG)

    # Copia inicio.png para jogo.png e abre no VS Code
    caminho_inicio = "images/inicio.png"
    if os.path.exists(caminho_inicio):
        shutil.copy(caminho_inicio, JOGO_IMG)
        abrir_imagem_jogo()   # abre só uma vez no VS Code
    else:
        #Imagem de início não encontrada
        print(f"Start image not found: {caminho_inicio}")

    palavras = [
        'harry', 'hermione', 'ron', 'dumbledore', 'voldemort', 'draco', 'patronum',
        'hogwarts', 'dementor', 'hippogriff', 'horcrux', 'invisibility', 'wand', 'broomstick'
    ]

    palavra_sorteada = escolher_palavra(palavras)
    palavra_escondida = '-' * len(palavra_sorteada)
    letras_adivinhadas = []
    letras_digitadas = []
    erros = 0
    max_tentativas = 6

    print('Welcome to the Hangman game - Harry Potter Edition!\n')

    while True:
        print(f'\nWord: {" ".join(palavra_escondida)}')
        print(f'[Word length: {len(palavra_sorteada)} letters]')
        print(f'Used letters: {", ".join(letras_digitadas)}')

        letra = input('Guess a letter: ').lower()

        if erros == 0:
            atualiza_imagem("forca.png")

        if not letra.isalpha() or len(letra) != 1:
            print('Please enter a single alphabetical letter.')
            continue

        if letra in letras_digitadas:
            print('You have already typed that letter. Try another one.')
            continue

        letras_digitadas.append(letra)

        palavra_escondida, letras_adivinhadas, tentativa_perdida = jogada(
            letras_adivinhadas, letra, palavra_sorteada, palavra_escondida
        )

        if tentativa_perdida:
            erros += 1
            atualiza_imagem(f"{erros}.png")
            print(f'Letter not found. You have {max_tentativas - erros} more {"tries" if max_tentativas > 1 else "try"}.')

        if palavra_escondida == palavra_sorteada:
            atualiza_imagem("venceu.png")
            print(f'\nCongratulations! 🎉 You guessed the word: "{palavra_sorteada.upper()}"')
            break
        elif erros == max_tentativas:
            atualiza_imagem(f"{erros}.png")  # Último erro
            print(f'\nYou lost. 💀 The word was: "{palavra_sorteada.upper()}"')
            break

# Apenas sobrescreve jogo.png (não reabre a aba no VS Code)
def atualiza_imagem(imagem_nome):
    caminho_origem = f"images/{imagem_nome}"
    if os.path.exists(caminho_origem):
        shutil.copy(caminho_origem, JOGO_IMG)
    else:
        #Imagem não encontrada:
        print(f"Image not found: {caminho_origem}")
    time.sleep(0.2)

# Abre a primeira vez dentro do VS Code
imagem_aberta_global = False
def abrir_imagem_jogo():
    global imagem_aberta_global
    if not imagem_aberta_global:
        os.system(f'code "{JOGO_IMG}"')
        imagem_aberta_global = True
        time.sleep(1)  # tempo pro VS Code abrir a aba

def escolher_palavra(palavras):
    return random.choice(palavras)

def atualizar_palavra_escondida(palavra_sorteada, palavra_escondida, letra):
    nova_palavra = []
    for i in range(len(palavra_sorteada)):
        if palavra_sorteada[i] == letra:
            nova_palavra.append(letra)
        else:
            nova_palavra.append(palavra_escondida[i])
    return ''.join(nova_palavra)

def jogada(letras_adivinhadas, letra, palavra_sorteada, palavra_escondida):
    letras_adivinhadas.append(letra)
    if letra in palavra_sorteada:
        nova_palavra_escondida = atualizar_palavra_escondida(
            palavra_sorteada, palavra_escondida, letra
        )
        return nova_palavra_escondida, letras_adivinhadas, False
    else:
        return palavra_escondida, letras_adivinhadas, True

if __name__ == "__main__":
    main()
