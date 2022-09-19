#ifndef PROJECT_QUEUE_H
#define PROJECT_QUEUE_H

typedef struct queue
{
  int length;
  int capacity;
  int out;
  int in;
  int *list;
} Queue;

Queue *initQueue(int capacity);
void enqueue(Queue *q, int value);
int dequeue(Queue *q);
int isQueueEmpty(Queue *q);
int isQueueFull(Queue *q);
void destroyQueue(Queue *q);
void printQueue(Queue *q);

void run_all_tests();
void test_initQueue();
void test_enqueue();
void test_dequeue();
void test_isQueueEmpty();
void test_isQueueFull();

#endif
