#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *second_half, *prev = *head;
	listint_t *midnode = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{

		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;

			prev = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}
		second_half = slow;
		prev->next = NULL;
		reverse(&second_half);
		res = compareLists(*head, second_half);
		reverse(&second_half);
		if (midnode != NULL)
		{
			prev->next = midnode;
			midnode->next = second_half;
		}
		else
			prev->next = second_half;
	}
	return (res);
}
/**
 * reverse - Reverses a linked list
 * @head_ref: Pointer to the head of the list
 *
 * This function reverses the linked list by changing the next pointers of the
 * nodes. It uses three pointers: prev, current, and next. It iterates over the
 * list, changing the next pointer of the current node to point to the previous
 * node. The prev and current pointers are then moved one step forward (with
 * current moving to next and prev moving to current), and the process is
 * repeated until the end of the list is reached.
 */
void reverse(listint_t **head_ref)
{
	listint_t *prev   = NULL;
	listint_t *current = *head_ref;
	listint_t *next;

	while (current != NULL)
	{
		next  = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}
/**
 * compareLists - Compares two linked lists
 * @head1: Head of the first list
 * @head2: Head of the second list
 *
 * Return: 1 if the lists are identical, 0 otherwise
 *
 * This function compares two linked lists node by node. It uses two pointers,
 * temp1 and temp2, to traverse the lists.
 * If at any point the data in the nodes
 * pointed to by temp1 and temp2 are not equal, it returns 0. If it reaches the
 * end of both lists at the same time, it returns 1, indicating that the lists
 * are identical. If it reaches the end of one list
 * before the other,it returns
 * 0, indicating that the lists are not identical.
 */
int compareLists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}
