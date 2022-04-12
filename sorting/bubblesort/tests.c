#include <stdio.h>
#include <assert.h>
#include "bubblesort.h"

void run_all_tests()
{
  test_bubblesort();
}

void test_bubblesort()
{
  Vector *v = initVector();
  push(v, 64);
  push(v, 2);
  push(v, 59);
  push(v, 22);
  push(v, 73);
  push(v, 40);
  push(v, 13);
  push(v, 51);
  push(v, 4);
  push(v, 55);
  push(v, 62);
  push(v, 1);
  push(v, 99);
  push(v, 40);
  push(v, 17);
  push(v, 76);
  push(v, 34);
  push(v, 92);
  push(v, 23);

  bubblesort(v);

  assert(v->array[0] == 1);
  assert(v->array[1] == 2);
  assert(v->array[2] == 4);
  assert(v->array[3] == 13);
  assert(v->array[4] == 17);
  assert(v->array[5] == 22);
  assert(v->array[6] == 23);
  assert(v->array[7] == 34);
  assert(v->array[8] == 40);
  assert(v->array[9] == 40);
  assert(v->array[10] == 51);
  assert(v->array[11] == 55);
  assert(v->array[12] == 59);
  assert(v->array[13] == 62);
  assert(v->array[14] == 64);
  assert(v->array[15] == 73);
  assert(v->array[16] == 76);
  assert(v->array[17] == 92);
  assert(v->array[18] == 99);

  printf("Test bubblesort: OK\n");
}
