#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t	*new;
	listint_t	*node;
	listint_t	*buf;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (0);
	new->n = number;
	new->next = 0;
	if (!*head)
		*head = new;
	else
	{
		node = *head;
		while (node)
		{
			if (!node->next)
			{
				node->next = new;
				break;
			}
			else if (node->next->n > number)
			{
				buf = node->next;
				node->next = new;
				new->next = buf;
				break;
			}
			node = node->next;
		}
	}
	return (new);
}
