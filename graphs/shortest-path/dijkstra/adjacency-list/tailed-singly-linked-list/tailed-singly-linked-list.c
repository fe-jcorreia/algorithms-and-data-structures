#include <stdio.h>
#include <stdlib.h>

#include "tailed-singly-linked-list.h"

SinglyLinkedList *initList()
{
  SinglyLinkedList *linkedList = (SinglyLinkedList *)malloc(sizeof(SinglyLinkedList));
  linkedList->length = 0;
  linkedList->head = NULL;
  linkedList->tail = NULL;

  return linkedList;
}

int isEmpty(SinglyLinkedList *list)
{
  if (list->length)
    return 0;
  else
    return 1;
}

int atOnList(SinglyLinkedList *list, int index)
{
  if (index < 0 || index > list->length - 1)
    exit(EXIT_FAILURE);

  if (index == list->length - 1)
    return list->tail->data;

  LinkedListNode *node = list->head;
  for (int i = 0; i < index; i++)
    node = node->next;
  return node->data;
}

void pushFront(SinglyLinkedList *list, int data, int weight)
{
  LinkedListNode *newNode = (LinkedListNode *)malloc(sizeof(LinkedListNode));
  newNode->data = data;
  newNode->weight = weight;
  newNode->next = list->head;
  list->head = newNode;

  if (list->length == 0)
    list->tail = list->head;

  list->length++;
}

void popFront(SinglyLinkedList *list)
{
  LinkedListNode *node = list->head;

  list->head = list->head->next;
  free(node);
  list->length--;
}

void pushBack(SinglyLinkedList *list, int data, int weight)
{
  LinkedListNode *newNode = (LinkedListNode *)malloc(sizeof(LinkedListNode));
  newNode->data = data;
  newNode->weight = weight;
  newNode->next = NULL;

  if (list->length == 0)
  {
    list->head = newNode;
    list->tail = newNode;
    list->length++;
    return;
  }

  list->tail->next = newNode;
  list->tail = newNode;
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
  list->tail = prev;
  free(node);
  list->length--;
}

int front(SinglyLinkedList *list)
{
  return list->head->data;
}

int back(SinglyLinkedList *list)
{
  return list->tail->data;
}

void insertOnList(SinglyLinkedList *list, int data, int weight, int index)
{
  if (index < 0 || index > list->length - 1)
    exit(EXIT_FAILURE);

  if (index == 0)
  {
    pushFront(list, data, weight);
    return;
  }

  LinkedListNode *newNode = (LinkedListNode *)malloc(sizeof(LinkedListNode));
  newNode->data = data;
  newNode->weight = weight;
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

void erase(SinglyLinkedList *list, int index)
{
  if (index < 0 || index > list->length - 1)
    exit(EXIT_FAILURE);

  if (index == 0)
  {
    popFront(list);
    return;
  }

  LinkedListNode *prev = list->head;
  LinkedListNode *node;
  for (int i = 0; i < index - 1; i++)
    prev = prev->next;

  node = prev->next;
  prev->next = node->next;
  if (list->tail == node)
    list->tail = prev;
  free(node);
  list->length--;
}

int valueNFromEnd(SinglyLinkedList *list, int index)
{
  return atOnList(list, list->length - 1 - index);
}

void reverse(SinglyLinkedList *list)
{
  LinkedListNode *prev = list->head;
  LinkedListNode *post = list->head->next->next;
  list->head = list->head->next;
  prev->next = NULL;
  list->tail = prev;

  for (int i = 0; i < list->length - 2; i++)
  {
    list->head->next = prev;
    prev = list->head;
    list->head = post;
    post = post->next;
  }
  list->head->next = prev;
}

void removeFirstValue(SinglyLinkedList *list, int value)
{
  LinkedListNode *node = list->head;
  for (int i = 0; i < list->length; i++)
  {
    if (node->data == value)
    {
      erase(list, i);
      break;
    }
    node = node->next;
  }
}

void destroyList(SinglyLinkedList *list)
{
  LinkedListNode *prev = list->head;
  for (int i = 0; i < list->length; i++)
  {
    list->head = list->head->next;
    free(prev);
    prev = list->head;
  }

  free(list);
}

void printList(SinglyLinkedList *list)
{
  printf("[");
  if (list->length == 0)
    printf("\n");
  else
    for (LinkedListNode *l = list->head; l != NULL; l = l->next)
      printf("%d ", l->data);
  printf("]");

  printf("\n");
}
