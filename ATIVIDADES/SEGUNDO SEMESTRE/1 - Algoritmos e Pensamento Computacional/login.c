#include <stdio.h>


int main() {
    int senha = 1234; // exemplo de senha fixa
    int contador = 0;

    while (contador < 3) {


        printf("Digite seu nome de usuario: ");
        char username[50];
        scanf("%49s", username);
        printf("Digite sua senha: ");
        char password[50];
        scanf("%49s", password);
        if (atoi(password) != senha){
            contador++;
        }
        else {
            printf("Login bem-sucedido! Bem-vindo, %s!\n", username);
            break;
        }
    }

    return 0;

}

// como rodar no terminal:
// 1. Salve o código em um arquivo chamado login.c
// 2. Abra o terminal e navegue até o diretório onde o arquivo está salvo
// 3. Compile o código usando o comando: gcc login.c -o login
// 4. Execute o programa usando o comando: ./login
