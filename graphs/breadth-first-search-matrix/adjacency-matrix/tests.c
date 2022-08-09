#include <stdio.h>
#include <assert.h>
#include "adjacency-matrix.h"

void run_all_tests()
{
  test_initGraph();
  test_isEmptyGraph();
  test_insertEdge();
}

void test_initGraph()
{
  Graph *graph = initGraph(10);

  assert(graph->totalVertices == 10);

  for (int i = 0; i < graph->totalVertices; i++)
    for (int j = 0; j < graph->totalVertices; j++)
      assert(graph->adjMatrix[i]->array[j] == 0);

  destroyGraph(graph);
  printf("Test initGraph: OK\n");
}

void test_isEmptyGraph()
{
  Graph *graph = initGraph(0);
  assert(isEmptyGraph(graph) == 1);
  destroyGraph(graph);

  graph = initGraph(10);
  assert(isEmptyGraph(graph) == 0);

  destroyGraph(graph);
  printf("Test isEmptyGraph: OK\n");
}

void test_insertEdge()
{
  Graph *graph = initGraph(9);

  insertEdge(graph, 0, 1);
  insertEdge(graph, 3, 6);

  assert(graph->adjMatrix[0]->array[1] == 1);
  assert(graph->adjMatrix[1]->array[0] == 1);

  assert(graph->adjMatrix[3]->array[6] == 1);
  assert(graph->adjMatrix[6]->array[3] == 1);

  destroyGraph(graph);
  printf("Test insertEdge: OK\n");
}
