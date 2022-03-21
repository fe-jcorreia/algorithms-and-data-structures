#include <stdio.h>
#include <stdlib.h>

#include "binary-search-tree.h"

BST *initBST()
{
  BST *tree = (BST *)malloc(sizeof(BST));
  tree->root = NULL;

  return tree;
}

BSTNode *createNode(int value, BSTNode *parent)
{
  BSTNode *node = (BSTNode *)malloc(sizeof(BSTNode));
  node->left = NULL;
  node->right = NULL;
  node->parent = parent;
  node->data = value;

  return node;
}

BSTNode *insert(BSTNode *root, int value, BSTNode *parent)
{
  if (root == NULL)
    root = createNode(value, parent);

  else if (value <= root->data)
    root->left = insert(root->left, value, root);

  else if (value > root->data)
    root->right = insert(root->right, value, root);

  return root;
}

void insertInBST(BST *tree, int value)
{
  tree->root = insert(tree->root, value, NULL);
}

int getNodeCount(BSTNode *root)
{
  if (!root)
    return 0;

  return 1 + getNodeCount(root->left) + getNodeCount(root->right);
}

int getBSTNodeCount(BST *tree)
{
  getNodeCount(tree->root);
}

int isInTree(BSTNode *root, int value)
{
  if (!root)
    return 0;

  if (root->data == value)
    return 1;

  else if (value <= root->data)
    return isInTree(root->left, value);

  else if (value > root->data)
    return isInTree(root->right, value);
}

int isInBST(BST *tree, int value)
{
  return isInTree(tree->root, value);
}

int max(int value1, int value2)
{
  if (value1 > value2)
    return value1;
  else
    return value2;
}

int getHeight(BSTNode *root)
{
  if (!root)
    return 0;

  return 1 + max(getHeight(root->left), getHeight(root->right));
}

int getBSTHeight(BST *tree)
{
  return getHeight(tree->root);
}

int getMin(BST *tree)
{
  BSTNode *node = tree->root;
  while (node->left != NULL)
    node = node->left;

  return node->data;
}

int getMax(BST *tree)
{
  BSTNode *node = tree->root;
  while (node->right != NULL)
    node = node->right;

  return node->data;
}

BSTNode *getMaxNode(BSTNode *node)
{
  while (node->right != NULL)
    node = node->right;

  return node;
}

BSTNode *deleteValue(BSTNode *root, int value)
{
  if (!root)
    return root;

  else if (value < root->data)
    root->left = deleteValue(root->left, value);

  else if (value > root->data)
    root->right = deleteValue(root->right, value);

  else if (root->data == value)
  {
    BSTNode *node = root;
    if (!root->left && !root->right)
    {
      root = NULL;
      free(node);
    }

    else if (!root->left)
    {
      root = root->right;
      root->parent = node->parent;
      free(node);
    }

    else if (!root->right)
    {
      root = root->left;
      root->parent = node->parent;
      free(node);
    }

    else
    {
      BSTNode *temp = getMaxNode(root->left);
      root->data = temp->data;
      root->left = deleteValue(root->left, temp->data);
    }
  }
  return root;
}

void deleteValueBST(BST *tree, int value)
{
  deleteValue(tree->root, value);
}

int isBinarySearchTree() {}

int getSuccessor() {}

void printTree(BSTNode *root)
{
  if (!root)
    return;

  printTree(root->left);
  printf("==========\n");
  printf("data: %d ", root->data);
  if (root->parent)
    printf("parent %d\n", root->parent->data);
  else
    printf("parent: NULL\n");
  printf("==========\n");
  printTree(root->right);
}

void printBST(BST *tree)
{
  printTree(tree->root);
}

void destroyTree(BST *tree) {}
