#ifndef PROJECT_ADJACENCY_LIST_H
#define PROJECT_ADJACENCY_LIST_H

#include "./tailed-singly-linked-list/tailed-singly-linked-list.h"

typedef struct graph
{
  int totalVertices;
  int totalCapacity;
  SinglyLinkedList **adjList;
} Graph;

Graph *initGraph(int totalCapacity);
int isEmptyGraph(Graph *graph);
void insertEdge(Graph *graph, int s, int d);
void addVertex(Graph *graph);
void eraseVertex(Graph *graph, int vertex);
void destroyGraph(Graph *graph);
void printGraph(Graph *graph);

void run_all_tests();
void test_initGraph();
void test_isEmptyGraph();
void test_insertEdge();
void test_addVertex();
void test_eraseVertex();

#endif
