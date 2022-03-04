#include <stdio.h>
#include <assert.h>
#include "stack.h"

void run_all_tests()
{
  test_initStack();
  test_pushStack();
  test_popStack();
  test_isStackEmpty();
  test_top();
}

void test_initStack()
{
  Stack *s = initStack();

  assert(s->length == 0);

  printf("Test initQueue: OK\n");

  destroyStack(s);
}

void test_pushStack()
{
  Stack *s = initStack();

  pushStack(s, 5);
  pushStack(s, 10);
  pushStack(s, 20);
  assert(top(s) == 20);
  assert(s->length == 3);

  printf("Test pushStack: OK\n");

  destroyStack(s);
}

void test_popStack()
{
  Stack *s = initStack();

  pushStack(s, 5);
  pushStack(s, 10);
  pushStack(s, 20);
  assert(top(s) == 20);
  assert(popStack(s) == 20);
  assert(top(s) == 10);
  assert(popStack(s) == 10);
  popStack(s);
  assert(popStack(s) == -1);

  printf("Test popStack: OK\n");

  destroyStack(s);
}

void test_isStackEmpty()
{
  Stack *s = initStack();
  assert(isStackEmpty(s) == 1);

  pushStack(s, 5);
  pushStack(s, 10);
  pushStack(s, 20);
  assert(isStackEmpty(s) == 0);
  popStack(s);
  popStack(s);
  popStack(s);
  assert(isStackEmpty(s) == 1);

  printf("Test isStackEmpty: OK\n");

  destroyStack(s);
}

void test_top()
{
  Stack *s = initStack();
  assert(top(s) == -1);

  pushStack(s, 5);
  pushStack(s, 10);
  assert(top(s) == 10);

  printf("Test top: OK\n");

  destroyStack(s);
}