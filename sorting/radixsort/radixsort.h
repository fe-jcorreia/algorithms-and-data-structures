#ifndef PROJECT_RADIXSORT_H
#define PROJECT_RADIXSORT_H

#include "./vector/vector.h"

typedef struct radixItem
{
  int data;
  struct radixItem *next;
} RadixItem;

void radixsort(Vector *v, int k);

void run_all_tests();
void test_radixsort();

#endif
