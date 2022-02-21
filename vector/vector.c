#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "vector.h"

Vector *initVector()
{
  Vector *v = (Vector *)malloc(sizeof(Vector));
  int *arr = (int *)malloc(8 * sizeof(int));
  v->array = arr;
  v->length = 0;
  v->capacity = 8;

  return v;
}

int is_empty(Vector *v)
{
  if (v->length)
    return 0;
  else
    return 1;
}

int at(Vector *v, int index)
{
  if (index < 0 || index > v->length - 1)
    exit(EXIT_FAILURE);
  return *(v->array + index);
}

void edit(Vector *v, int index, int value)
{
  if (index < 0 || index > v->length - 1)
    exit(EXIT_FAILURE);
  *(v->array + index) = value;
}

void resize(Vector *v, int capacity)
{
  int *new_array = malloc(capacity * sizeof(int));
  for (int i = 0; i < v->length; i++)
    *(new_array + i) = *(v->array + i);
  free(v->array);
  v->array = new_array;
  v->capacity = capacity;
}

void push(Vector *v, int item)
{
  if (v->length == v->capacity)
    resize(v, v->length * 2);

  *(v->array + v->length) = item;
  v->length++;
}

void insert(Vector *v, int index, int item)
{
  if (v->length <= index || index < 0)
    exit(EXIT_FAILURE);

  if (v->length == v->capacity)
    resize(v, v->length * 2);

  for (int i = v->length; i > index; i--)
    *(v->array + i) = *(v->array + i - 1);

  *(v->array + index) = item;
  v->length++;
}

void prepend(Vector *v, int item)
{
  insert(v, 0, item);
}

void pop(Vector *v)
{
  v->length--;
  if (v->capacity / 4 >= v->length)
    resize(v, v->capacity / 2);
}

void deleteIndex(Vector *v, int index)
{
  if (index < 0 || index > v->length - 1)
    exit(EXIT_FAILURE);

  if (index == v->length - 1)
  {
    pop(v);
    return;
  }

  for (int i = index; i < v->length - 1; i++)
    *(v->array + i) = *(v->array + i + 1);

  v->length--;

  if (v->capacity / 4 >= v->length)
    resize(v, v->capacity / 2);
}

void removeItem(Vector *v, int item)
{
  for (int i = 0; i < v->length; i++)
    while (*(v->array + i) == item && i < v->length)
    {
      deleteIndex(v, i);
      if (v->length == 0)
        break;
    }
}

int find(Vector *v, int item)
{
  for (int i = 0; i < v->length; i++)
    if (*(v->array + i) == item)
      return i;

  return -1;
}

void destroyVector(Vector *v)
{
  free(v->array);
  free(v);
}

void printVector(Vector *v)
{
  printf("Length: %d\n", v->length);
  printf("Capacity: %d\n", v->capacity);

  for (int i = 0; i < v->length; i++)
    printf("%d ", *(v->array + i));

  printf("\n");
}

// ========================= tests ==================

void run_all_tests()
{
  test_initVector();
  test_push();
  test_resize();
  test_empty();
  test_at();
  test_edit();
  test_insert();
  test_prepend();
  test_pop();
  test_deleteIndex();
  test_removeItem();
  test_find();
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

  push(v, 12);
  push(v, 45);

  int new_len = v->length;
  int first_element = *(v->array);
  int second_element = *(v->array + 1);

  assert(new_len == 2);
  assert(first_element == 12);
  assert(second_element == 45);

  destroyVector(v);
  printf("Test push: OK\n");
}

void test_resize()
{
  Vector *v = initVector();
  int capacity = v->capacity;
  assert(capacity == 8);

  for (int i = 1; i <= 32; i++)
    push(v, i);

  capacity = v->capacity;
  assert(capacity == 32);

  for (int i = 1; i <= 24; i++)
    pop(v);

  capacity = v->capacity;
  assert(capacity == 16);

  destroyVector(v);

  printf("Test resize: OK\n");
}

void test_empty()
{
  Vector *v = initVector();
  int empty = is_empty(v);
  assert(empty == 1);

  push(v, 15);
  empty = is_empty(v);
  assert(empty == 0);

  destroyVector(v);

  printf("Test empty: OK\n");
}

void test_at()
{
  Vector *v = initVector();
  for (int i = 0; i < 10; i++)
    push(v, i);

  assert(at(v, 6) == 6);

  destroyVector(v);

  printf("Test at: OK\n");
}

void test_edit()
{
  Vector *v = initVector();

  push(v, 1);
  assert(at(v, 0) == 1);
  edit(v, 0, 2);
  assert(at(v, 0) == 2);

  destroyVector(v);

  printf("Test edit: OK\n");
}

void test_insert()
{
  Vector *v = initVector();
  for (int i = 0; i < 10; i++)
    push(v, i);

  insert(v, 3, 40);
  insert(v, v->length - 1, 50);

  assert(at(v, 3) == 40);
  assert(at(v, 10) == 50);

  destroyVector(v);

  printf("Test insert: OK\n");
}

void test_prepend()
{
  Vector *v = initVector();
  for (int i = 0; i < 10; i++)
    push(v, i);

  prepend(v, 16);
  assert(at(v, 0) == 16);
  assert(at(v, 1) == 0);

  destroyVector(v);

  printf("Test prepend: OK\n");
}

void test_pop()
{
  Vector *v = initVector();
  int size;
  for (int i = 0; i < 10; i++)
    push(v, i);

  size = v->length;
  assert(size == 10);

  for (int i = 0; i < 10; i++)
    pop(v);

  size = v->length;
  assert(size == 0);

  destroyVector(v);

  printf("Test pop: OK\n");
}

void test_deleteIndex()
{
  Vector *v = initVector();
  for (int i = 0; i < 10; i++)
    push(v, i);

  deleteIndex(v, 9);
  deleteIndex(v, 0);
  assert(at(v, 0) == 1);
  assert(at(v, 7) == 8);

  destroyVector(v);

  printf("Test deleteIndex: OK\n");
}

void test_removeItem()
{
  Vector *v = initVector();
  int size;
  push(v, 10);
  push(v, 3);
  push(v, 10);
  push(v, 10);
  push(v, 10);

  removeItem(v, 10);
  size = v->length;
  assert(size == 1);

  destroyVector(v);

  printf("Test removeItem: OK\n");
}

void test_find()
{
  Vector *v = initVector();
  push(v, 10);
  push(v, 3);
  push(v, 5);
  push(v, 10);
  push(v, 10);

  assert(find(v, 10) == 0);
  assert(find(v, 3) == 1);
  assert(find(v, 19) == -1);

  destroyVector(v);

  printf("Test find: OK\n");
}
