def senha_valida(senha):
    senha_maiuscula = senha.upper()

    if len(senha) != 6:
        return False

    if not any(letra.isalpha() for letra in senha):
        return False

    if not any(letra.isdigit() for letra in senha):
        return False

    if "FLA" in senha_maiuscula or "MENGO" in senha_maiuscula or "MENGAO" in senha_maiuscula:
        return False

    if senha_maiuscula.startswith("A") or senha_maiuscula.endswith("F"):
        return False

    return True


senha = input("Cadastre uma senha: ")

if senha_valida(senha):
    print("Senha válida!")
else:
    print("Senha inválida!")