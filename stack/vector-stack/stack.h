#ifndef PROJECT_STACK_H
#define PROJECT_STACK_H

#include "../../vector/vector.h"

typedef struct stack
{
  int length;
  Vector *list;
} Stack;

Stack *initStack();
void pushStack(Stack *s, int value);
int popStack(Stack *s);
int isStackEmpty(Stack *s);
int top(Stack *s);
void destroyStack(Stack *s);
void printStack(Stack *s);

void run_all_tests();
void test_initStack();
void test_pushStack();
void test_popStack();
void test_isStackEmpty();
void test_top();

#endif
