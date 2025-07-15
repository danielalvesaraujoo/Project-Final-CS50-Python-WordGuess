import random

def main():
    palavras = ['harry', 'hermione', 'ron', 'dumbledore', 'voldemort', 'draco', 'patronum',
                'hogwarts', 'dementor', 'hippogriff', 'horcrux', 'invisibility', 'wand', 'broomstick']

    palavra_sorteada = escolher_palavra(palavras)
    palavra_escondida = '-' * len(palavra_sorteada)
    letras_adivinhadas = []
    letras_digitadas = []
    max_tentativas = 6

    print('Word Guess - Harry Potter Edition!\n')

    while True:
        print(f'\nWord: {" ".join(palavra_escondida)}')
        print(f'[Word length: {len(palavra_sorteada)} letters]')
        print(f'Used letters: {", ".join(letras_digitadas)}')

        letra = input('Guess a letter: ').lower()

        if not letra.isalpha() or len(letra) != 1:
            print('Please enter a single alphabetical letter.')
            continue

        if letra in letras_digitadas:
            print('You have already typed that letter. Try another one.')
            continue

        letras_digitadas.append(letra)

        palavra_escondida, letras_adivinhadas, tentativa_perdida = jogada(letras_adivinhadas, letra, palavra_sorteada, palavra_escondida)

        if tentativa_perdida:
            max_tentativas -= 1
            print(f'Letter not found. You have {max_tentativas} more {"tries" if max_tentativas > 1 else "try"}.')

        if palavra_escondida == palavra_sorteada:
            print(f'\nCongratulations! 🎉 You guessed the word: "{palavra_sorteada.upper()}"')
            break
        elif max_tentativas == 0:
            print(f'\nYou lost. 💀 The word was: "{palavra_sorteada.upper()}"')
            break

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
        nova_palavra_escondida = atualizar_palavra_escondida(palavra_sorteada, palavra_escondida, letra)
        return nova_palavra_escondida, letras_adivinhadas, False
    else:
        return palavra_escondida, letras_adivinhadas, True

if __name__ == "__main__":
    main()
