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
BSTNode *createNode(int value, BSTNode *parent);
void insertInBST(BST *tree, int value);
int getBSTNodeCount(BST *tree);
int isInBST(BST *tree, int value);
int getBSTHeight(BST *tree);
int getMin(BST *tree);
int getMax(BST *tree);
void deleteValueBST(BST *tree, int value);
int isBST(BST *tree);
int getSuccessorBST(BST* tree, int value);
void printBST(BST *tree);
void destroyTree(BST *tree);

void run_all_tests();
void test_initBST();
void test_insertInBST();
void test_getBSTNodeCount();
void test_isInBST();
void test_getBSTHeight();
void test_getMin();
void test_getMax();
void test_isBST();
void test_deleteValueBST();
void test_getSuccessorBST();

#endif
