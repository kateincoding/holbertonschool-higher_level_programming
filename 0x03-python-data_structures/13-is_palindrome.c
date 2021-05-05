#include "lists.h"

/**
 * _compare_extreme_nodes - function that use a recursion to check palindromic
 * @head: head of linked list
 * @tail: the node that will be the tail of a singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int _compare_extreme_nodes(listint_t **head, listint_t *tail)
{
	int result;

	if (!tail)
		return (1);

	result = _compare_extreme_nodes(head, tail->next);
	if (result == 0)
		return (0);
	result = ((*head)->n == tail->n);
	*head = (*head)->next;

	return (result);
}

/**
 * is_palindrome - is palindrome a simply linked list without using a while
 *
 * @head: head of linked list
 * Return: call another function to call the last node in less time
 * 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (_compare_extreme_nodes(head, *head));
}
