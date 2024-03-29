#include <stdio.h>
#include <assert.h>
#include "stack.h"

void run_all_tests()
{
  test_initStack();
  test_push();
  test_pop();
  test_isStackEmpty();
  test_top();
}

void test_initStack()
{
  Stack *s = initStack();

  assert(s->length == 0);
  assert(s->list->head == NULL);
  assert(s->list->length == 0);

  printf("Test initQueue: OK\n");

  destroyStack(s);
}

void test_push()
{
  Stack *s = initStack();

  push(s, 5);
  push(s, 10);
  push(s, 20);
  assert(s->list->head->data == 20);
  assert(s->length == 3);

  printf("Test push: OK\n");

  destroyStack(s);
}

void test_pop()
{
  Stack *s = initStack();

  push(s, 5);
  push(s, 10);
  push(s, 20);
  assert(s->list->head->data == 20);
  assert(pop(s) == 20);
  assert(s->list->head->data == 10);
  assert(pop(s) == 10);
  pop(s);
  assert(pop(s) == -1);

  printf("Test pop: OK\n");

  destroyStack(s);
}

void test_isStackEmpty()
{
  Stack *s = initStack();
  assert(isStackEmpty(s) == 1);

  push(s, 5);
  push(s, 10);
  push(s, 20);
  assert(isStackEmpty(s) == 0);
  pop(s);
  pop(s);
  pop(s);
  assert(isStackEmpty(s) == 1);

  printf("Test isStackEmpty: OK\n");

  destroyStack(s);
}

void test_top()
{
  Stack *s = initStack();
  assert(top(s) == -1);

  push(s, 5);
  push(s, 10);
  assert(top(s) == 10);

  printf("Test top: OK\n");

  destroyStack(s);
}