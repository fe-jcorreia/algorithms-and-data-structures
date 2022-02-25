#ifndef PROJECT_NONTAILED_SINGLY_LINKED_LIST_H
#define PROJECT_NONTAILED_SINGLY_LINKED_LIST_H

typedef struct linkedListNode
{
  int data;
  struct linkedListNode *next;
} LinkedListNode;

typedef struct SinglyLinkedList
{
  int length;
  struct linkedListNode *head;
} SinglyLinkedList;

SinglyLinkedList *initList();
int isEmpty(SinglyLinkedList *list);
int at(SinglyLinkedList *list, int index);
void pushFront(SinglyLinkedList *list, int data);
void popFront(SinglyLinkedList *list);
void pushBack(SinglyLinkedList *list, int data);
void popBack(SinglyLinkedList *list);
int front(SinglyLinkedList *list);
int back(SinglyLinkedList *list);
void insert(SinglyLinkedList *list, int data, int index);
void printList(SinglyLinkedList *list);

#endif
