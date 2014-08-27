#include <stdio.h>

/* 二叉搜索树：查找 */
bst_tree* BST_Search(bst_tree* root, var value)
{
    if (root == NULL)
    {
        return NULL;
    }
    else if (root->key = value)
    {
        return root;
    }
    else
    {
        if (value < root->key)
        {
            BST_Search(root->left, value);
        }
        else
        {
            BST_Search(root->right, value);
        }
    }
}

/* 二叉搜索树：插入 */
void BST_Insert(bst_tree* root, var value)
{
    bst_tree *child, *parent, *node;
    if (root == NULL)
    {
        child = new bst_tree();
        root = child;
        root->key = value;
        root->left = NULL;
        root->right = NULL;
    }
    else
    {
        node = child = root;
        while (node != NULL && child != NULL)
        {
            if (node->key == value)
            {
                child = NULL;
            }
            else
            {
                parent = node;
                if (value < node->key)
                {
                    node = node->left;
                }
                else
                {
                    node = node->right;
                }
            }
        }
        if (child != NULL)
        {
            child = new bst_tree();
            child->key = value;
            child->left = NULL;
            child->right = NULL;
            if (value < parent->key)
            {
                parent->left = child;
            }
            else
            {
                parent->right = child;
            }
        }
    }
}
