#include <stdio.h>
#include <stdlib.h>

#include "mergesort.h"

void merge(int array[], int aux[], int max, int min, int middle)
{
  for (int k = min; k < max + 1; k++)
    aux[k] = array[k];

  int i = min;
  int j = middle + 1;
  for (int k = min; k < max + 1; k++)
  {
    if (i > middle)
      array[k] = aux[j++];
    else if (j > max)
      array[k] = aux[i++];
    else if (aux[j] < aux[i])
      array[k] = aux[j++];
    else
      array[k] = aux[i++];
  }
}

void sorting(int array[], int aux[], int max, int min)
{
  if (max <= min)
    return;

  int middle = min + (max - min) / 2;

  sorting(array, aux, middle, min);
  sorting(array, aux, max, middle + 1);

  merge(array, aux, max, min, middle);
}

void mergesort(Vector *v)
{
  int n = v->length;
  int aux[n];

  for (int i = 0; i < n; i++)
    aux[i] = v->array[i];

  sorting(v->array, aux, n - 1, 0);
}
