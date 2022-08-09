#ifndef PROJECT_ADJACENCY_MATRIX_H
#define PROJECT_ADJACENCY_MATRIX_H

#include "./vector/vector.h"

typedef struct graph
{
  int totalVertices;
  Vector **adjMatrix;
} Graph;

Graph *initGraph(int initialCapacity);
int isEmptyGraph(Graph *graph);
void insertEdge(Graph *graph, int s, int d);
void destroyGraph(Graph *graph);
void printGraph(Graph *graph);

void run_all_tests();
void test_initGraph();
void test_isEmptyGraph();
void test_insertEdge();

#endif
