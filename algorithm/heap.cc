#include <stdio.h>

/* 堆的remove操作 */
/* 优先队列时使用堆 
 * 参数：A是一个数组，n是现有元素个数.
 * 返回值：返回删除的最大值，以及之后的数组A和数组长度n.
 */
int Remove_Max_from_Heap(int *A, int &n)
{
    if (n == 0)
    {
        fprintf(stderr,"The heap is empty!!\n");
        return -1;
    }
    int result = A[0];
    n -= 1;
    int parent = 0;
    int clild = 1;
    /* 堆的父节点和两个子节点的关系：父节点是i, 两个子节点分别是 2i+1, 2i+2 */
    while (child < n-1)
    {
        if (A[child] < A[child+1])
            child += 1;
        if (A[child] > A[parent])
        {
            swap(A, child, parent);
            parent = child;
            child = 2 * child + 1;
        }
        else
        {
            child = n;   // 已经是最大值堆，结束循环
        }
    }
    return result;
}

/* 堆的Insert操作 */
/*
 * 参数：A是一个数组，n是现有元素个数.
 * 返回值: 插入之后的数组A和数组长度n.
 */
int Insert_to_Heap(int *A, int &n, int value)
{
    n += 1; // 假定数组没有越界
    A[n - 1] = value;
    int child = n - 1;
    int parent = (child - 1)/2;
    while (parent >= 0)
    {
        if (A[parent] < A[child])
        {
            swap(A, parent, child);
            child = parent;
            parent = (child - 1)/2;
        }
        else
        {
            parent = -1;    // 满足堆的性质，退出循环
        }
    }
    return 0;
}

/* 交换数组A中的两个元素的值 */
void swap(int *A, int a, int b)
{
    int temp = A[a];
    A[a] = A[b];
    A[b] = temp;
}
