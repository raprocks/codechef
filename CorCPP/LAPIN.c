#include <string.h>
#include <stdio.h>
int main(int argc, char const *argv[])
{
    char input[1000];
    int onehalfcount[26];
    int twohalfcount[26];
    int testCases, halfend, halfstart, lapin = 0;
    scanf("%d\n", &testCases);
    for (int i = 0; i < testCases; i++)
    {
        for (int i = 0; i < 26; i++)
        {
            onehalfcount[i] = 0;
            twohalfcount[i] = 0;
        }

        scanf("%[^\n]%*c", input);
        if ((strlen(input) % 2) == 0)
        {
            // printf("%s is equally dividable. Length is  %d\n", input, strlen(input));
            halfend = (strlen(input) / 2) - 1;
            halfstart = halfend + 1;
        }
        else
        {
            // printf("%s is not equally dividable. Length is %d\n", input, strlen(input));
            halfend = ((strlen(input) - 1) / 2) - 1;
            halfstart = halfend + 2;
        }
        // printf("First Half is :");
        for (int i = 0; i <= halfend; i++)
        {
            // printf("%d ", input[i] - 97);
            onehalfcount[input[i] - 97]++;
        }
        // printf("\nSecond Half is : ");
        for (int i = halfstart; i < strlen(input); i++)
        {
            // printf("%d ", input[i] - 97);
            twohalfcount[input[i] - 97]++;
        }
        // printf("\n");
        for (int i = 0; i < 26; i++)
        {
            if (onehalfcount[i]!=twohalfcount[i])
            {
                lapin = 0;
                    break;
            }
            lapin = 1;
        }
        
        if (lapin)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}
