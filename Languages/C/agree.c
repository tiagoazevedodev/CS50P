#include <stdio.h>
#include <cs50.h>
/* "" USED ONLY FOR STRINGS.  \\\  ''USED ONLY FOR CHAR(CHARACTER)*/
int main(void)
{
    char c = get_char("do you agree?\n");
    if (c == 'y' || c == 'Y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'n'|| c == 'N')
    {
        printf("Refused.\n");
    }
    else
    {
        printf("Answer must be `y` or `n`.\n");
    }
}