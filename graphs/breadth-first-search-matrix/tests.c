#include <stdio.h>
#include <assert.h>
#include "breadth-first-search.h"

void run_all_tests()
{
  test_BFS();
}

void test_BFS()
{
  Graph *graph = initGraph(9);

  insertEdge(graph, 0, 1);
  insertEdge(graph, 1, 2);
  insertEdge(graph, 1, 3);
  insertEdge(graph, 1, 4);
  insertEdge(graph, 3, 6);
  insertEdge(graph, 3, 5);
  insertEdge(graph, 3, 4);
  insertEdge(graph, 6, 7);
  insertEdge(graph, 5, 7);
  insertEdge(graph, 7, 8);

  BFS(graph, 0);

  destroyGraph(graph);
  printf("Test BFS: OK\n");
}
