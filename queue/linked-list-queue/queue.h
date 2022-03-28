#ifndef PROJECT_QUEUE_H
#define PROJECT_QUEUE_H

#include "./linked-list/tailed-singly-linked-list.h"

typedef struct queue
{
  int length;
  SinglyLinkedList *list;
} Queue;

Queue *initQueue();
void enqueue(Queue *q, int value);
int dequeue(Queue *q);
int isQueueEmpty(Queue *q);
void destroyQueue(Queue *q);

void run_all_tests();
void test_initQueue();
void test_enqueue();
void test_dequeue();
void test_isQueueEmpty();

#endif
