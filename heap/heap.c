#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#include "heap.h"
#include "./vector/vector.h"

Heap *initHeap()
{
  Heap *heap = (Heap *)malloc(sizeof(Heap));
  heap->array = initVector();
  heap->length = heap->array->length;

  return heap;
}

void insertHeap(Heap *h, int value)
{
  push(h->array, value);
  h->length++;
  siftUp(h, h->length - 1);
}

void siftUp(Heap *h, int index)
{
  int *heap = h->array->array;

  if (index < 0 && index >= h->length)
    return;

  if (heap[index] > heap[(index - 1) / 2])
  {
    int aux = heap[(index - 1) / 2];
    heap[(index - 1) / 2] = heap[index];
    heap[index] = aux;
    siftUp(h, (index - 1) / 2);
  }
}

int getMax(Heap *h)
{
  return h->array->array[0];
}

int getSize(Heap *h)
{
  return h->length;
}

int isEmptyHeap(Heap *h)
{
  if (h->length)
    return 1;
  else
    return 0;
}

int extractMax(Heap *h)
{
  int maxValue = h->array->array[0];

  h->array->array[0] = h->array->array[h->length - 1];
  pop(h->array);
  h->length--;

  siftDown(h, 0);

  return maxValue;
}

void siftDown(Heap *h, int index)
{
  int *heap = h->array->array;
  int maxIndex = index;

  if (index < 0 && index >= h->length)
    return;

  if ((2 * index) + 1 < h->length && heap[(2 * index) + 1] > heap[maxIndex])
    maxIndex = (2 * index) + 1;
  if ((2 * index) + 2 < h->length && heap[(2 * index) + 2] > heap[maxIndex])
    maxIndex = (2 * index) + 2;

  if (heap[index] < heap[maxIndex])
  {
    int aux = heap[maxIndex];
    heap[maxIndex] = heap[index];
    heap[index] = aux;
    siftDown(h, maxIndex);
  }
}

void removeFromHeap(Heap *h, int index)
{
  int *heap = h->array->array;

  heap[index] = INT_MAX;
  siftUp(h, index);
  extractMax(h);
}

void heapify(Heap *h)
{
  for (int i = (h->length - 1) / 2; i >= 0; i--)
    siftDown(h, i);
}

void heapSort(Vector *v)
{
  Heap *h = initHeap();
  Vector *aux = initVector();
  destroyVector(h->array);
  h->array = v;
  h->length = h->array->length;

  heapify(h);

  int len = h->length;
  for (int i = 0; i < len; i++)
    push(aux, extractMax(h));

  len = aux->length;
  push(v, *(aux->array));
  for (int i = 1; i < len; i++)
    prepend(v, *(aux->array + i));

  h->array = aux;
  destroyHeap(h);
}

void destroyHeap(Heap *h)
{
  destroyVector(h->array);
  free(h);
}

void printHeap(Heap *h)
{
  printVector(h->array);
}
