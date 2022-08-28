#include <stdio.h>
#include <assert.h>
#include "heap.h"

void run_all_tests()
{
  test_initHeap();
  test_insertHeap();
  test_siftUp();
  test_getMin();
  test_getSize();
  test_isEmptyHeap();
  test_extractMax();
  test_siftDown();
  test_removeFromHeap();
  test_heapify();
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

  insertHeap(h, 15, 0);
  insertHeap(h, 10, 0);
  insertHeap(h, 24, 0);
  insertHeap(h, 46, 0);
  insertHeap(h, 30, 0);
  insertHeap(h, 99, 0);
  insertHeap(h, 342, 0);
  insertHeap(h, 64, 0);
  insertHeap(h, 87, 0);
  insertHeap(h, 1, 0);
  insertHeap(h, 12, 0);
  insertHeap(h, 17, 0);

  assert(h->array->array[0].data == 1);
  assert(h->array->array[1].data == 10);
  assert(h->array->array[2].data == 17);
  assert(h->array->array[3].data == 46);
  assert(h->array->array[4].data == 12);
  assert(h->array->array[5].data == 24);
  assert(h->array->array[6].data == 342);
  assert(h->array->array[7].data == 64);
  assert(h->array->array[8].data == 87);
  assert(h->array->array[9].data == 30);
  assert(h->array->array[10].data == 15);
  assert(h->array->array[11].data == 99);

  assert(h->length == 12);

  destroyHeap(h);
  printf("Test insertHeap: OK\n");
}

void test_siftUp()
{
  Heap *h = initHeap();

  Tuple a = {90, 0};
  push(h->array, a);
  Tuple b = {76, 0};
  push(h->array, b);
  Tuple c = {45, 0};
  push(h->array, c);
  Tuple d = {27, 0};
  push(h->array, d);
  Tuple e = {18, 0};
  push(h->array, e);
  Tuple f = {67, 0};
  push(h->array, f);
  Tuple g = {13, 0};
  push(h->array, g);
  Tuple ht = {14, 0};
  push(h->array, ht);

  siftUp(h, 6);
  assert(h->array->array[0].data == 13);
  siftUp(h, 7);
  assert(h->array->array[1].data == 14);

  destroyHeap(h);
  printf("Test siftUp: OK\n");
}

void test_getMin()
{
  Heap *h = initHeap();

  insertHeap(h, 15, 0);
  insertHeap(h, 30, 0);
  insertHeap(h, 99, 0);
  insertHeap(h, 342, 0);
  insertHeap(h, 64, 0);
  insertHeap(h, 87, 0);

  assert(getMin(h).data == 15);

  destroyHeap(h);
  printf("Test getMin: OK\n");
}

void test_getSize()
{
  Heap *h = initHeap();

  insertHeap(h, 15, 0);
  insertHeap(h, 10, 0);
  assert(getSize(h) == 2);
  insertHeap(h, 24, 0);
  insertHeap(h, 46, 0);
  assert(getSize(h) == 4);

  destroyHeap(h);
  printf("Test getSize: OK\n");
}

void test_isEmptyHeap()
{
  Heap *h = initHeap();

  assert(isEmptyHeap(h) == 1);

  insertHeap(h, 15, 0);

  assert(isEmptyHeap(h) == 0);

  destroyHeap(h);
  printf("Test isEmptyHeap: OK\n");
}

void test_extractMax()
{
  Heap *h = initHeap();

  insertHeap(h, 15, 0);
  insertHeap(h, 10, 0);
  insertHeap(h, 24, 0);
  insertHeap(h, 46, 0);
  insertHeap(h, 30, 0);
  insertHeap(h, 99, 0);
  insertHeap(h, 342, 0);
  insertHeap(h, 64, 0);
  insertHeap(h, 87, 0);
  insertHeap(h, 1, 0);
  insertHeap(h, 12, 0);
  insertHeap(h, 17, 0);

  assert(extractMin(h).data == 1);
  assert(extractMin(h).data == 10);
  assert(extractMin(h).data == 12);
  assert(h->length == 9);

  destroyHeap(h);
  printf("Test extractMin: OK\n");
}

void test_siftDown()
{
  Heap *h = initHeap();

  Tuple a = {90, 0};
  push(h->array, a);
  Tuple b = {76, 0};
  push(h->array, b);
  Tuple c = {45, 0};
  push(h->array, c);
  Tuple d = {27, 0};
  push(h->array, d);
  Tuple e = {18, 0};
  push(h->array, e);
  Tuple f = {67, 0};
  push(h->array, f);
  Tuple g = {13, 0};
  push(h->array, g);
  Tuple ht = {14, 0};
  push(h->array, ht);
  h->length = h->array->length;

  siftDown(h, 0);
  assert(h->array->array[0].data == 45);
  assert(h->array->array[6].data == 90);
  siftDown(h, 3);
  assert(h->array->array[3].data == 14);
  assert(h->array->array[7].data == 27);

  destroyHeap(h);
  printf("Test siftDown: OK\n");
}

void test_removeFromHeap()
{
  Heap *h = initHeap();

  insertHeap(h, 15, 0);
  insertHeap(h, 10, 0);
  insertHeap(h, 24, 0);
  insertHeap(h, 46, 0);
  insertHeap(h, 30, 0);
  insertHeap(h, 99, 0);
  insertHeap(h, 342, 0);
  insertHeap(h, 64, 0);
  insertHeap(h, 87, 0);
  insertHeap(h, 1, 0);
  insertHeap(h, 12, 0);
  insertHeap(h, 17, 0);

  removeFromHeap(h, 1);

  assert(h->array->array[1].data == 12);
  assert(h->array->array[4].data == 15);
  assert(h->array->array[10].data == 99);
  assert(h->length == 11);

  destroyHeap(h);
  printf("Test removeFromHeap: OK\n");
}

void test_heapify()
{
  Heap *h = initHeap();

  Tuple a = {90, 0};
  push(h->array, a);
  Tuple b = {76, 0};
  push(h->array, b);
  Tuple c = {45, 0};
  push(h->array, c);
  Tuple d = {27, 0};
  push(h->array, d);
  Tuple e = {18, 0};
  push(h->array, e);
  Tuple f = {67, 0};
  push(h->array, f);
  Tuple g = {13, 0};
  push(h->array, g);
  Tuple ht = {14, 0};
  push(h->array, ht);
  h->length = h->array->length;

  heapify(h);

  assert(h->array->array[0].data == 13);
  assert(h->array->array[1].data == 14);
  assert(h->array->array[2].data == 45);
  assert(h->array->array[3].data == 27);
  assert(h->array->array[4].data == 18);
  assert(h->array->array[5].data == 67);
  assert(h->array->array[6].data == 90);
  assert(h->array->array[7].data == 76);

  destroyHeap(h);
  printf("Test heapify: OK\n");
}
