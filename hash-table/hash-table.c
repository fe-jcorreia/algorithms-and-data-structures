#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "hash-table.h"

#define BIG_PRIME 44263
#define A 39048
#define B 16147

HashTable *initHashTable()
{
  HashTable *ht = (HashTable *)malloc(sizeof(HashTable));
  Item *list = (Item *)calloc(8, sizeof(Item));
  ht->list = list;
  ht->length = 0;
  ht->capacity = 8;

  return ht;
}

int hash(char *key, int m, int trial)
{
  if (key[0] == '\0')
    return -1;

  int hash = 0;

  for (int i = 0; key[i] != '\0'; i++)
    hash += (A * key[i]);

  hash = (hash + B) % BIG_PRIME;

  return (hash + trial) % m;
}

void add(HashTable *ht, char *key, int value)
{
  int trial, index = 0;
  Item item = *(ht->list);

  for (int trial = 0; trial < ht->capacity; trial++)
  {
    index = hash(key, ht->capacity, trial);
    item = *(ht->list + index);

    if (item.key == NULL || item.key == key || !strcmp(item.key, "_deleted_value"))
    {
      (ht->list + index)->key = key;
      (ht->list + index)->value = value;
      if (item.key != key)
        ht->length++;
      break;
    }
  }

  if (ht->length > (2 * ht->capacity) / 3)
    resizeHashTable(ht, 2 * ht->capacity);
}

int exists(HashTable *ht, char *key)
{
  if (get(ht, key) == -1)
    return 0;
  else
    return 1;
}

int get(HashTable *ht, char *key)
{
  int index = 0;
  Item item = *(ht->list);

  for (int trial = 0; trial < ht->capacity; trial++)
  {
    index = hash(key, ht->capacity, trial);
    item = *(ht->list + index);

    if (item.key == NULL)
      return -1;

    if (item.key == key)
      return item.value;
  }

  return -1;
}

void removeKey(HashTable *ht, char *key)
{
  int index = 0;
  Item item = *(ht->list);

  for (int trial = 0; trial < ht->capacity; trial++)
  {
    index = hash(key, ht->capacity, trial);
    item = *(ht->list + index);

    if (item.key == NULL)
      return;

    if (item.key == key)
    {
      (ht->list + index)->key = "_deleted_value";
      ht->length--;

      if (ht->length < ht->capacity / 4)
        resizeHashTable(ht, ht->capacity / 2);

      break;
    }
  }
}

void resizeHashTable(HashTable *ht, int capacity)
{
  Item *new_list = (Item *)calloc(capacity, sizeof(Item));

  for (int i = 0; i < ht->capacity; i++)
  {
    Item old_item = *(ht->list + i);
    if (old_item.key == NULL || !strcmp(old_item.key, "_deleted_value"))
      continue;

    int index = 0;
    Item new_item = *(new_list);

    for (int trial = 0; trial < capacity; trial++)
    {
      index = hash(old_item.key, capacity, trial);
      new_item = *(new_list + index);

      if (new_item.key == NULL)
      {
        (new_list + index)->key = old_item.key;
        (new_list + index)->value = old_item.value;
        break;
      }
    }
  }

  ht->capacity = capacity;
  free(ht->list);
  ht->list = new_list;
}

void destroyHashTable(HashTable *ht)
{
  free(ht->list);
  free(ht);
}

void printHashTable(HashTable *ht)
{
  printf("Length: %d\n", ht->length);
  printf("Capacity: %d\n", ht->capacity);

  for (int i = 0; i < ht->capacity; i++)
  {
    Item item = *(ht->list + i);
    printf("%s: %d\n", item.key, item.value);
  }

  printf("\n");
}
