#include "lists.h"

/**
  * check_cycles - check for cycles in a linked list
  * @head: the first elem of the list
  * Return: 1 if cycle found 0 otherwise
  **/
int	check_cycle(listint_t *head)
{
	listint_t	*node;
	listint_t	*node2;

	if (!head)
		return (0);
	node = head;
	node2 = head;
	while (node2 && node2->next)
	{
		node = node->next;
		node2 = node2->next->next;
		if (node == node2)
			return (1);
	}
	return (0);
}
