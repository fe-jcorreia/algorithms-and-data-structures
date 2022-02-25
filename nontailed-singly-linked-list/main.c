#include <stdio.h>
#include "nontailed-singly-linked-list.h"

int main()
{
  SinglyLinkedList *list = initList();
  printf("%d\n", isEmpty(list));
  pushFront(list, 3);
  pushFront(list, 4);
  printList(list);
}