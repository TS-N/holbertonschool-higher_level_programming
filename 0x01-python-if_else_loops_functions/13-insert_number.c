#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the address of the head of the list
 * @number: the number to add into the list
 * Return: a pointer to the newly created node or NULL
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t	*new;
	listint_t	*node;
	listint_t	*prev = 0;

	if (!head)
		return (0);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (0);
	new->n = number;
	new->next = 0;
	node = *head;
	if (!*head)
	{
		*head = new;
		return (new);
	}
	while (node->next)
	{
		if (node->next->n > number)
		{
			prev = node->next;
			node->next = new;
			new->next = prev;
			return (new);
		}
		prev = node;
		node = node->next;
	}
	if (node->n > number)
	{
		new->next = node;
		if (!prev)
			*head = new;
		else
			prev->next = new;
	}
	else
		node->next = new;
	return (new);
}
