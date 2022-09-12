#include <stdio.h>
#include <stdlib.h>

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
