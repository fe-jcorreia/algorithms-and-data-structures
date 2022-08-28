#include <stdio.h>
#include <assert.h>
#include "dijkstra.h"

void run_all_tests()
{
  test_dijkstra();
}

void test_dijkstra()
{
  Graph *graph = initGraph(10);

  for (int i = 0; i < 9; i++)
    addVertex(graph);

  insertEdge(graph, 0, 1, 5);
  insertEdge(graph, 1, 2, 2);
  insertEdge(graph, 1, 3, 1);
  insertEdge(graph, 1, 4, 3);
  insertEdge(graph, 3, 6, 4);
  insertEdge(graph, 3, 5, 2);
  insertEdge(graph, 3, 4, 1);
  insertEdge(graph, 6, 7, 1);
  insertEdge(graph, 5, 7, 2);
  insertEdge(graph, 7, 8, 1);

  dijkstra(graph, 1);

  destroyGraph(graph);
  printf("Test Dijkstra: OK\n");
}
