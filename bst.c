/*
 * =====================================================================================
 *
 *       Filename:  bst.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/23/2017 08:46:31 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct _node_ {
  int val;
  struct _node_ *left;
  struct _node_ *right;
} node;


node *
node_create(int val)
{
  node *n = (node *)malloc(sizeof(node));
  n->val = val;
  n->left = NULL;
  n->right = NULL;

  return n;
}


void
node_insert(node *root, int val)
{
  node *n = node_create(val);
  if (root == NULL)
    return;

  node **temp = &root;
  while (*temp != NULL)
    temp = ((*temp)->val >= val)? &((*temp)->left) : &((*temp)->right);
  *temp = n;
}

node *
node_find(node *root, int val)
{
  if (root == NULL)
    return NULL;

  node *temp = root;
  while (temp != NULL) {
    if (temp->val == val)
      break;
    temp = (temp->val >= val)? temp->left : temp->right;
  }

  return temp;
}

node *
node_delete(node *root, node *arg)
{
  return NULL;
}

void
in_order(node *root)
{
  if (root == NULL)
    return;
  
  if (root->left)
    in_order(root->left);

  printf("%d\n", root->val);
  
  if (root->right)
    in_order(root->right);

}

int
main(int argc, char **argv)
{
  node *root = node_create(10);
  node_insert(root, 5);
  node_insert(root, 15);
  node_insert(root, 13);
  node_insert(root, 3);
  node_insert(root, 7);
  
  in_order(root);
}
