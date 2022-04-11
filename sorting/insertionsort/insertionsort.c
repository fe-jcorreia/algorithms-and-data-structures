#include <stdio.h>
#include <stdlib.h>

#include "insertionsort.h"

void insertionsort(Vector *v)
{
  for (int i = 1; i < v->length; i++)
  {
    int key = i;
    int aux = v->array[key];
    while (key != 0 && v->array[key - 1] > v->array[key])
    {
      v->array[key] = v->array[key - 1];
      v->array[key - 1] = aux;
      key--;
    }
  }
}
