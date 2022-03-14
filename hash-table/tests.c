#include <stdio.h>
#include <assert.h>
#include "hash-table.h"

void run_all_tests()
{
  test_initHashTable();
  test_add();
  test_exists();
  test_get();
  test_removeKey();
}

void test_initHashTable()
{
  HashTable *table = initHashTable();

  assert(table->length == 0);
  assert(table->capacity == 8);
  for (int i = 0; i < table->capacity; i++)
  {
    assert((table->list + i)->key == NULL);
    assert((table->list + i)->value == 0);
  }

  destroyHashTable(table);
  printf("Test initHashTable: OK\n");
}

void test_add()
{
  HashTable *table = initHashTable();

  add(table, "maça", 43);
  add(table, "pera", 56);
  add(table, "uva", 123);
  assert(table->length == 3);
  add(table, "abacaxi", 94);
  add(table, "cenoura", 57);
  add(table, "batata", 60);
  assert(table->capacity == 16);

  destroyHashTable(table);
  printf("Test add: OK\n");
}

void test_exists()
{
  HashTable *table = initHashTable();

  add(table, "maça", 43);
  add(table, "pera", 56);
  add(table, "uva", 123);
  assert(exists(table, "maça") == 1);
  assert(exists(table, "uva") == 1);
  assert(exists(table, "cenoura") == 0);

  destroyHashTable(table);
  printf("Test exists: OK\n");
}

void test_get()
{
  HashTable *table = initHashTable();

  add(table, "maça", 43);
  add(table, "pera", 56);
  add(table, "uva", 123);
  removeKey(table, "uva");
  assert(get(table, "maça") == 43);
  assert(get(table, "uva") == -1);
  assert(get(table, "cenoura") == -1);

  destroyHashTable(table);
  printf("Test get: OK\n");
}

void test_removeKey()
{
  HashTable *table = initHashTable();

  add(table, "maça", 43);
  add(table, "pera", 56);
  add(table, "uva", 123);
  removeKey(table, "maça");
  removeKey(table, "pera");
  assert(table->capacity == 4);
  removeKey(table, "uva");
  assert(table->capacity == 2);
  assert(get(table, "maça") == -1);
  assert(get(table, "pera") == -1);
  assert(get(table, "uva") == -1);

  destroyHashTable(table);
  printf("Test removeKey: OK\n");
}
