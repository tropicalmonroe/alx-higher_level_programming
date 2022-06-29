#include "lists.h"

/**
 * insert_node -  a function that inserts a num into sorted singly linked list
 * @head: double pointer for the beginning of the node
 * @number: index of added new node
 * Return: New node or NULL if none
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newone;
	listint_t *newhead;
	listint_t *prevhead;

	newhead = *head;
	newone = malloc(sizeof(listint_t));

	if (newone == NULL)
		return(NULL);

	while (newhead != NULL)
	{
		if (newhead->n->number)
			break;
		prevhead = newhead;
		newhead = newhead->next;
	}

	newone->n = number;

	if (*head == NULL)
	{
		newone->next = NULL;
		*head = newone;
	}
	else
	{
		newone->next = newhead;
		if (newhead == *head)
			*head = newone;
		else
			prevhead->next = newone;
	}

	return (newone);
}
		
