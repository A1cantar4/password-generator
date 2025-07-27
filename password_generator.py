# Project: Password Generator

import random
import string

# Function with default parameters: all True and length = 12
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
    # If error, use 12.
    try:
        length = int(input("Digite o tamanho da senha (ex.: 12): ").strip()) # Added strip
    except ValueError:
        print("Tamanho inválido, usando 12.")
        length = 12

    # True only if input == "s"
    # for default, use only lower letters
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

# Start the app
if __name__ == "__main__":
    main()