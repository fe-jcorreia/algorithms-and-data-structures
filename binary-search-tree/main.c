#include <stdio.h>
#include "binary-search-tree.h"

int main()
{
  BST *tree = initBST();
  insertInBST(tree, 15);
  insertInBST(tree, 45);
  insertInBST(tree, 9);
  insertInBST(tree, 9);
  insertInBST(tree, 10);
  insertInBST(tree, 1);
  insertInBST(tree, 2);
  insertInBST(tree, 30);
  insertInBST(tree, 53);
  insertInBST(tree, 47);
  insertInBST(tree, 20);
  // printBST(tree);

  // printf("%d\n", getBSTNodeCount(tree));

  // printf("10: %d\n", isInBST(tree, 10));
  // printf("20: %d\n", isInBST(tree, 20));
  // printf("2: %d\n", isInBST(tree, 2));
  // printf("45: %d\n", isInBST(tree, 45));
  // printf("15: %d\n", isInBST(tree, 15));
  // printf("53: %d\n", isInBST(tree, 53));
  // printf("13: %d\n", isInBST(tree, 13));
  // printf("3: %d\n", isInBST(tree, 3));
  // printf("46: %d\n", isInBST(tree, 46));

  // printf("height: %d\n", getBSTHeight(tree));

  // printf("min: %d\n", getMin(tree));
  // printf("max: %d\n", getMax(tree));

  // deleteValueBST(tree, 45);
  // printBST(tree);

  

  printf("\n");

  return 0;
}