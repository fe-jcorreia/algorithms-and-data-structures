#ifndef PROJECT_HEAP_H
#define PROJECT_HEAP_H

#include "./vector/vector.h"

typedef struct heap
{
  int length;
  Vector *array;
} Heap;

Heap *initHeap();
void insertHeap(Heap *h, int value);
void siftUp(Heap *h, int index);
int getMax(Heap *h);
int getSize(Heap *h);
int isEmptyHeap(Heap *h);
int extractMax(Heap *h);
void siftDown(Heap *h, int index);
void removeFromHeap(Heap *h, int index);
void heapify(Heap *h);
void heapSort(Vector *v);
void printHeap(Heap *h);
void destroyHeap(Heap *h);

void run_all_tests();
void test_initHeap();
void test_insertHeap();
void test_siftUp();
void test_getMax();
void test_getSize();
void test_isEmptyHeap();
void test_extractMax();
void test_siftDown();
void test_removeFromHeap();
void test_heapify();
void test_heapSort();

#endif
