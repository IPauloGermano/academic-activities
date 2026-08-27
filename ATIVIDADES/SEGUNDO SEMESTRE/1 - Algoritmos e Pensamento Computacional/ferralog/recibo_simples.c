#include <stdio.h>
#include <stdlib.h>

int main()
{
    char nome_ferramenta[50];
    int codigo_qr;
    float valor_compra;

    printf("--- SISTEMA FERRALOG ---\n");

    printf("Nome da ferramenta: ");
    scanf(" %[^\n]", nome_ferramenta);

    printf("Codigo QR: ");
    scanf("%d", &codigo_qr);

    printf("Valor da compra: ");
    scanf("%f", &valor_compra);

    system("cls");

    printf("--- RECIBO FERRAMENTA ---\n");

    if (valor_compra < 0)
    {
        printf("Valor da compra invalido\n");
    }

    else
    {
        printf("Nome da ferramenta: %s\n", nome_ferramenta);
        printf("Codigo QR: %d\n", codigo_qr);
        printf("Valor da compra: R$ %.2f\n", valor_compra);
    }

    return 0;
}
