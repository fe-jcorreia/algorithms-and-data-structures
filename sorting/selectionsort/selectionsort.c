#include <stdio.h>
#include <stdlib.h>

#include "selectionsort.h"

void selectionsort(Vector *v)
{
  int len = 0;
  while (len != v->length)
  {
    int min_index = len;
    for (int key = len; key < v->length - 1; key++)
      if (v->array[min_index] > v->array[key + 1])
        min_index = key + 1;

    int aux = v->array[len];
    v->array[len] = v->array[min_index];
    v->array[min_index] = aux;

    len++;
  }
}
