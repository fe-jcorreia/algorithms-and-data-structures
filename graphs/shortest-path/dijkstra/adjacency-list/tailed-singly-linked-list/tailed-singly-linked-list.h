#ifndef PROJECT_TAILED_SINGLY_LINKED_LIST_H
#define PROJECT_TAILED_SINGLY_LINKED_LIST_H

typedef struct linkedListNode
{
  int data;
  int weight;
  struct linkedListNode *next;
} LinkedListNode;

typedef struct SinglyLinkedList
{
  int length;
  struct linkedListNode *head;
  struct linkedListNode *tail;
} SinglyLinkedList;

SinglyLinkedList *initList();
int isEmpty(SinglyLinkedList *list);
int atOnList(SinglyLinkedList *list, int index);
void pushFront(SinglyLinkedList *list, int data, int weight);
void popFront(SinglyLinkedList *list);
void pushBack(SinglyLinkedList *list, int data, int weight);
void popBack(SinglyLinkedList *list);
int front(SinglyLinkedList *list);
int back(SinglyLinkedList *list);
void insertOnList(SinglyLinkedList *list, int data, int weight, int index);
void erase(SinglyLinkedList *list, int index);
int valueNFromEnd(SinglyLinkedList *list, int index);
void reverse(SinglyLinkedList *list);
void removeFirstValue(SinglyLinkedList *list, int value);
void destroyList(SinglyLinkedList *list);
void printList(SinglyLinkedList *list);

void run_all_tests();
void test_initList();
void test_isEmpty();
void test_atOnList();
void test_pushFront();
void test_popFront();
void test_pushBack();
void test_popBack();
void test_front();
void test_back();
void test_insertOnList();
void test_erase();
void test_valueNFromEnd();
void test_reverse();
void test_removeFirstValue();

#endif
