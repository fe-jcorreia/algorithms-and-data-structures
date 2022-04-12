#include <stdio.h>
#include <stdlib.h>

#include "heapsort.h"

void siftDown(int array[], int len, int index)
{
  int *heap = array;
  int maxIndex = index;

  if (index < 0 && index >= len)
    return;

  if ((2 * index) + 1 < len && heap[(2 * index) + 1] > heap[maxIndex])
    maxIndex = (2 * index) + 1;
  if ((2 * index) + 2 < len && heap[(2 * index) + 2] > heap[maxIndex])
    maxIndex = (2 * index) + 2;

  if (heap[index] < heap[maxIndex])
  {
    int aux = heap[maxIndex];
    heap[maxIndex] = heap[index];
    heap[index] = aux;
    siftDown(array, len, maxIndex);
  }
}

void heapify(Vector *v)
{
  for (int i = (v->length - 2) / 2; i >= 0; i--)
    siftDown(v->array, v->length, i);
}

void heapsort(Vector *v)
{
  heapify(v);

  int len = v->length;
  while (len != 0)
  {
    int aux = v->array[len - 1];
    v->array[len - 1] = v->array[0];
    v->array[0] = aux;
    len--;
    siftDown(v->array, len, 0);
  }
}
