/* 求最大子序列算法
 *
 * 输入：X （大小为n的数组）
 * 输出：global_Max(最大连续子序列之和)
 *
 * TODO: 稍微改进下可以顺便得到所求的序列
 */

int Maximum_Consecutive_Subsequence(int *x, int n)
{
    int global_Max = 0;   // 最大子序列的和
    int suffix_Max = 0;   // 最大后缀子序列的和，每次迭代都会更新
    int i = 0;
    for (i = 0; i < n; i++)
    {
        if (x[i] + suffix_Max > global_Max)
        {
            suffix_Max = suffix_Max + x[i];
            global_Max = suffix_Max;
        }
        else if (x[i] + suffix_Max > 0)
        {
            suffix_Max = suffix_Max + x[i];
        }
        else
        {
            suffix_Max = 0;
        }
    }
    return global_Max;
}
