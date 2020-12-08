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
