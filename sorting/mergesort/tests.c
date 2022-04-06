#include <stdio.h>
#include <assert.h>
#include "mergesort.h"

void run_all_tests()
{
  test_mergesort();
}

void test_mergesort()
{
  int array[18] = {64, 2, 59, 22, 73, 40, 13, 51, 4, 55, 62, 1, 99, 17, 76, 34, 92, 23};

  mergesort(array);

  assert(array[0] == 1);
  assert(array[1] == 2);
  assert(array[2] == 4);
  assert(array[3] == 13);
  assert(array[4] == 17);
  assert(array[5] == 22);
  assert(array[6] == 23);
  assert(array[7] == 34);
  assert(array[8] == 40);
  assert(array[9] == 51);
  assert(array[10] == 55);
  assert(array[11] == 59);
  assert(array[12] == 62);
  assert(array[13] == 64);
  assert(array[14] == 73);
  assert(array[15] == 76);
  assert(array[16] == 92);
  assert(array[17] == 99);

  printf("Test mergesort: OK\n");
}
