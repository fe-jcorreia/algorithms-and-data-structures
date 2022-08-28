#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "vector.h"

void run_all_tests()
{
  test_initVector();
  test_push();
  test_empty();
  test_pop();
}

void test_initVector()
{
  Vector *v = initVector();

  int length = v->length;
  int capacity = v->capacity;

  assert(capacity == 8);
  assert(length == 0);

  destroyVector(v);
  printf("Test initVector: OK\n");
}

void test_push()
{
  Vector *v = initVector();
  Tuple a = {12, 0};
  Tuple b = {54, 1};

  push(v, a);
  push(v, b);

  int new_len = v->length;
  int first_element = (v->array)->data;
  int second_element = (v->array + 1)->data;

  assert(new_len == 2);
  assert(first_element == 12);
  assert(second_element == 54);

  destroyVector(v);
  printf("Test push: OK\n");
}

void test_empty()
{
  Vector *v = initVector();
  int empty = is_empty(v);
  assert(empty == 1);

  Tuple a = {43, 1};

  push(v, a);
  empty = is_empty(v);
  assert(empty == 0);

  destroyVector(v);

  printf("Test empty: OK\n");
}

void test_pop()
{
  Vector *v = initVector();
  int size;
  Tuple a = {43, 1};
  Tuple b = {45, 3};
  push(v, a);
  push(v, b);

  size = v->length;
  assert(size == 2);

  pop(v);

  size = v->length;
  assert(size == 1);

  destroyVector(v);

  printf("Test pop: OK\n");
}
