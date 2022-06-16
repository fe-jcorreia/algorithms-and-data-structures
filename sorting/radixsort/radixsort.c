#include <stdio.h>
#include <stdlib.h>

#include "radixsort.h"

void radixsort(Vector *v, int k)
{
  Vector *arr[10];
  for (int i = 0; i < 10; i++)
    arr[i] = initVector();

  int mod = 10;
  int q = 1;

  while (q <= k)
  {
    for (int i = 0; i < v->length; i++)
    {
      int unit = v->array[i] % mod;
      int index = unit / q;
      push(arr[index], v->array[i]);
    }

    int count = 0;
    for (int i = 0; i < 10; i++)
    {
      for (int j = 0; j < arr[i]->length; j++)
      {
        v->array[count] = arr[i]->array[j];
        count++;
      }
      destroyVector(arr[i]);
      arr[i] = initVector();
    }

    mod *= 10;
    q *= 10;
  }
}
