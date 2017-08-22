/*
 * =====================================================================================
 *
 *       Filename:  link_list.c
 *
 *    Description:  Linked list => LRU based implementation
 *
 *        Version:  1.0
 *        Created:  08/21/2017 09:21:11 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */


#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

typedef struct _link_ {
  struct _link_ *next;
  struct _link_ *prev;
} link;


typedef struct _node_ {
  link l;
  int val;
} node;


void
_list_init (link *l)
{
  l->next = l;
  l->prev = l;
}

void
_list_add (link *prev, link *next, link *l)
{
  prev->next  = l;
  l->prev     = prev;

  next->prev  = l;
  l->next     = next;
}

void
_list_remove (link *prev, link *next)
{
  prev->next = next;
  next->prev = prev;
}

void
list_add(link *head, link *arg)
{
  _list_add(head, head->next, arg);
}

void
list_remove(link *arg)
{
  _list_remove(arg->prev, arg->next);
}

void
list_add_tail(link *head, link *arg)
{
  _list_add(head->prev, head, arg);
}

void
node_remove(node *n)
{
  list_remove(&n->l);
}

void
print_node(link *l)
{
  size_t offs = offsetof(struct _node_, l);
  node *n = (node *)(l - offs);
  printf("value: %d\n", n->val);
}

node *
new_node(int val)
{
  node *n = (node *)malloc(sizeof(node));
  n->val = val;
  _list_init(&(n->l));
  return n;
}

void
node_traverse(node *head)
{
  link *temp = head->l.next;
  while (temp != &head->l) {
    print_node(temp);
    temp = temp->next;
  }
}

int
main(int argc, char **argv)
{
  node head;
  _list_init( &(head.l));
  node *a = new_node(3);
  list_add(&(head.l), &(a->l));
  node *b = new_node(5);
  list_add(&(head.l), &(b->l));
  node *c = new_node(6);
  list_add_tail(&(head.l), &(c->l));

  node_traverse(&head);
  return 0;
}

