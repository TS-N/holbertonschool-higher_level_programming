#include "hash_tables.h"

/**
  * key_index - returns the table index based on the key
  * @key: the key string
  * @size: the size of the table
  * Return: the index in the hash table
  **/
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	return (hash_djb2(key) % size);
}
