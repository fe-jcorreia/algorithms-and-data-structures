#include <stdio.h>
#include <stdlib.h>

#include "adjacency-matrix.h"

Graph *initGraph(int initialCapacity)
{
  Graph *graph = (Graph *)malloc(sizeof(Graph));
  graph->totalVertices = initialCapacity;
  graph->adjMatrix = malloc(graph->totalVertices * sizeof(Vector *));

  for (int i = 0; i < graph->totalVertices; i++)
  {
    graph->adjMatrix[i] = initVector();

    for (int j = 0; j < graph->totalVertices; j++)
      push(graph->adjMatrix[i], 0);
  }

  return graph;
}

int isEmptyGraph(Graph *graph)
{
  if (graph->totalVertices)
    return 0;
  else
    return 1;
}

void insertEdge(Graph *graph, int s, int d)
{
  if ((d < 0 || s < 0) && (d >= graph->totalVertices || s >= graph->totalVertices))
  {
    printf("ERROR: Vertex not found\n");
    exit(EXIT_FAILURE);
  }

  graph->adjMatrix[s]->array[d] = 1;
  graph->adjMatrix[d]->array[s] = 1;
}

void destroyGraph(Graph *graph)
{
  for (int i = 0; i < graph->totalVertices; i++)
    destroyVector(graph->adjMatrix[i]);

  free(graph->adjMatrix);
  free(graph);
}

void printGraph(Graph *graph)
{
  printf("Total Vertices: %d\n", graph->totalVertices);
  if (graph->totalVertices == 0)
    printf("Graph is empty\n");
  else
    for (int i = 0; i < graph->totalVertices; i++)
      printVector(graph->adjMatrix[i]);

  printf("\n");
}
