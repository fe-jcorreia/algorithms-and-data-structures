#include <stdio.h>
#include <assert.h>
#include "binary-search.h"

void run_all_tests()
{
  test_binarySearch();
}

void test_binarySearch()
{
  int array[18] = {1, 2, 8, 22, 29, 40, 41, 51, 52, 55, 62, 64, 65, 68, 76, 86, 92, 100};

  assert(binarySearch(array, 12, 0, 17) == -1);
  assert(binarySearch(array, 1, 0, 17) == 1);
  assert(binarySearch(array, 2, 0, 17) == 2);
  assert(binarySearch(array, 8, 0, 17) == 8);
  assert(binarySearch(array, 22, 0, 17) == 22);
  assert(binarySearch(array, 29, 0, 17) == 29);
  assert(binarySearch(array, 40, 0, 17) == 40);
  assert(binarySearch(array, 41, 0, 17) == 41);
  assert(binarySearch(array, 51, 0, 17) == 51);
  assert(binarySearch(array, 52, 0, 17) == 52);
  assert(binarySearch(array, 55, 0, 17) == 55);
  assert(binarySearch(array, 62, 0, 17) == 62);
  assert(binarySearch(array, 64, 0, 17) == 64);
  assert(binarySearch(array, 65, 0, 17) == 65);
  assert(binarySearch(array, 68, 0, 17) == 68);
  assert(binarySearch(array, 76, 0, 17) == 76);
  assert(binarySearch(array, 86, 0, 17) == 86);
  assert(binarySearch(array, 92, 0, 17) == 92);
  assert(binarySearch(array, 100, 0, 17) == 100);

  printf("Test binarySearch: OK\n");
}
