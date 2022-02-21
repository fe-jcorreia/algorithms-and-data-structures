#ifndef PROJECT_VECTOR_H
#define PROJECT_VECTOR_H

typedef struct vector
{
  int length;
  int capacity;
  int *array;
} Vector;

Vector *initVector();
int is_empty(Vector *v);
int at(Vector *v, int index);
void resize(Vector *v, int capacity);
void push(Vector *v, int item);
void insert(Vector *v, int index, int item);
void prepend(Vector *v, int item);
void pop(Vector *v);
void deleteIndex(Vector *v, int index);
void removeItem(Vector *v, int item);
int find(Vector *v, int item);
void destroyVector(Vector *v);
void printVector(Vector *v);

void run_all_tests();
void test_initVector();
void test_push();
void test_resize();
void test_empty();
void test_at();
void test_edit();
void test_insert();
void test_prepend();
void test_pop();
void test_deleteIndex();
void test_removeItem();
void test_find();

#endif
