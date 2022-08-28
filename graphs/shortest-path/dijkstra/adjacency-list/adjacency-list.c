#include <stdio.h>
#include <stdlib.h>

#include "adjacency-list.h"

Graph *initGraph(int totalCapacity)
{
  Graph *graph = (Graph *)malloc(sizeof(Graph));
  graph->totalVertices = 0;
  graph->totalCapacity = totalCapacity;
  graph->adjList = malloc(graph->totalCapacity * sizeof(SinglyLinkedList *));

  for (int i = 0; i < graph->totalCapacity; i++)
    graph->adjList[i] = initList();

  return graph;
}

int isEmptyGraph(Graph *graph)
{
  if (graph->totalVertices)
    return 0;
  else
    return 1;
}

void insertEdge(Graph *graph, int s, int d, int weight)
{
  if ((d < 0 || s < 0) && (d >= graph->totalVertices || s >= graph->totalVertices))
  {
    printf("ERROR: Vertex not found\n");
    exit(EXIT_FAILURE);
  }

  SinglyLinkedList *list = graph->adjList[d];
  pushBack(list, s, weight);

  list = graph->adjList[s];
  pushBack(list, d, weight);
}

void addVertex(Graph *graph)
{
  if (graph->totalVertices + 1 <= graph->totalCapacity)
    graph->totalVertices++;
  else
    printf("Maximum capacity reached\n");
}

void eraseVertex(Graph *graph, int vertex)
{
  if (vertex == graph->totalVertices - 1)
  {
    destroyList(graph->adjList[vertex]);
    free(graph->adjList[vertex]);
    graph->totalVertices--;
  }
  else
  {
    destroyList(graph->adjList[vertex]);

    for (int i = vertex; i < graph->totalVertices - 1; i++)
      *(graph->adjList + i) = *(graph->adjList + i + 1);

    graph->adjList[graph->totalVertices] = NULL;
    graph->totalVertices--;
  }

  for (int i = 0; i < graph->totalVertices; i++)
  {
    removeFirstValue(graph->adjList[i], vertex);

    LinkedListNode *node = graph->adjList[i]->head;
    while (node != NULL)
    {
      if (node->data > vertex)
        node->data--;
      node = node->next;
    }
  }
}

void destroyGraph(Graph *graph)
{
  for (int i = 0; i < graph->totalVertices; i++)
    destroyList(graph->adjList[i]);

  free(graph);
}

void printGraph(Graph *graph)
{
  printf("Total Vertices: %d\n", graph->totalVertices);
  if (graph->totalVertices == 0)
    printf("Graph is empty\n");
  else
    for (int i = 0; i < graph->totalVertices; i++)
    {
      printf("%d: ", i);
      printList(graph->adjList[i]);
    }
}
