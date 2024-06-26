#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void compute_LSP_array(const char *pattern, int pattern_length, int *LSP)
{
    int len = 0;
    LSP[0] = 0;
    int i = 1;

    while (i < pattern_length)
    {
        if (pattern[i] == pattern[len])
        {
            len++;
            LSP[i++] = len;
        }
        else
        {
            if (len != 0)
            {
                len = LSP[len - 1];
            }
            else
            {
                LSP[i++] = 0;
            }
        }
    }
}

int search_pattern(char *text, char *pattern, int expected_text_len, int expected_pattern_len)
{
    int text_length = (int)strnlen(text, expected_text_len);
    int pattern_length = (int)strnlen(pattern, expected_pattern_len);

    int *LSP = (int *)malloc(pattern_length * sizeof(int));
    compute_LSP_array(pattern, pattern_length, LSP);

    int i = 0;
    int j = 0;

    while (i < text_length)
    {
        if (pattern[j] == text[i])
        {
            i++;
            j++;
        }

        if (j == pattern_length)
        {
            free(LSP);
            return i - j;
        }

        if (i < text_length && pattern[j] != text[i])
        {
            if (j != 0)
            {
                j = LSP[j - 1];
            }
            else
            {
                i++;
            }
        }
    }

    free(LSP);
    return -1;
}

int main()
{
    char text[] = "CAABCAAABAACAADAABAAABAA";
    char pattern[] = "AABAA";

    int text_len = 25;
    int pattern_len = 5;

    int index = search_pattern(text, pattern, text_len, pattern_len);

    if (index != -1)
    {
        printf("Pattern found at index %d\n", index);
    }
    else
    {
        printf("Pattern not found\n");
    }

    return 0;
}
