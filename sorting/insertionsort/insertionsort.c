#include <stdio.h>
#include <stdlib.h>

#include "insertionsort.h"

void insertionsort(Vector *v)
{
  int n = v->length;

  for (int sorted_len = 1; sorted_len < n; sorted_len++)
  {
    int key = sorted_len;

    if (v->array[key] >= v->array[key - 1])
      continue;

    int aux = v->array[key];
    while (key != 0)
    {
      if (v->array[key - 1] > v->array[key])
      {
        v->array[key] = v->array[key - 1];
        v->array[key - 1] = aux;
        key--;
      }
      else
        break;
    }
  }
}
