#include <stdio.h>
#include <stdlib.h>

#include "vector.h"

Vector *initVector()
{
  Vector *v = (Vector *)malloc(sizeof(Vector));
  Tuple *arr = (Tuple *)malloc(8 * sizeof(Tuple));
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

void resize(Vector *v, int capacity)
{
  Tuple *new_array = malloc(capacity * sizeof(Tuple));
  for (int i = 0; i < v->length; i++)
    *(new_array + i) = *(v->array + i);
  free(v->array);
  v->array = new_array;
  v->capacity = capacity;
}

void push(Vector *v, Tuple item)
{
  if (v->length == v->capacity)
    resize(v, v->length * 2);

  *(v->array + v->length) = item;
  v->length++;
}

void pop(Vector *v)
{
  v->length--;
  if (v->capacity / 4 >= v->length)
    resize(v, v->capacity / 2);
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
    printf("(%d, %d)", (v->array + i)->data, (v->array + i)->index);

  printf("\n");
}
