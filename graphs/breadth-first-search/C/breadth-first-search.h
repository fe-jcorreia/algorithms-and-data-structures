#ifndef PROJECT_BREADTH_FIRST_SEARCH_H
#define PROJECT_BREADTH_FIRST_SEARCH_H

#include "./adjacency-list/adjacency-list.h"
#include "./array-queue/queue.h"

void BFS(Graph *graph, int initialVertex);

void run_all_tests();
void test_BFS();

#endif
