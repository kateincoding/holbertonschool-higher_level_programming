#include "lists.h"
/**
 * check_cycle - function that detects if a linked list is a cycle
 * @list: linked list to evaluate
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *list_fast, *list_slow;

	if (!list)
		return (0);

	list_fast = list_slow = list;
	while (list_fast)
	{
		if (list_fast->next == NULL || (list_fast->next)->next == NULL)
			return (0);
		list_fast = (list_fast->next)->next;
		if (list_slow == list_fast)
			return (1);
		list_slow = list_slow->next;
	}
	return (0);
}
