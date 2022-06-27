#include "lists.h"

/**
 * check_cycle - how fast or slow is the cycle
 * @list - pointer to lists head
 * Return: 0 if no cycle 1 if theres cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL)
		return (0);
	fast = list;
	slow = list;

	while (fast->next != NULL fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			slow = list;

			while (slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}
			return (1);
		}
	}
	return (0);
}

