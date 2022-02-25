#include <stdio.h>
#include <stdlib.h>

#include "nontailed-singly-linked-list.h"

SinglyLinkedList *initList()
{
  SinglyLinkedList *linkedList = (SinglyLinkedList *)malloc(sizeof(SinglyLinkedList));
  linkedList->length = 0;
  linkedList->head = NULL;

  return linkedList;
}

int isEmpty(SinglyLinkedList *list)
{
  if (list->length)
    return 0;
  else
    return 1;
}

int at(SinglyLinkedList *list, int index)
{
  LinkedListNode *node = list->head;
  if (index < 0 || index > list->length - 1)
    exit(EXIT_FAILURE);
  for (int i = 0; i < index; i++)
    node = node->next;
  return node->data;
}

void pushFront(SinglyLinkedList *list, int data)
{
  LinkedListNode *newNode = (LinkedListNode *)malloc(sizeof(LinkedListNode));
  newNode->data = data;
  newNode->next = list->head;
  list->head = newNode;
  list->length++;
}

void popFront(SinglyLinkedList *list)
{
  LinkedListNode *node = list->head;

  list->head = list->head->next;
  free(node);
  list->length--;
}

void pushBack(SinglyLinkedList *list, int data)
{
  LinkedListNode *newNode = (LinkedListNode *)malloc(sizeof(LinkedListNode));
  newNode->data = data;
  newNode->next = NULL;

  LinkedListNode *node = list->head;
  for (int i = 0; i < list->length - 1; i++)
    node = node->next;

  node->next = newNode;
  list->length++;
}

void popBack(SinglyLinkedList *list)
{
  LinkedListNode *prev = list->head;
  LinkedListNode *node;
  for (int i = 0; i < list->length - 2; i++)
    prev = prev->next;

  node = prev->next;
  prev->next = NULL;
  free(node);
  list->length--;
}

int front(SinglyLinkedList *list)
{
  return list->head->data;
}

int back(SinglyLinkedList *list)
{
  LinkedListNode *node = list->head;
  for (int i = 0; i < list->length - 1; i++)
    node = node->next;
  return node->data;
}

void insert(SinglyLinkedList *list, int data, int index)
{
  if (index < 0 || index > list->length - 1)
    exit(EXIT_FAILURE);

  LinkedListNode *newNode = (LinkedListNode *)malloc(sizeof(LinkedListNode));
  newNode->data = data;
  newNode->next = NULL;

  LinkedListNode *prev = list->head;
  LinkedListNode *node;
  for (int i = 0; i < index - 1; i++)
    prev = prev->next;

  node = prev->next;
  prev->next = newNode;
  newNode->next = node;
  list->length++;
}

void printList(SinglyLinkedList *list)
{
  printf("Length: %d\n", list->length);
  if (list->length == 0)
    printf("List is empty\n");
  else
    for (LinkedListNode *l = list->head; l != NULL; l = l->next)
      printf("%d ", l->data);

  printf("\n");
}
