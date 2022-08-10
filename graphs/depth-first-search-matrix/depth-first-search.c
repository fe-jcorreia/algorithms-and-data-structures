#include <stdio.h>
#include <stdlib.h>

#include "depth-first-search.h"

#define PROCESSED 'P'
#define DISCOVERED 'D'
#define UNDISCOVERED 0

void processVertexInit(int v)
{
  printf("Starting vertex %d processing...\n", v);
}

void processVertexEnd(int v)
{
  printf("Vertex %d processed.\n", v);
}

void processEdge(int v, int w)
{
  printf("Edge (%d, %d) processed.\n", v, w);
}

void depthFirstSearch(Graph *graph, int initialVertex, char *status, int *parent)
{
  status[initialVertex] = DISCOVERED;
  processVertexInit(initialVertex);

  for (int i = 0; i < graph->adjMatrix[initialVertex]->length; i++)
  {
    if (graph->adjMatrix[initialVertex]->array[i] == 1)
    {
      if (status[i] == UNDISCOVERED)
      {
        parent[i] = initialVertex;
        processEdge(initialVertex, i);
        depthFirstSearch(graph, i, status, parent);
      }
      else if (status[i] == DISCOVERED && parent[initialVertex] != i)
      {
        processEdge(initialVertex, i);
      }
    }
  }

  status[initialVertex] = PROCESSED;
  processVertexEnd(initialVertex);
}

void DFS(Graph *graph, int initialVertex)
{
  char *status = malloc(graph->totalVertices * sizeof(char));
  int *parent = calloc(graph->totalVertices, sizeof(int));

  if (initialVertex < 0 || initialVertex >= graph->totalVertices)
  {
    printf("ERROR: Vertex invalid\n");
    exit(EXIT_FAILURE);
  }

  depthFirstSearch(graph, initialVertex, status, parent);
}
