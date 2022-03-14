#ifndef PROJECT_HASH_TABLE_H
#define PROJECT_HASH_TABLE_H

typedef struct item {
  char *key;
  int value;
} Item;

typedef struct hashTable
{
  int length;
  int capacity;
  Item *list;
} HashTable;

HashTable *initHashTable();
int hash(char *key, int m, int trial);
void add(HashTable *ht, char *key, int value);
int exists(HashTable *ht, char *key);
int get(HashTable *ht, char *key);
void removeKey(HashTable *ht, char *key);
void resizeHashTable(HashTable *ht, int capacity);
void destroyHashTable(HashTable *ht);
void printHashTable(HashTable *ht);

void run_all_tests();
void test_initHashTable();
void test_add();
void test_exists();
void test_get();
void test_removeKey();

#endif
