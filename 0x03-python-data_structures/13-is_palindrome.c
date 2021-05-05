#include "lists.h"

int _compare_extreme_nodes(listint_t **head, listint_t *tail)
{
    int result;

    if (!tail)
        return (1);

    result = _compare_extreme_nodes(head, tail->next);
    result = ((*head)->n == tail->n);
    *head = (*head)->next;

    return(result);
}


int is_palindrome(listint_t **head)
{
    if (!head)
        return (0);
    return (_compare_extreme_nodes(head, *head));
}
