#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts new node to a sorted linked list
 * @head: head of linked list
 * @number: value in linked list->n
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *head_tmp, *new_node, *next_node;

	head_tmp = *head;
	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (!head_tmp || head_tmp->n >= number)
	{
		new_node->next = head_tmp;
		*head = new_node;
		return (new_node);
	}

	next_node = head_tmp->next;
	while (head_tmp && next_node && (number >= next_node->n))
	{
		head_tmp = head_tmp->next;
		next_node = head_tmp->next;
	}
	head_tmp->next = new_node;
	new_node->next = next_node;
	return (new_node);
}
