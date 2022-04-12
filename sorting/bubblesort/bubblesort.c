#include <stdio.h>
#include <stdlib.h>

#include "bubblesort.h"

void bubblesort(Vector *v)
{
  int len = v->length;
  while (len != 0)
  {
    for (int key = 0; key < len - 1; key++)
      if (v->array[key] > v->array[key + 1])
      {
        int aux = v->array[key];
        v->array[key] = v->array[key + 1];
        v->array[key + 1] = aux;
      }
    len--;
  }
}
