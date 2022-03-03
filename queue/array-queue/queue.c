#include <stdio.h>
#include <stdlib.h>

#include "queue.h"

Queue *initQueue(int capacity)
{
  Queue *q = (Queue *)malloc(sizeof(Queue));
  q->length = 0;
  q->capacity = capacity;
  q->in = q->out = 0;
  q->list = (int *)malloc(q->capacity * sizeof(int));

  return q;
}

void enqueue(Queue *q, int value)
{
  if (isQueueFull(q))
    return;

  if (q->in == q->capacity)
    q->in = 0;

  *(q->list + q->in) = value;
  if (q->length + 1 <= q->capacity)
    q->length++;

  q->in++;
}

int dequeue(Queue *q)
{
  if (isQueueEmpty(q))
    return -1;

  int value = *(q->list + q->out);
  q->length--;
  q->out++;

  if (q->out == q->capacity)
    q->out = 0;

  return value;
}

int isQueueEmpty(Queue *q)
{
  return (q->in == q->out || (q->in == 10 && q->out == 0)) && q->length == 0;
}

int isQueueFull(Queue *q)
{
  return q->length == q->capacity;
}

void destroyQueue(Queue *q)
{
  free(q->list);
  free(q);
}

void printQueue(Queue *q)
{
  printf("Length: %d\n", q->length);
  printf("Capacity: %d\n", q->capacity);
  printf("Next in: %d\n", q->in);
  printf("Next out: %d\n", q->out);
  for (int i = 0; i < 10; i++)
    printf("%d ", *(q->list + i));
  printf("\n");
  printf("\n");
}
