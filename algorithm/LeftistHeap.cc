// 左式堆
template <typename Comparable>
class LeftistHeap
{
    public:
        LeftistHeap();
        LeftistHeap(const LeftistHeap &rhs);
        ~LeftistHeap();

        bool isEmpty() const;
        const Comparable &findMin() const;

        void insert(const Comparable &x);
        void deleteMin();
        void deleteMin(Comparable & minItem);
        void makeEmpty();
        void merge(LeftistHeap &rhs);

        const LeftistHeap &operator=(const LeftistHeap &rhs);

    private:
        struct LeftistNode
        {
            Comparable element;
            LeftistNode *left;
            LeftistNode *right;
            int          npl;

            LeftistNode(const Comparable &theElement, LeftistNode *lt = NULL,
                    LeftistNode *rt = NULL, int np = 0)
                : element(theElement),left(lt),right(rt),npl(np) { }
        };

        LeftistNode *root;

        LeftistNode *merge(LeftistNode *h1, LeftistNode *h2);
        LeftistNode *merge1(LeftistNode *h1, LeftistNode *h2);

        void swapChildren(LeftistNode *t);
        void reclaimMemory(LeftistNode *t);
        LeftistNode *clone(LeftistNode *t) const;
};

/**
 * Merge rhs into the priority queue.
 * rhs becomes empty. rhs must be different from this.
 */
void LeftistHeap::merge(LeftistHeap &rhs)
{
    if ( this == &rhs)              // Avoid aliasing problems
        return;

    root = merge(root, rhs.root);
    rhs.root = NULL;
}

/**
 * Internal method to merge two roots.
 * Deals with deviant cases and calls recursive merge1.
 */
LeftistNode * LeftistHeap::merge(LeftistNode *h1, LeftistNode *h2)
{
    if (h1 == NULL)
        return h2;
    if (h2 == NULL)
        return h1;
    if (h1->element < h2->element)
        return merge1(h1,h2);
    else
        return merge1(h2, h1);
}

/**
 * Internal method to merge two roots.
 * Assumes trees are not empty, and h1's root contains smallest item.
 */
LeftistNode * LeftistHeap::merge1(LeftistNode *h1, LeftistNode *h2)
{
    if (h1->left == NULL)           // single node
        h1->left = h2;       // other fields in h1 already accurate.
    else
    {
        h1->right = merge(h1->right, h2);
        if (h1->left->npl < h1->right->npl)
            swapChildren(h1);
        h1->npl = h1->right->npl + 1;
    }
    return h1;
}

/**
 * Inserts x; duplicates allowed.
 */
void LeftistHeap::insert(const Comparable &x)
{
    root = merge(new LeftistNode(x), root);
}

/** 
 * Remove the minimum item.
 * Throws UnderflowException if empty.
 */
void LeftistHeap::deleteMin()
{
    if ( isEmpty() )
    {
        throw UnderflowException();
    }
    LeftistNode *oldRoot = root;
    root = merge(root-left, root->right);
    delete oldRoot;
}

/**
 * Remove the minimum item and place it in minItem.
 * Throws UnderflowException if empty.
 */
void LeftistHeap::deleteMin(Comparable & minItem)
{
    minItem = findMin();
    deleteMin();
}
