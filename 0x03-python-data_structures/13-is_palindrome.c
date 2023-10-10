#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*is_palindrome - identify if a syngle linked list is palindrome
*@head: head of listint_t
*Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *mid_mode;
	listint_t *second_half, *prev, *next;
	int is_palindrome = 1;

	slow = fast = prev_slow = *head;
	mid_mode = NULL;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			mid_mode = slow;
			slow = slow->next;
		}
		second_half = slow;
		prev_slow->next = NULL;
		prev = NULL;
		next = NULL;
		
		while (second_half != NULL)
		{
			next = second_half->next;
			second_half->next = prev;
			prev = second_half;
			second_half = next;
		}

		while (*head != NULL && second_half != NULL)
		{
			if ((*head)->n != second_half->n)
			{
				is_palindrome = 0;
				break;
			}
			*head = (*head)->next;
			second_half = second_half->next;
		}

	prev = NULL;
	while (prev != NULL)
	{
		next = prev->next;
		free(prev);
		prev = next;
	}

	if (mid_mode != NULL)
	{
		prev_slow->next = mid_mode;
		mid_mode->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}
}
	return is_palindrome;
}

