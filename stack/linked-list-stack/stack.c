#include <stdio.h>
#include <stdlib.h>

#include "stack.h"
#include "../../linked-list/nontailed-singly-linked-list/nontailed-singly-linked-list.h"

Stack *initStack()
{
  Stack *s = (Stack *)malloc(sizeof(Stack));
  s->length = 0;
  s->list = initList();

  return s;
}

void push(Stack *s, int value)
{
}

int pop(Stack *s)
{
}

int isStackEmpty(Stack *s)
{
}

int top(Stack *s)
{
}

void destroyStack(Stack *s)
{
  destroyList(s->list);
  free(s);
}

void printStack(Stack *s)
{
}
