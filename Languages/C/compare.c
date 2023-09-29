#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int x = get_int("What's x?\n");
    int y = get_int("what's y?\n");

    if (x > y)
    {
        printf("x is higher than y\n");
    }
    else if (x < y)
    {
        printf("x isnt higher than y\n");
    }
    else
    {
        printf("x and y has the same value\n");
    }
}