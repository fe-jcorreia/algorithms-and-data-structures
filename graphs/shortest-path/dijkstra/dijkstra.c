#include <stdio.h>
#include <stdlib.h>

#include "dijkstra.h"

#define PROCESSED 'P'
#define UNPROCESSED 0
#define INT_MAX 999999999

int findIndex(Heap *h, int index)
{
  Vector *array = h->array;
  for (int i = 0; i < array->length; i++)
    if (array->array[i].index == index)
      return i;
}

void dijkstra(Graph *graph, int initialVertex)
{
  if (initialVertex < 0 || initialVertex >= graph->totalVertices)
  {
    printf("ERROR: Vertex invalid\n");
    exit(EXIT_FAILURE);
  }

  char *status = calloc(graph->totalVertices, sizeof(char));
  int *totalDistance = calloc(graph->totalVertices, sizeof(int));
  int *parent = calloc(graph->totalVertices, sizeof(int));

  Heap *distance = initHeap();
  Tuple *d = distance->array->array;

  parent[initialVertex] = -1;

  for (int i = 0; i < graph->totalVertices; i++)
  {
    if (i != initialVertex)
      insertHeap(distance, INT_MAX, i);
    else
      insertHeap(distance, 0, initialVertex);
  }

  printHeap(distance);

  int currentIndex = initialVertex;
  while (!isEmptyHeap(distance))
  {
    currentIndex = getMin(distance).index;
    if (status[currentIndex] == UNPROCESSED)
    {
      int currentHeapIndex = findIndex(distance, currentIndex);
      LinkedListNode *node = graph->adjList[currentIndex]->head;

      while (node != NULL)
      {
        int nextHeapIndex = findIndex(distance, node->data);
        if (d[nextHeapIndex].data > d[currentHeapIndex].data + node->weight)
        {
          printf("%d: %d\n", node->data, node->weight);
          printf("%d\n", nextHeapIndex);
          for (int i = 0; i < distance->array->length; i++)
            printf("(%d, %d) ", d[i].data, d[i].index);
          printf("(%d, %d)\n", d[nextHeapIndex].data, d[nextHeapIndex].index);
          printf("%d > %d + %d\n", d[nextHeapIndex].data, d[currentHeapIndex].data, node->weight);
          d[nextHeapIndex].data = d[currentHeapIndex].data + node->weight;
          printf("%d\n", d[nextHeapIndex].data);
          siftUp(distance, nextHeapIndex);
          siftDown(distance, findIndex(distance, node->data));
          parent[node->data] = currentIndex;

          printHeap(distance);
        }

        node = node->next;
      }
    }

    status[currentIndex] = PROCESSED;
    totalDistance[currentIndex] = getMin(distance).data;
    currentIndex = extractMin(distance).index;
  }

  for (int i = 0; i < graph->totalVertices; i++)
    printf("%d ", totalDistance[i]);

  printf("\n");
  printf("\n");

  for (int i = 0; i < graph->totalVertices; i++)
    printf("%d ", parent[i]);

  printf("\n");
  printf("\n");
}
