#include "hash_tables.h"

/**
   * hash_table_create - creates an empty hash table and set it to zero
   * @size: the size of the table
   * Return: the newly created table
   **/
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t	*T;

	T = malloc(sizeof(hash_table_t));
	if (!T)
		return (NULL);
	T->array = malloc(sizeof(hash_node_t *) * size);
	if (T->array == NULL)
		return (NULL);
	T->array = memset(T->array, 0, sizeof(hash_node_t *) * size);
	T->size = size;
	return (T);
}
