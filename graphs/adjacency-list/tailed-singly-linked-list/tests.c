#include <stdio.h>
#include <assert.h>
#include "tailed-singly-linked-list.h"

void run_all_tests()
{
  test_initList();
  test_isEmpty();
  test_at();
  test_pushFront();
  test_popFront();
  test_pushBack();
  test_popBack();
  test_front();
  test_back();
  test_insert();
  test_erase();
  test_valueNFromEnd();
  test_reverse();
  test_removeFirstValue();
}

void test_initList()
{
  SinglyLinkedList *list = initList();

  assert(list->length == 0);
  assert(list->head == NULL);
  assert(list->tail == NULL);

  destroyList(list);
  printf("Test initVector: OK\n");
}

void test_isEmpty()
{
  SinglyLinkedList *list = initList();
  assert(isEmpty(list) == 1);
  assert(list->tail == list->head);

  pushFront(list, 15);
  assert(isEmpty(list) == 0);
  assert(list->tail == list->head);

  destroyList(list);

  printf("Test isEmpty: OK\n");
}

void test_at()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 9; i++)
    pushFront(list, i);

  assert(at(list, 6) == 2);
  assert(at(list, 8) == 0);

  destroyList(list);

  printf("Test at: OK\n");
}

void test_pushFront()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 3; i++)
    pushFront(list, i);

  assert(at(list, 0) == 2);
  assert(at(list, 1) == 1);
  assert(at(list, 2) == 0);

  destroyList(list);

  printf("Test pushFront: OK\n");
}

void test_popFront()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 9; i++)
    pushFront(list, i);

  popFront(list);
  assert(at(list, 0) == 7);
  popFront(list);
  assert(at(list, 0) == 6);
  assert(list->length == 7);

  destroyList(list);

  printf("Test popFront: OK\n");
}

void test_pushBack()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 9; i++)
    pushBack(list, i);

  assert(at(list, 0) == 0);
  assert(at(list, 1) == 1);
  assert(at(list, 2) == 2);
  assert(list->length == 9);

  destroyList(list);

  printf("Test pushBack: OK\n");
}

void test_popBack()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 9; i++)
    pushBack(list, i);

  assert(list->length == 9);
  popBack(list);
  assert(list->length == 8);
  popBack(list);
  assert(list->length == 7);

  assert(at(list, 6) == 6);

  destroyList(list);

  printf("Test popBack: OK\n");
}

void test_front()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 9; i++)
    pushBack(list, i);

  assert(front(list) == 0);

  destroyList(list);

  printf("Test front: OK\n");
}

void test_back()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 9; i++)
    pushBack(list, i);

  assert(back(list) == 8);

  destroyList(list);

  printf("Test back: OK\n");
}

void test_insert()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 9; i++)
    pushBack(list, i);

  insert(list, 40, 0);
  assert(at(list, 0) == 40);
  insert(list, 40, 9);
  assert(at(list, 9) == 40);
  insert(list, 40, 5);
  assert(at(list, 5) == 40);

  destroyList(list);

  printf("Test insert: OK\n");
}

void test_erase()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 9; i++)
    pushBack(list, i);

  erase(list, 0);
  assert(at(list, 0) == 1);
  erase(list, 7);
  assert(at(list, 6) == 7);
  assert(list->length == 7);
  erase(list, 3);
  assert(at(list, 3) == 5);

  destroyList(list);

  printf("Test erase: OK\n");
}

void test_valueNFromEnd()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 9; i++)
    pushBack(list, i);

  assert(valueNFromEnd(list, 0) == 8);
  assert(valueNFromEnd(list, 1) == 7);
  assert(valueNFromEnd(list, 2) == 6);

  destroyList(list);

  printf("Test valueNFromEnd: OK\n");
}

void test_reverse()
{
  SinglyLinkedList *list = initList();

  for (int i = 0; i < 5; i++)
    pushBack(list, i);

  reverse(list);
  assert(at(list, 0) == 4);
  assert(at(list, 1) == 3);
  assert(at(list, 2) == 2);
  assert(at(list, 3) == 1);
  assert(at(list, 4) == 0);
  destroyList(list);

  printf("Test reverse: OK\n");
}

void test_removeFirstValue()
{
  SinglyLinkedList *list = initList();

  pushBack(list, 10);
  pushBack(list, 10);
  pushBack(list, 5);
  pushBack(list, 10);

  removeFirstValue(list, 5);
  assert(at(list, 2) == 10);
  removeFirstValue(list, 10);
  assert(at(list, 0) == 10);
  assert(list->length == 2);
  removeFirstValue(list, 10);
  removeFirstValue(list, 10);
  assert(list->length == 0);
  
  destroyList(list);

  printf("Test removeFirstValue: OK\n");
}