#include <stdio.h>
#include <assert.h>
#include "adjacency-list.h"

void run_all_tests()
{
  test_initGraph();
  test_isEmptyGraph();
  test_insertEdge();
  test_addVertex();
  test_eraseVertex();
}

void test_initGraph()
{
  Graph *graph = initGraph(10);

  assert(graph->totalCapacity == 10);
  assert(graph->totalVertices == 0);

  for (int i = 0; i < graph->totalCapacity; i++)
  {
    assert(graph->adjList[i]->length == 0);
    assert(graph->adjList[i]->head == NULL);
    assert(graph->adjList[i]->tail == NULL);
  }

  destroyGraph(graph);
  printf("Test initGraph: OK\n");
}

void test_isEmptyGraph()
{
  Graph *graph = initGraph(10);
  assert(isEmptyGraph(graph) == 1);

  addVertex(graph);
  assert(isEmptyGraph(graph) == 0);

  destroyGraph(graph);
  printf("Test isEmptyGraph: OK\n");
}

void test_insertEdge()
{
  Graph *graph = initGraph(10);

  for (int i = 0; i < 9; i++)
    addVertex(graph);

  insertEdge(graph, 1, 2, 10);
  assert(graph->adjList[1]->head->data == 2);
  assert(graph->adjList[2]->head->data == 1);
  insertEdge(graph, 1, 4, 5);
  assert(graph->adjList[1]->head->next->data == 4);
  assert(graph->adjList[4]->head->data == 1);

  destroyGraph(graph);
  printf("Test insertEdge: OK\n");
}

void test_addVertex()
{
  Graph *graph = initGraph(10);

  for (int i = 0; i < 9; i++)
    addVertex(graph);

  for (int i = 0; i < 9; i++)
  {
    assert(graph->adjList[i]->length == 0);
    assert(graph->adjList[i]->head == NULL);
    assert(graph->adjList[i]->tail == NULL);
  }

  destroyGraph(graph);
  printf("Test addVertex: OK\n");
}

void test_eraseVertex()
{
  Graph *graph = initGraph(10);

  for (int i = 0; i < 9; i++)
    addVertex(graph);

  insertEdge(graph, 0, 1, 3);
  insertEdge(graph, 1, 2, 4);
  insertEdge(graph, 1, 4, 5);
  insertEdge(graph, 3, 4, 6);
  insertEdge(graph, 1, 3, 7);
  insertEdge(graph, 3, 6, 8);
  insertEdge(graph, 3, 5, 9);
  insertEdge(graph, 6, 7, 10);
  insertEdge(graph, 7, 5, 11);
  insertEdge(graph, 7, 8, 12);

  eraseVertex(graph, 3);

  assert(graph->adjList[1]->head->data == 0);
  assert(graph->adjList[1]->head->next->data == 2);
  assert(graph->adjList[1]->head->next->next->data == 3);

  assert(graph->adjList[6]->head->data == 5);
  assert(graph->adjList[6]->head->next->data == 4);
  assert(graph->adjList[6]->head->next->next->data == 7);

  destroyGraph(graph);
  printf("Test eraseVertex: OK\n");
}
