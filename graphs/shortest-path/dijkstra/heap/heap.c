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

void insertHeap(Heap *h, int value, int index)
{
  Tuple insert = {value, index};
  push(h->array, insert);
  h->length++;
  siftUp(h, h->length - 1);
}

void siftUp(Heap *h, int index)
{
  Tuple *heap = h->array->array;

  if (index < 0 && index >= h->length)
    return;

  if (heap[index].data < heap[(index - 1) / 2].data)
  {
    Tuple aux = heap[(index - 1) / 2];
    heap[(index - 1) / 2] = heap[index];
    heap[index] = aux;
    siftUp(h, (index - 1) / 2);
  }
}

Tuple getMin(Heap *h)
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
    return 0;
  else
    return 1;
}

Tuple extractMin(Heap *h)
{
  Tuple minValue = h->array->array[0];

  h->array->array[0] = h->array->array[h->length - 1];
  pop(h->array);
  h->length--;

  siftDown(h, 0);

  return minValue;
}

void siftDown(Heap *h, int index)
{
  Tuple *heap = h->array->array;
  int minIndex = index;

  if (index < 0 && index >= h->length)
    return;

  if ((2 * index) + 1 < h->length && heap[(2 * index) + 1].data < heap[minIndex].data)
    minIndex = (2 * index) + 1;
  if ((2 * index) + 2 < h->length && heap[(2 * index) + 2].data < heap[minIndex].data)
    minIndex = (2 * index) + 2;

  if (heap[index].data > heap[minIndex].data)
  {
    Tuple aux = heap[minIndex];
    heap[minIndex] = heap[index];
    heap[index] = aux;
    siftDown(h, minIndex);
  }
}

void removeFromHeap(Heap *h, int index)
{
  Tuple *heap = h->array->array;

  heap[index].data = INT_MIN;
  siftUp(h, index);
  extractMin(h);
}

void heapify(Heap *h)
{
  for (int i = (h->length - 1) / 2; i >= 0; i--)
    siftDown(h, i);
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
