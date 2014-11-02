
/**
 * Simple inserttion sort
 */
template <typename Comparable>
void insertionSort(vector<Comparable> &a)
{
    int j;
    for (int p = 1; p < a.size(); p++)
    {
        Comparable tmp = a[p];
        for (j = p; j > 0 && tmp < a[j - 1]; j--)
        {
            a[j] = a[j-1];
        }
        a[j] = tmp;
    }
}
// insertion sort, STL version
template <typename Iterator>
void insertionSort(const Iterator &begin, const Iterator &end)
{
    if (begin != end)
        insertionSortHelp(begin, end, *begin);
}
template <typename Iterator, typename Object>
void insertionSortHelp(const Iterator &begin, const Iterator &end, const Object &obj)
{
    insertionSort(begin, end, less<Object>());
}
template <typename Iterator, typename Comparable>
void insertionSort(const Iterator &begin, const Iterator &end, Comparable lessThan)
{
    if (begin != end)
        insertionSort(begin, end, lessThan, *begin);
}
template <typename Iterator, typename Comparable, typename Object>
void insertionSort(const Iterator &begin, const Iterator &end, Comparable lessThan, const Object &obj)
{
    Iterator j;
    for (Iterator p = begin+1; p != end; ++p)
    {
        Object tmp = *p;
        for (j = p; j != begin && lessThan(tmp, *(j-1) ); --j )
            *j = *(j-1);
        *j = tmp;
    }
}

/**
 * Shellsort, using Shell's(poor) increments.
 */
template <typename Comparable>
void shellsort(vector<Comparable> &a)
{
    for (int gap = a.size()/2; gap > 0; gap /= 2)
    {
        for (int i = gap; i < a.size(); i++)
        {
            Comparable tmp = a[i];
            int j = i;

            for (; j >= gap && tmp < a[j - gap]; j -= gap)
                a[j] = a[j - gap];
            a[j] = tmp;
        }
    }
}

/**
 * Standard heapsort.
 */
template <typename Comparable>
void heapsort(vector<Comparable> &a)
{
    for (int i = a.size() / 2; i >= 0; i--)  // build Heap
        perDown(a,i,z.size());
    for (int j = a.size() - 1; j > 0; j--)
    {
        swap(a[0],a[j]);        // delete Max
        perDown(a, 0, j);
    }
}
/**
 * Inernal method for heapsort.
 * i is the index of an item in the heap.
 * Returns the index of the left child.
 */
inline int leftChild(int i)
{
    return 2 * i + 1;
}
/**
 * Internal method for heapsort that is used in deleteMax and buildHeap.
 * i is position from which to percolate down.
 * n is the logical size of the binary heap.
 */
template <typename Comparable>
void perDown(vector<Comparable> &a, int i, int n)
{
    int child;
    Comparable tmp;

    for (tmp = a[i]; leftChild(i) < n; i = child)
    {
        child = leftChild(i);
        if (child != n-1 && a[child] < a[child + 1])
            child++;
        if (tmp < a[child])
            a[i] = a[child];
        else  // tmp是最大值时结束循环
            break;
    }
    a[i] = tmp;
}

/**
 * Mergesort algorithm (driver).
 */
template <typename Comparable>
void mergeSort(vector<Comparable> &a)
{
    vector<Comparable> tmpArray(a.size());
    mergeSort(a, tmpArray, 0, a.size() - 1);
}
/**
 * Internal method that makes recursive calls.
 * a is an array of Comparable items.
 * tmpArray is an array to place the method result.
 * left is the left-most index of the subarray.
 * right is the right-most index of the subarray.
 */
template <typename Comparable>
void mergeSort(vector<Comparable> &a, vector<Comparable> &tmpArray, int left, int right)
{
    if (left < right)
    {
        int center = (left + right) / 2;
        mergeSort(a, tmpArray, left, center);
        mergeSort(a, tmpArray, center+1, right);
        merge(a, tmpArray, left, center+1, right);
    }
}
/**
 * Internal method that merges two sorted halves of a subarray.
 * a is an array of Comparable items.
 * tmpArray is an array to place the merge result.
 * leftPos is the left-most index of the subArray.
 * rightPos is the index of the start of the second half.
 * rightEnd is the right-most index of the subArray.
 */
template <typename Comparable>
void merge(vector<Comparable> &a, vector<Comparable> &tmpArray, int leftPos,
        int rightPos, int rightEnd)
{
    int leftEnd = rightPos - 1;
    int tmpPos = leftPos;
    int numElements = rightEnd - leftPos + 1;

    // Mian loop
    while (leftPos <= leftEnd && rightPos <= rightEnd)
    {
        if (a[leftPos] <= a[rightPos])
            tmpArray[tmpPos++] = a[leftPos++];
        else
            tmpArray[tmpPos++] = a[rightPos++];
    }
    while (leftPos <= leftEnd)   // Copy rest of first half
        tmpArray[tmpPos++] = a[leftPos++];
    while (rightPos <= rightEnd)
        tmpArray[tmpPos++] = a[rightPos++];

    // Copy tmpArray back
    for (int i = 0; i < numElements; i++, rightEnd--)
        a[rightEnd] = tmpArray[rightEnd];
}
