// 20. Valid Parentheses

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define btoa(x) ((x) ? "true" : "false")

struct Node
{
    char data;
    struct Node *next;
};

struct Node *TOP = NULL;

int push(char element)
{
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = element;
    new_node->next = TOP;
    TOP = new_node;

    return 0;
}

char pop()
{
    struct Node *temp = TOP;
    TOP = TOP->next;
    char popped = temp->data;
    free(temp);

    return popped;
}

bool isValid(char *s)
{
    int i = 0;
    char ch;

    while (s[i] != '\0')
    {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
        {
            push(s[i]);
        }
        else
        {
            if (TOP == NULL)
            {
                return false;
            }

            ch = pop();
            if (s[i] == ')' && ch != '(')
            {
                return false;
            }

            if (s[i] == '}' && ch != '{')
            {
                return false;
            }

            if (s[i] == ']' && ch != '[')
            {
                return false;
            }
        }
        i++;
    }

    if (TOP == NULL)
    {
        return true;
    }

    return false;
}

int main()
{
    char s[] = "()";
    bool valid = isValid(s);
    printf("%s\n", btoa(valid));

    return 0;
}
