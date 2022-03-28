#ifndef PROJECT_STACK_H
#define PROJECT_STACK_H

#include "./linked-list/nontailed-singly-linked-list.h"

typedef struct stack
{
  int length;
  SinglyLinkedList *list;
} Stack;

Stack *initStack();
void push(Stack *s, int value);
int pop(Stack *s);
int isStackEmpty(Stack *s);
int top(Stack *s);
void destroyStack(Stack *s);
void printStack(Stack *s);

void run_all_tests();
void test_initStack();
void test_push();
void test_pop();
void test_isStackEmpty();
void test_top();

#endif
