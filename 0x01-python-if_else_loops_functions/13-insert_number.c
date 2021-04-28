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
	listint_t *head_tmp, *new_node, *save;

	head_tmp = *head;
	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	while (head_tmp != NULL)
	{
		if ((head_tmp->next != NULL) && (number <= (head_tmp->next)->n))
		{
			save = head_tmp->next;
			break;
		}
		head_tmp = head_tmp->next;
	}
	head_tmp->next = new_node;
	new_node->n = number;
	new_node->next = save;
	return (new_node);
}
