#include <stdio.h>
#include <stdlib.h>

int main() {
    int opcao_menu = 0;
    char nome_ferramenta[50];
    unsigned int codigo_qr = 0;
    float valor_compra = 0.0;
    int possui_garantia = 0;

    int producao[3][3] = {
        {120, 150, 100}, 
        {130, 140, 110}, 
        {160, 120, 140}  
    };
    int total_geral = 0;

    printf("==================================================\n");
    printf("          SISTEMA FERRALOG - INVENTARIO           \n");
    printf("==================================================\n");
    printf("[1] Cadastrar nova ferramenta\n");
    printf("[2] Consultar ferramenta\n");
    printf("[3] Relatorios (Painel de Producao)\n");
    printf("[4] Sair do sistema\n");
    printf("==================================================\n");
    printf("Digite a opcao desejada: ");

    scanf("%d", &opcao_menu);

    system("clear");

    switch (opcao_menu) {

        case 1:
            printf("--- MODULO DE CADASTRO ---\n");

            printf("Nome da ferramenta: ");
            scanf("%49s", nome_ferramenta);

            printf("Codigo QR: ");
            scanf("%u", &codigo_qr);

            printf("Valor da compra: R$ ");
            scanf("%f", &valor_compra);

            printf("Possui garantia? (1 para SIM, 0 para NAO): ");
            scanf("%d", &possui_garantia);

            system("clear"); 
            
            printf("--- RECIBO FERRALOG ---\n");
            printf("Ferramenta: %s\n", nome_ferramenta);
            printf("QR Code: %u\n", codigo_qr);
            printf("Valor: R$ %.2f\n", valor_compra);

            if (valor_compra > 1000.0 && possui_garantia == 0) {
                printf("STATUS: *** ALERTA DE ALTO RISCO FINANCEIRO ***\n");
                printf("Motivo: Equipamento de alto valor alocado sem cobertura de garantia.\n");
            } else {
                printf("STATUS: Cadastro em conformidade.\n");
            }

            break;

        case 2:
            printf("--- MODULO DE CONSULTA ---\n");
            printf("Aviso: O modulo de consulta de QR Code esta em desenvolvimento.\n");
            break;

        case 3:
            printf("--- MODULO DE RELATORIOS: PAINEL DE PRODUCAO ---\n\n");

            for (int i = 0; i < 3; i++) {
                printf("Maquina %d: ", i + 1);
                for (int j = 0; j < 3; j++) {
                    printf("[%d] ", producao[i][j]);
                    total_geral += producao[i][j]; // Soma as pecas produzidas
                }
                printf("\n");
            }

            printf("\n==================================================\n");
            printf("Total Geral da fabrica: %d pecas produzidas!\n", total_geral);
            printf("==================================================\n");
            break;

        case 4:
            printf("Desconectando do banco de dados...\n");
            printf("Saindo do sistema. Ate logo!\n");
            break;

        default:
            printf("ERRO: A opcao %d nao existe no menu.\n", opcao_menu);
            break;
    }

    return 0;
}
