// AVL树的节点声明
struct AvlNode
{
    Comparable element;
    AvlNode *left;
    AvlNode *right;
    int height;

    AvlNode ( const Comparable & theElement, AvlNode * lt, AvlNode * rt, int h = 0)
        : element(theElement), left(lt), right(rt), height(h) { }
};

// AVL节点高度计算
int height (AvlNode *t) const
{
    return t == NULL ? -1 : t->height;
}

// AVL的插入操作
void insert( const Comparable & x, AvlNode * & t )
{
    if ( t == NULL )
        t = new AvlNode( x, NULL, NULL );
    else if ( x < t->element )
    {
        insert ( x, t->left );
        if ( height( t->left ) - height( t->right ) == 2 )
            if ( x < t->left->element )
                rotateWithLeftChild(t);
            else
                doubleWithLeftChild(t);
    }
    else if ( t->element < x )
    {
        insert( x, t->right );
        if ( height( t-> right ) - height( t->left ) == 2)
            if ( t->right->element < x )
                rotateWithRightChild(t);
            else
                doubleWithRightChild(t);
    }

    t->height = max( height(t->left),height(t->right)) + 1;
}

// 单旋转
void rotateWithLeftChild( AvlNode * & k2)
{
    AvlNode *k1 = k2->left;
    k2->left = k1->right;
    k2->height = max( height( k2->left ), height( k2->right )) + 1;
    k1->height = max( height( k1->left ), k2->height ) + 1;
    k2 = k1;
}
