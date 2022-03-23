#include <stdio.h>
#include <assert.h>
#include "binary-search-tree.h"

void run_all_tests()
{
  test_initBST();
  test_insertInBST();
  test_getBSTNodeCount();
  test_isInBST();
  test_getBSTHeight();
  test_getMin();
  test_getMax();
  test_isBST();
  test_deleteValueBST();
  test_getSuccessorBST();
}

void test_initBST()
{
  BST *tree = initBST();
  assert(tree->root == NULL);
  destroyTree(tree);
  printf("Test initBST: OK\n");
}

void test_insertInBST()
{
  BST *tree = initBST();
  insertInBST(tree, 15);
  insertInBST(tree, 45);
  insertInBST(tree, 9);
  insertInBST(tree, 9);
  insertInBST(tree, 10);
  insertInBST(tree, 30);
  insertInBST(tree, 53);

  assert(tree->root->data == 15);
  assert(tree->root->left->data == 9);
  assert(tree->root->right->data == 45);
  assert(tree->root->left->left->data == 9);
  assert(tree->root->left->right->data == 10);
  assert(tree->root->right->left->data == 30);
  assert(tree->root->right->right->data == 53);
  destroyTree(tree);
  printf("Test insertInBST: OK\n");
}

void test_getBSTNodeCount()
{
  BST *tree = initBST();
  insertInBST(tree, 15);
  insertInBST(tree, 45);
  insertInBST(tree, 9);
  insertInBST(tree, 9);
  insertInBST(tree, 10);
  insertInBST(tree, 30);
  insertInBST(tree, 53);

  assert(getBSTNodeCount(tree) == 7);
  destroyTree(tree);
  printf("Test getBSTNodeCount: OK\n");
}

void test_isInBST()
{
  BST *tree = initBST();
  insertInBST(tree, 15);
  insertInBST(tree, 45);
  insertInBST(tree, 9);
  insertInBST(tree, 9);
  insertInBST(tree, 10);
  insertInBST(tree, 30);
  insertInBST(tree, 53);

  assert(isInBST(tree, 15) == 1);
  assert(isInBST(tree, 45) == 1);
  assert(isInBST(tree, 10) == 1);
  assert(isInBST(tree, 25) == 0);
  destroyTree(tree);
  printf("Test isInBST: OK\n");
}

void test_getBSTHeight()
{
  BST *tree = initBST();
  insertInBST(tree, 15);
  insertInBST(tree, 45);
  insertInBST(tree, 9);
  insertInBST(tree, 9);
  insertInBST(tree, 10);
  insertInBST(tree, 30);
  insertInBST(tree, 53);

  assert(getBSTHeight(tree) == 3);
  insertInBST(tree, 1);
  assert(getBSTHeight(tree) == 4);
  destroyTree(tree);
  printf("Test getBSTHeight: OK\n");
}

void test_getMin()
{
  BST *tree = initBST();
  insertInBST(tree, 15);
  insertInBST(tree, 45);
  insertInBST(tree, 9);
  insertInBST(tree, 9);
  insertInBST(tree, 10);
  insertInBST(tree, 30);
  insertInBST(tree, 53);

  assert(getMin(tree) == 9);
  insertInBST(tree, 1);
  assert(getMin(tree) == 1);
  destroyTree(tree);
  printf("Test getMin: OK\n");
}

void test_getMax()
{
  BST *tree = initBST();
  insertInBST(tree, 15);
  insertInBST(tree, 45);
  insertInBST(tree, 9);
  insertInBST(tree, 9);
  insertInBST(tree, 10);
  insertInBST(tree, 30);
  insertInBST(tree, 53);

  assert(getMax(tree) == 53);
  insertInBST(tree, 60);
  assert(getMax(tree) == 60);
  destroyTree(tree);
  printf("Test getMax: OK\n");
}

void test_isBST()
{
  BST *tree = initBST();
  BST *tree2 = initBST();
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

  tree2->root = createNode(16, NULL);
  tree2->root->left = createNode(12, tree->root);
  tree2->root->right = createNode(20, tree->root);
  tree2->root->left->left = createNode(6, tree->root->left);
  tree2->root->left->right = createNode(3, tree->root->left);

  assert(isBST(tree) == 1);
  assert(isBST(tree2) == 0);

  destroyTree(tree);
  printf("Test isBST: OK\n");
}

void test_deleteValueBST() {
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

  deleteValueBST(tree, 45);
  assert(tree->root->right->data == 30);
  deleteValueBST(tree, 53);
  assert(tree->root->right->right->data == 47);
  deleteValueBST(tree, 47);
  assert(tree->root->right->right == NULL);

  destroyTree(tree);
  printf("Test deleteValueBST: OK\n");
}

void test_getSuccessorBST() {
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

  assert(getSuccessorBST(tree, 1) == 2);
  assert(getSuccessorBST(tree, 2) == 9);
  assert(getSuccessorBST(tree, 9) == 10);
  assert(getSuccessorBST(tree, 10) == 15);
  assert(getSuccessorBST(tree, 15) == 20);
  assert(getSuccessorBST(tree, 20) == 30);
  assert(getSuccessorBST(tree, 30) == 45);
  assert(getSuccessorBST(tree, 45) == 47);
  assert(getSuccessorBST(tree, 47) == 53);
  assert(getSuccessorBST(tree, 53) == -1);
  assert(getSuccessorBST(tree, 13) == -1);

  destroyTree(tree);
  printf("Test getSuccessorBST: OK\n");
}