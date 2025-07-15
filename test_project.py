import pytest
from project import escolher_palavra, atualizar_palavra_escondida, jogada

def test_escolher_palavra():
    palavras = ['harry', 'ron', 'hermione']
    palavra = escolher_palavra(palavras)
    assert palavra in palavras

def test_atualizar_palavra_escondida():
    palavra = 'ron'
    escondida = '---'
    letra = 'o'
    resultado = atualizar_palavra_escondida(palavra, escondida, letra)
    assert resultado == '-o-'

    escondida = resultado
    letra = 'r'
    resultado = atualizar_palavra_escondida(palavra, escondida, letra)
    assert resultado == 'ro-'
    resultado = atualizar_palavra_escondida(palavra, resultado, 'n')
    assert resultado == 'ron'

def test_jogada():
    palavra = 'ron'
    escondida = '---'
    letras_adivinhadas = []
    letra = 'r'
    nova_escondida, novas_adivinhadas, tentativa_perdida = jogada(letras_adivinhadas, letra, palavra, escondida)
    assert nova_escondida == 'r--'
    assert 'r' in novas_adivinhadas
    assert tentativa_perdida is False

    palavra = 'ron'
    escondida = '---'
    letras_adivinhadas = []
    letra = 'z'
    nova_escondida, novas_adivinhadas, tentativa_perdida = jogada(letras_adivinhadas, letra, palavra, escondida)
    assert nova_escondida == escondida
    assert 'z' in novas_adivinhadas
    assert tentativa_perdida is True
