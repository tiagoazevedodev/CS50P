#include <cs50.h>
#include <stdio.h>
int main(void)

{
    int counter = 0;
    while (counter < 5)  se quiser modificar a quantidade de `meows` apenas troque o while (counter < x)
    {
        printf("meow\n");
        counter = counter +1;
    }

}
infinite loop: you need to use the lib <stdbool.h> (included in <cs50.h>)
{
    while(true) \\ while(1)
    {
        printf("meow\n");
    }

}

