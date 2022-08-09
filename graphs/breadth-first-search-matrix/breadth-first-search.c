#include <stdio.h>
#include <stdlib.h>

#include "breadth-first-search.h"

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

void BFS(Graph *graph, int initialVertex)
{
  char *status = malloc(graph->totalVertices * sizeof(char));
  Queue *q = initQueue(graph->totalVertices);
  int *parent = calloc(graph->totalVertices, sizeof(int));

  if (initialVertex < 0 || initialVertex >= graph->totalVertices)
  {
    printf("ERROR: Vertex invalid\n");
    exit(EXIT_FAILURE);
  }

  status[initialVertex] = DISCOVERED;
  enqueue(q, initialVertex);

  while (!isQueueEmpty(q))
  {
    int currentVertex = dequeue(q);

    processVertexInit(currentVertex);

    for (int i = 0; i < graph->adjMatrix[currentVertex]->length; i++)
    {
      if (graph->adjMatrix[currentVertex]->array[i] == 1)
      {
        int nextVertex = i;

        if (status[nextVertex] != PROCESSED)
          processEdge(currentVertex, nextVertex);

        if (status[nextVertex] == UNDISCOVERED)
        {
          status[nextVertex] = DISCOVERED;
          enqueue(q, nextVertex);
          parent[nextVertex] = currentVertex;
        }
      }
    }

    processVertexEnd(currentVertex);
    status[currentVertex] = PROCESSED;
  }
}
