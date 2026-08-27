#include <stdio.h>

int main()
{
    int age;

    printf("Digite sua idade: ");
    scanf("%d", &age);

    if (age >= 18)
    {
    printf("Adulto\n");
    }

    else if (age > 60){
        printf("Idoso\n");
        }

    else if (age < 18){
        printf("Menor de idade\n");
        }

    return 0;
}
