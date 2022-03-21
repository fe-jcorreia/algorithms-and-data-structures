#ifndef PROJECT_BINARY_SEARCH_TREE_H
#define PROJECT_BINARY_SEARCH_TREE_H

typedef struct bstNode
{
  int data;
  struct bstNode *left;
  struct bstNode *right;
  struct bstNode *parent;
} BSTNode;

typedef struct bst
{
  struct bstNode *root;
} BST;

BST *initBST();
void insertInBST(BST *tree, int value);
int getBSTNodeCount(BST *tree);
int isInBST(BST *tree, int value);
int getBSTHeight(BST *tree);
int getMin(BST *tree);
int getMax(BST *tree);
void deleteValueBST(BST *tree, int value);
int isBinarySearchTree();
int getSuccessor();
void printBST(BST *tree);
void destroyTree(BST *tree);

void run_all_tests();
void test_insert();
void test_getNodeCount();
void test_isInTree();
void test_getHeight();
void test_getMin();
void test_getMax();
void test_isBinarySearchTree();
void test_deleteValue();
void test_getSuccessor();

#endif
