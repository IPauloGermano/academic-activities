#include <stdio.h>

int main() {

    int opcao;

    printf("Menu:\n");
    printf("1. Novo Jogo\n");
    printf("2. Carregar Jogo\n");
    printf("3. Sair\n");
    printf("Escolha uma opcao: ");
    scanf("%d", &opcao);

    while (1) {
        switch (opcao) {

        case 1:
            printf("Iniciando um novo jogo...\n");
            break;

        case 2:
            printf("Carregando jogo salvo...\n");
            break;
        case 3:
            printf("Saindo do jogo...\n");
            return 0;

        default:
            printf("Opcao invalida. Tente novamente.\n");
            break;
        }
    }
    return 0;
}
