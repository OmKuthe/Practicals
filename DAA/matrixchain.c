#include <stdio.h>
#include <limits.h>
#include <time.h>
#include <stdlib.h>

#define MAX 100

/* ---------------- RECURSIVE METHOD ---------------- */

int min(int a, int b)
{
    return (a < b) ? a : b;
}

int matrixChainRecursive(int p[], int i, int j)
{
    if(i == j)
        return 0;

    int minCost = INT_MAX;

    for(int k = i; k < j; k++)
    {
        int cost =
            matrixChainRecursive(p, i, k) +
            matrixChainRecursive(p, k + 1, j) +
            p[i - 1] * p[k] * p[j];

        if(cost < minCost)
        {
            minCost = cost;
        }
    }

    return minCost;
}

/* ---------------- DYNAMIC PROGRAMMING ---------------- */

int matrixChainDP(int p[], int n)
{
    int m[MAX][MAX];

    for(int i = 1; i < n; i++)
    {
        m[i][i] = 0;
    }

    for(int L = 2; L < n; L++)
    {
        for(int i = 1; i < n - L + 1; i++)
        {
            int j = i + L - 1;

            m[i][j] = INT_MAX;

            for(int k = i; k < j; k++)
            {
                int q =
                    m[i][k] +
                    m[k + 1][j] +
                    p[i - 1] * p[k] * p[j];

                if(q < m[i][j])
                {
                    m[i][j] = q;
                }
            }
        }
    }

    return m[1][n - 1];
}

/* ---------------- MAIN ---------------- */

int main()
{
    int sizes[] = {5, 10, 15, 20, 25};

    printf("\nCOMPARISON OF MATRIX CHAIN MULTIPLICATION METHODS\n");

    printf("---------------------------------------------------------------------------------\n");
    printf("| Matrices | Recursive Time | Dynamic Programming Time |\n");
    printf("---------------------------------------------------------------------------------\n");

    for(int s = 0; s < 5; s++)
    {
        int n = sizes[s];

        int p[MAX];

        /* Generate random dimensions */

        for(int i = 0; i <= n; i++)
        {
            p[i] = rand() % 50 + 1;
        }

        clock_t start, end;

        double recursive_time, dp_time;

        /* ---------- Recursive Method ---------- */

        start = clock();

        matrixChainRecursive(p, 1, n);

        end = clock();

        recursive_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        /* ---------- Dynamic Programming ---------- */

        start = clock();

        matrixChainDP(p, n + 1);

        end = clock();

        dp_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("| %-8d | %-14f | %-24f |\n",
               n,
               recursive_time,
               dp_time);
    }

    printf("---------------------------------------------------------------------------------\n");

    return 0;
}