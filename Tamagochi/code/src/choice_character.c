#include <stdio.h>
#include <stdlib.h>

#include "choice_anime.h"

int choice_character(int choose_a)
{
    if (choose_a == 1)
    {
        // Define the choice's variable
        int choose_c;
        // Characters list
        printf("1. Naruto\n");
        printf("2. Hinata\n");
        printf("3. Neji\n");
        printf("Please choose your anime : ");
        // Input for choice
        scanf("%d", &choose_c);
    }
}