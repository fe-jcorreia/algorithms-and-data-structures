#include <stdio.h>
#include <stdlib.h>

#include "quicksort.h"

int select_pivot(int min, int max)
{
  return min + (rand() % (max - min + 1));
}

void swap(Vector *v, int i, int j)
{
  int aux = v->array[i];
  v->array[i] = v->array[j];
  v->array[j] = aux;
}

void q_sort(Vector *v, int min, int max)
{
  if (min >= max)
    return;

  int pivot = v->array[select_pivot(min, max)];
  int i = min, j = max;

  while (i != j)
  {
    if (v->array[i] == pivot && v->array[j] == pivot)
      i++;

    while (v->array[i] < pivot)
      i++;
    while (v->array[j] > pivot)
      j--;

    swap(v, i, j);
  }

  q_sort(v, min, i - 1);
  q_sort(v, i + 1, max);
}

void quicksort(Vector *v)
{
  q_sort(v, 0, v->length - 1);
}
