/* 社会名流问题
 *
 * 参数：know - 保存任务之间的认识相互关系，n x n 的数组;
 * 输出：社会名流
 *
 * 前提：假定最多只有一个社会名流，并且社会名流不认识其他人，其他人都认识
 * 社会名流。
 */

int Celebrity(int **know, int n)
{
    int celebrity = -1;
    int i = 0, j = 1, next = 3;
    int candidate = 0;
    while (next <= n)
    {
        // 如果i知道j，则i肯定不是社会名流
        if (know[i][j])
        {
            i = next;
        }
        else
        {
            j = next;
        }
        next++;
    }

    if (i == n)
    {
        candidate = j;
    }
    else
    {
        candidate = i;
    }

    int wrong = 0;
    int k = 0;
    know[candidate][candidate] = 0;
    while (!wrong && k <= n-1)
    {
        if (know[candidate][k])
        {
            wrong = true;
        }
        if (!know[k][candidate] && candidate != k)
        {
            wrong = true;
        }
        k++;
    }

    if (!wrong)
    {
        celebrity = candidate;
    }
    else
    {
        celebrity = -1;
    }

    return celebrity;
}
