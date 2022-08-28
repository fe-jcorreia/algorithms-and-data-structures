#ifndef PROJECT_DIJKSTRA_H
#define PROJECT_DIJKSTRA_H

#include "./adjacency-list/adjacency-list.h"
#include "heap/heap.h"

void dijkstra(Graph *graph, int initialVertex);

void run_all_tests();
void test_dijkstra();

#endif
