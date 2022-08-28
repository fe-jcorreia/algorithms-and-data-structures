#ifndef PROJECT_VECTOR_H
#define PROJECT_VECTOR_H

typedef struct tuple
{
  int data;
  int index;
} Tuple;

typedef struct vector
{
  int length;
  int capacity;
  Tuple *array;
} Vector;

Vector *initVector();
int is_empty(Vector *v);
void resize(Vector *v, int capacity);
void push(Vector *v, Tuple item);
void pop(Vector *v);
void destroyVector(Vector *v);
void printVector(Vector *v);

void run_all_tests();
void test_initVector();
void test_push();
void test_empty();
void test_pop();

#endif
