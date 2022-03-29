#include <stdio.h>
#include <assert.h>
#include "heap.h"

void run_all_tests()
{
  test_initHeap();
  test_insertHeap();
  test_siftUp();
  test_getMax();
  test_getSize();
  test_isEmptyHeap();
  test_extractMax();
  test_siftDown();
  test_removeFromHeap();
  test_heapify();
  test_heapSort();
}

void test_initHeap()
{
  Heap *h = initHeap();

  assert(h->length == 0);

  destroyHeap(h);
  printf("Test initHeap: OK\n");
}

void test_insertHeap()
{
  Heap *h = initHeap();

  insertHeap(h, 15);
  insertHeap(h, 10);
  insertHeap(h, 24);
  insertHeap(h, 46);
  insertHeap(h, 30);
  insertHeap(h, 99);
  insertHeap(h, 342);
  insertHeap(h, 64);
  insertHeap(h, 87);
  insertHeap(h, 1);
  insertHeap(h, 12);
  insertHeap(h, 17);

  assert(h->array->array[0] == 342);
  assert(h->array->array[1] == 87);
  assert(h->array->array[2] == 99);
  assert(h->array->array[3] == 64);
  assert(h->array->array[4] == 24);
  assert(h->array->array[5] == 17);
  assert(h->array->array[6] == 46);
  assert(h->array->array[7] == 10);
  assert(h->array->array[8] == 30);
  assert(h->array->array[9] == 1);
  assert(h->array->array[10] == 12);
  assert(h->array->array[11] == 15);

  assert(h->length == 12);

  destroyHeap(h);
  printf("Test insertHeap: OK\n");
}

void test_siftUp()
{
  Heap *h = initHeap();

  push(h->array, 14);
  push(h->array, 45);
  push(h->array, 27);
  push(h->array, 13);
  push(h->array, 18);
  push(h->array, 67);
  push(h->array, 90);
  push(h->array, 76);

  siftUp(h, 6);
  assert(h->array->array[0] == 90);
  siftUp(h, 7);
  assert(h->array->array[1] == 76);

  destroyHeap(h);
  printf("Test siftUp: OK\n");
}

void test_getMax()
{
  Heap *h = initHeap();

  insertHeap(h, 15);
  insertHeap(h, 30);
  insertHeap(h, 99);
  insertHeap(h, 342);
  insertHeap(h, 64);
  insertHeap(h, 87);

  assert(getMax(h) == 342);

  destroyHeap(h);
  printf("Test getMax: OK\n");
}

void test_getSize()
{
  Heap *h = initHeap();

  insertHeap(h, 15);
  insertHeap(h, 10);
  assert(getSize(h) == 2);
  insertHeap(h, 24);
  insertHeap(h, 46);
  assert(getSize(h) == 4);

  destroyHeap(h);
  printf("Test getSize: OK\n");
}

void test_isEmptyHeap()
{
  Heap *h = initHeap();

  assert(isEmptyHeap(h) == 1);

  insertHeap(h, 15);

  assert(isEmptyHeap(h) == 0);

  destroyHeap(h);
  printf("Test isEmptyHeap: OK\n");
}

void test_extractMax()
{
  Heap *h = initHeap();

  insertHeap(h, 15);
  insertHeap(h, 10);
  insertHeap(h, 24);
  insertHeap(h, 46);
  insertHeap(h, 30);
  insertHeap(h, 99);
  insertHeap(h, 342);
  insertHeap(h, 64);
  insertHeap(h, 87);
  insertHeap(h, 1);
  insertHeap(h, 12);
  insertHeap(h, 17);

  assert(extractMax(h) == 342);
  assert(extractMax(h) == 99);
  assert(extractMax(h) == 87);
  assert(h->length == 9);

  destroyHeap(h);
  printf("Test extractMax: OK\n");
}

void test_siftDown()
{
  Heap *h = initHeap();

  push(h->array, 14);
  push(h->array, 45);
  push(h->array, 27);
  push(h->array, 13);
  push(h->array, 18);
  push(h->array, 67);
  push(h->array, 90);
  push(h->array, 76);
  h->length = h->array->length;

  siftDown(h, 0);
  assert(h->array->array[0] == 45);
  assert(h->array->array[4] == 14);
  siftDown(h, 3);
  assert(h->array->array[3] == 76);
  assert(h->array->array[7] == 13);

  destroyHeap(h);
  printf("Test siftDown: OK\n");
}

void test_removeFromHeap()
{
  Heap *h = initHeap();

  insertHeap(h, 15);
  insertHeap(h, 10);
  insertHeap(h, 24);
  insertHeap(h, 46);
  insertHeap(h, 30);
  insertHeap(h, 99);
  insertHeap(h, 342);
  insertHeap(h, 64);
  insertHeap(h, 87);
  insertHeap(h, 1);
  insertHeap(h, 12);
  insertHeap(h, 17);

  removeFromHeap(h, 1);

  assert(h->array->array[1] == 64);
  assert(h->array->array[3] == 30);
  assert(h->array->array[8] == 15);
  assert(h->length == 11);

  destroyHeap(h);
  printf("Test removeFromHeap: OK\n");
}

void test_heapify()
{
  Heap *h = initHeap();

  push(h->array, 14);
  push(h->array, 45);
  push(h->array, 27);
  push(h->array, 13);
  push(h->array, 18);
  push(h->array, 67);
  push(h->array, 90);
  push(h->array, 76);
  h->length = h->array->length;

  heapify(h);

  assert(h->array->array[0] == 90);
  assert(h->array->array[1] == 76);
  assert(h->array->array[2] == 67);
  assert(h->array->array[3] == 45);
  assert(h->array->array[4] == 18);
  assert(h->array->array[5] == 14);
  assert(h->array->array[6] == 27);
  assert(h->array->array[7] == 13);

  destroyHeap(h);
  printf("Test heapify: OK\n");
}

void test_heapSort()
{
  Vector *v = initVector();
  push(v, 14);
  push(v, 45);
  push(v, 27);
  push(v, 13);
  push(v, 18);
  push(v, 67);
  push(v, 90);
  push(v, 76);

  heapSort(v);

  assert(v->array[0] == 13);
  assert(v->array[1] == 14);
  assert(v->array[2] == 18);
  assert(v->array[3] == 27);
  assert(v->array[4] == 45);
  assert(v->array[5] == 67);
  assert(v->array[6] == 76);
  assert(v->array[7] == 90);

  destroyVector(v);
  printf("Test heapSort: OK\n");
}
