#include <stdio.h>
#include <stdlib.h>

#include "stack.h"
#include "./linked-list/nontailed-singly-linked-list.h"

Stack *initStack()
{
  Stack *s = (Stack *)malloc(sizeof(Stack));
  s->length = 0;
  s->list = initList();

  return s;
}

void push(Stack *s, int value)
{
  pushFront(s->list, value);
  s->length++;
}

int pop(Stack *s)
{
  if (isStackEmpty(s))
    return -1;

  int value = s->list->head->data;
  popFront(s->list);
  s->length--;
  return value;
}

int isStackEmpty(Stack *s)
{
  return s->length == 0;
}

int top(Stack *s)
{
  if (isStackEmpty(s))
    return -1;

  return s->list->head->data;
}

void destroyStack(Stack *s)
{
  destroyList(s->list);
  free(s);
}

void printStack(Stack *s)
{
  printList(s->list);
}
