#include <stdio.h>
#include <stdlib.h>

#include "queue.h"
#include "./linked-list/tailed-singly-linked-list.h"

Queue *initQueue()
{
  Queue *q = (Queue *)malloc(sizeof(Queue));
  q->length = 0;
  q->list = initList();

  return q;
}

void enqueue(Queue *q, int value)
{
  pushBack(q->list, value);
  q->length++;
}

int dequeue(Queue *q)
{
  int value = q->list->head->data;
  popFront(q->list);
  q->length--;
  return value;
}

int isQueueEmpty(Queue *q)
{
  if (q->length)
    return 0;
  else
    return 1;
}

void destroyQueue(Queue *q)
{
  destroyList(q->list);
  free(q);
}
