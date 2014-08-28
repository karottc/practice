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

/* 二叉搜索树：删除 */
/* 假定根节点不会被删除
 * 参数：root-根节点，value-要删除的目标值
 */
void BST_Delete(bst_tree* root, var value)
{
    bst_tree *node = root;
    bst_tree *parent;
    while (node != NULL && node->key != value)
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
    if (node == NULL)
    {
        printf("value is not in the tree\n");
        return;
    }
    if (node != root)
    {
        /********************************
         * 目标节点左子节点为空
         *       O       O
         *      /         \
         *     X           X
         *    / \         / \
         *  NULL O      NULL O
         *      / \         / \
         *     O   O       O   O
         * */
        if (node->left == NULL)
        {
            if (value < parent->key)
            {
                parent->left = node->right;
            }
            else
            {
                parent->right = node->right;
            }
        }
        /******************************** 
         * 目标节点右子节点为空
         *       O       O      
         *      /         \
         *     X           X
         *    / \         / \
         *   O   NULL    O  NULL
         *  / \         / \
         * O   O       O   O
         * 
         ********************************/
        else if (node->right == NULL)
        {
            if (value < parent->key)
            {
                parent->left = node->left;
            }
            else
            {
                parent->right = node->left;
            }
        }
        else
        {
            /*********************************
             * 目标节点的子节点都不为空
             *                 O
             *                 |
             *                 X
             *                / \
             *               O   O
             *              / \
             *             O   O
             *                  \
             *                   T
             *                  / \
             *                 O   NULL
             * 用T的值替换目标X的值 
             ********************************/
            bst_tree *node1 = node->left;
            bst_tree *parent1 = node;
            while (node1->right != NULL)
            {
                parent1 = node1;
                node1 = node1->right;
            }
            parent1->right = node1->left;
            node->key = node1->key;
        }
    }
}
