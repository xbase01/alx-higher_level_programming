#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome_rec - check whether a singly linked list is a palindrome
 *
 * @left: pointer to the head node
 * @right: the head node
 *
 * Return: 1 if it's a palindrome, otherwise 0 (an empty list is considered
 * to be a palindrome)
 *
 */
int is_palindrome_rec(listint_t **left, listint_t *right)
{
int check1, check2;

if (right == NULL)
return (1);

check1 = is_palindrome_rec(left, right->next);
if (check1 == 0)
return (0);

check2 = ((*left)->n == right->n);
*left = (*left)->next;

return (check2);
}

/**
 * is_palindrome - check whether a singly linked list is a palindrome
 *
 * @head: pointer to the head node
 *
 * Return: 1 if it's a palindrome, otherwise 0 (an empty list is considered
 * to be a palindrome)
 *
 */
int is_palindrome(listint_t **head)
{
listint_t *current = *head;

if (current == NULL)
return (1);
return (is_palindrome_rec(&current, current));
}
