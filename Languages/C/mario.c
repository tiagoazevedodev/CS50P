#include <stdio.h>
#include <cs50.h>
int main(void)
{
    /*for (int i = 0; i<4; i++)
    {
        printf("?");
    }
    printf("\n");*/

    const int n = 3;
    for(int i =0; i<n; i++)
    {
        for (int j =0; j<n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
