#include <stdio.h>
#include "heap.h"

int main()
{
  // run_all_tests();
  Vector *v = initVector();
  push(v, 14);
  push(v, 45);
  push(v, 27);
  push(v, 13);
  push(v, 18);
  push(v, 67);
  push(v, 90);
  push(v, 76);
  printVector(v);
  heapSort(v);
  printVector(v);

  // Heap *h = initHeap();
  // push(h->array, 14);
  // push(h->array, 45);
  // push(h->array, 27);
  // push(h->array, 13);
  // push(h->array, 18);
  // push(h->array, 67);
  // push(h->array, 90);
  // push(h->array, 76);
  // h->length = h->array->length;

  // printHeap(h);

  // heapify(h);

  // insertHeap(h, 15);
  // insertHeap(h, 10);
  // insertHeap(h, 24);
  // insertHeap(h, 46);
  // insertHeap(h, 30);
  // insertHeap(h, 99);
  // insertHeap(h, 342);
  // insertHeap(h, 64);
  // insertHeap(h, 87);
  // insertHeap(h, 1);
  // insertHeap(h, 12);
  // insertHeap(h, 17);

  // removeFromHeap(h, 3);

  // printf("max: %d\n", getMax(h));
  // printf("size: %d\n", getSize(h));
  // printf("isEmpty: %d\n", isEmptyHeap(h));

  // printf("extracted max: %d\n", extractMax(h));
  // printf("extracted max: %d\n", extractMax(h));

  // printHeap(h);
  return 0;
}