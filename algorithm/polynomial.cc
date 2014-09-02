
/* 多项式求值
 *
 * P_n(x) = a_n * x^n + a_(n-1) * x^(n-1) + ... + a_2 * x^2 + a_1 * x + a_0
 * 思路：
 * P_(n-1)(x) = a_n * x^(n-1) + a_(n-1) * x^(n-2) + ... + a_2 * x + a_1
 * P_(n-2)(x) = a_n * x^(n-2) + a_(n-1) * x^(n-3) + ... + a_3 * x + a-2
 * ...
 * P_2(x) = a_n * x^2 + a_(n-1) * x + a_(n-2)
 * P_1(x) = a_n * x + a_(n-1)
 * P_0(x) = a_n
 */
int Polynomial_Evaluation(int *a, int n, var value)
{
    int i = 0;
    int result = a[n];
    for (i = 0; i < n; i++)
    {
        result = result * value + a[n-1-i]
    }
    return result;
}
