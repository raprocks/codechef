#include <stdio.h>

int main(int argc, char const *argv[])
{
    int input, power = 1, rev = 0, cur;
    scanf("%d", &input);
    while (input != 0)
    {
        cur = input % 10;
        rev = (rev * 10) + cur;
        power++;
        input /= 10;
        // printf("%d\n", rev);
    }
    printf("%d", rev);

    return 0;
}
