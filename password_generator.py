# Gerador de senhas aleatórias
# Possui true/false para tipos de caracteres
# Possui também except para erros de digitação

import random
import string

# Função com parametros TRUE por padrão e tamanho 12.
def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = list(string.ascii_lowercase)

    if use_uppercase:
        characters += list(string.ascii_uppercase)

    if use_digits:
        characters += list(string.digits)

    if use_symbols:
        characters += list("!@#$%^&*()-_=+[]{};:,.<>?")

    if not characters:
        raise ValueError("Nenhum conjunto de caracteres selecionado.")

    password = ''.join(random.choices(characters, k=length))

    return password

def main():
    print("=== Gerador de Senhas Aleatórias ===")

    try:
        length = int(input("Digite o tamanho da senha (ex.: 12): "))
    except ValueError:
        print("Tamanho inválido, usando 12.")
        length = 12

    use_uppercase = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == "s"
    use_digits = input("Incluir números? (s/n): ").strip().lower() == "s"
    use_symbols = input("Incluir símbolos? (s/n): ").strip().lower() == "s"

    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_digits=use_digits,
        use_symbols=use_symbols
    )

    print("\nSenha gerada:")
    print(password)

if __name__ == "__main__":
    main()