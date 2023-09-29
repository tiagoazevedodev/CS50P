#include <cs50.h>
#include <stdio.h>

int main (void);
{
    string name = get_string("whats your name? ");
    string last_name = get_string ("whats your last name? ");
    printf("hello, %s %s!\n", name, last_name);
}

