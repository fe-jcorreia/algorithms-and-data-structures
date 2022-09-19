#ifndef PROJECT_TAILED_SINGLY_LINKED_LIST_H
#define PROJECT_TAILED_SINGLY_LINKED_LIST_H

typedef struct linkedListNode
{
  int data;
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
int at(SinglyLinkedList *list, int index);
void pushFront(SinglyLinkedList *list, int data);
void popFront(SinglyLinkedList *list);
void pushBack(SinglyLinkedList *list, int data);
void popBack(SinglyLinkedList *list);
int front(SinglyLinkedList *list);
int back(SinglyLinkedList *list);
void insert(SinglyLinkedList *list, int data, int index);
void erase(SinglyLinkedList *list, int index);
int valueNFromEnd(SinglyLinkedList *list, int index);
void reverse(SinglyLinkedList *list);
void removeFirstValue(SinglyLinkedList *list, int value);
void destroyList(SinglyLinkedList *list);
void printList(SinglyLinkedList *list);

void run_all_tests();
void test_initList();
void test_isEmpty();
void test_at();
void test_pushFront();
void test_popFront();
void test_pushBack();
void test_popBack();
void test_front();
void test_back();
void test_insert();
void test_erase();
void test_valueNFromEnd();
void test_reverse();
void test_removeFirstValue();

#endif
