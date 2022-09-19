#include <stdio.h>
#include <assert.h>
#include "queue.h"

void run_all_tests()
{
  test_initQueue(10);
  test_enqueue();
  test_dequeue();
  test_isQueueEmpty();
  test_isQueueFull();
}

void test_initQueue(int capacity)
{
  Queue *q = initQueue(capacity);

  assert(q->length == 0);
  assert(q->capacity == capacity);
  assert(q->in == 0);
  assert(q->out == 0);

  printf("Test initQueue: OK\n");

  destroyQueue(q);
}

void test_enqueue()
{
  Queue *q = initQueue(10);

  for (int i = 0; i < 10; i++)
  {
    enqueue(q, i);
    assert(q->in == i + 1);
  }

  enqueue(q, 10);
  assert(*(q->list) == 0);
  assert(*(q->list + 9) == 9);

  assert(q->out == 0);
  dequeue(q);
  assert(q->out == 1);

  enqueue(q, 10);
  assert(*(q->list) == 10);

  enqueue(q, 11);
  assert(*(q->list + 1) == 1);

  dequeue(q);
  assert(q->out == 2);
  enqueue(q, 11);
  assert(*(q->list + 1) == 11);

  printf("Test enqueue: OK\n");

  destroyQueue(q);
}

void test_dequeue()
{
  Queue *q = initQueue(10);

  for (int i = 0; i < 10; i++)
    enqueue(q, i);

  for (int i = 0; i < 10; i++)
    assert(dequeue(q) == i);

  assert(dequeue(q) == -1);
  enqueue(q, 10);
  assert(dequeue(q) == 10);
  assert(dequeue(q) == -1);

  printf("Test dequeue: OK\n");

  destroyQueue(q);
}

void test_isQueueEmpty()
{
  Queue *q = initQueue(10);
  assert(isQueueEmpty(q) == 1);

  for (int i = 0; i < 10; i++)
    enqueue(q, i);

  assert(isQueueEmpty(q) == 0);

  printf("Test isQueueEmpty: OK\n");

  destroyQueue(q);
}

void test_isQueueFull()
{
  Queue *q = initQueue(10);
  assert(isQueueFull(q) == 0);

  for (int i = 0; i < 10; i++)
    enqueue(q, i);

  assert(isQueueFull(q) == 1);
  dequeue(q);
  assert(isQueueFull(q) == 0);
  enqueue(q, 10);
  assert(isQueueFull(q) == 1);

  printf("Test isQueueFull: OK\n");

  destroyQueue(q);
}
