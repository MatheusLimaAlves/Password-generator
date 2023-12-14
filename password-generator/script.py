import random
import string

# Função geradora de senha.
def gerador_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Função para entrada do usuário.
def receber_tamanho_senha():
    while True:
        tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
        
        if tamanho_senha < 6:
            print('O número de caracteres desejado é muito baixo! Digite novamente.')
        else:
            senha_gerada = gerador_senha(tamanho_senha)
            print("Senha gerada:", senha_gerada)
            break  # Sai do loop se o tamanho da senha for válido

# Chama a função para receber o tamanho da senha.
receber_tamanho_senha()

#zeedh