/* 寻找一对一的映射集 
 *
 * 参数:
 * A - 由1到n组成的集合;
 * S - 目标所求，A的一个子集;
 * f - S上一对一的函数;
 * c - 映射的计数;
 */

List algorithm_mapping(List A, int *f, int n, int *c)
{
    List S = A;
    int i = 0;
    queen q;
    // 第一遍遍历，初始化映射计数
    for (i = 0; i < n; i++)
    {
        c[i] = 0;
    }
    // 第一遍遍历，计算映射计数
    for (i = 0; i < n; i++)
    {
        c[f[i]]++;
    }
    // 第三遍遍历，将没有被映射到的元素取出放到队列
    for (i = 0; i < n; i++)
    {
        if (c[i] == 0)
        {
            q.put(i);
        }
    }
    // 更新目标子集：
    // 1. 从目标子集中删除映射数为0的元素；
    // 2. 将删除元素映射到的目标元素计数值减一；
    // 3. 在第2步基础上重新判断计数值，更新队列；
    // 4. 当处理完所有元素时，队列应该为空。
    while (!q.empty())
    {
        int temp = q.pop();
        S.remove(temp);
        c[f[temp]]--;
        if (c[f[temp]] == 0)
        {
            q.put(f[temp]);
        }
    }
    return S;
}
