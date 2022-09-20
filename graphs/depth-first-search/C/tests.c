#include <stdio.h>
#include <assert.h>
#include "depth-first-search.h"

void run_all_tests()
{
  test_DFS();
}

void test_DFS()
{
  Graph *graph = initGraph(10);

  for (int i = 0; i < 9; i++)
    addVertex(graph);

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

  DFS(graph, 0);

  destroyGraph(graph);
  printf("Test DFS: OK\n");
}
