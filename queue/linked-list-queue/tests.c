#include <stdio.h>
#include <assert.h>
#include "queue.h"

void run_all_tests()
{
  test_initQueue();
  test_enqueue();
  test_dequeue();
  test_isQueueEmpty();
}

void test_initQueue()
{
  Queue *q = initQueue();

  assert(q->length == 0);
  assert(q->list->head == NULL);
  assert(q->list->tail == NULL);
  assert(q->list->length == 0);

  printf("Test initQueue: OK\n");

  destroyQueue(q);
}

void test_enqueue()
{
  Queue *q = initQueue();

  for (int i = 0; i < 5; i++)
    enqueue(q, i);

  assert(q->list->head->data == 0);
  assert(q->list->head->next->data == 1);
  assert(q->list->head->next->next->data == 2);
  assert(q->list->head->next->next->next->data == 3);
  assert(q->list->tail->data == 4);

  printf("Test enqueue: OK\n");

  destroyQueue(q);
}

void test_dequeue()
{
  Queue *q = initQueue();

  for (int i = 0; i < 5; i++)
    enqueue(q, i);

  assert(dequeue(q) == 0);
  assert(dequeue(q) == 1);
  assert(dequeue(q) == 2);
  assert(dequeue(q) == 3);
  assert(dequeue(q) == 4);
  assert(q->length == 0);

  printf("Test dequeue: OK\n");

  destroyQueue(q);
}

void test_isQueueEmpty()
{
  Queue *q = initQueue();
  assert(isQueueEmpty(q) == 1);

  for (int i = 0; i < 5; i++)
    enqueue(q, i);

  assert(isQueueEmpty(q) == 0);

  printf("Test isQueueEmpty: OK\n");

  destroyQueue(q);
}
