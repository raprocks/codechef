#include <stdio.h>

int main()
{
    int input;
    while (1)
    {
        scanf("%d", &input);
        if (input==42){
            return 0;
        }
        printf("%d\n", input);
    }
}