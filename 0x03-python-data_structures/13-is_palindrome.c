#include "lists.h"

/**
  * lllen - returns the len of the linked list
  * @head: the 1st elem of the ll
  * Return: the len
  **/
int	lllen(listint_t *head)
{
	int	l = 0;

	while (head)
	{
		++l;
		head = head->next;
	}
	return (l);
}

/**
  * get_node_at_index - get node in ll at index i
  * @head: 1st elem
  * @i: the index
  * Return: the elem
  **/
listint_t	*get_node_at_index(listint_t *head, int i)
{
	while (head && i > 0)
	{
		head = head->next;
		--i;
	}
	return (head);
}

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: the address of the first elem of the ll
  * Return: 0 if it's not a palindrome, 1 if it is
  **/
int is_palindrome(listint_t **head)
{
	int	l;
	int	i;

	if (!head || !*head)
		return (1);
	l = lllen(*head);
	i = 0;
	while (i < l / 2)
	{
		if (get_node_at_index(*head, i)->n != get_node_at_index(*head, l - 1 - i)->n)
		{
			return (0);
		}
		++i;
	}
	return (1);
}
