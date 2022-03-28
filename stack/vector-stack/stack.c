#include <stdio.h>
#include <stdlib.h>

#include "stack.h"
#include "./vector/vector.h"

Stack *initStack()
{
  Stack *s = (Stack *)malloc(sizeof(Stack));
  s->length = 0;
  s->list = initVector();

  return s;
}

void pushStack(Stack *s, int value)
{
  push(s->list, value);
  s->length++;
}

int popStack(Stack *s)
{
  if (isStackEmpty(s))
    return -1;

  int value = at(s->list, s->length - 1);
  pop(s->list);
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

  return at(s->list, s->length - 1);
}

void destroyStack(Stack *s)
{
  destroyVector(s->list);
  free(s);
}

void printStack(Stack *s)
{
  printVector(s->list);
}
