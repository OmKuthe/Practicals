#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define MAX 100

/* ---------------- RECURSIVE METHOD ---------------- */

int sum(int freq[], int i, int j)
{
    int s = 0;

    for(int k = i; k <= j; k++)
    {
        s += freq[k];
    }

    return s;
}

int obstRecursive(int freq[], int i, int j)
{
    if(i > j)
        return 0;

    if(i == j)
        return freq[i];

    int minCost = INT_MAX;

    for(int r = i; r <= j; r++)
    {
        int cost =
            obstRecursive(freq, i, r - 1) +
            obstRecursive(freq, r + 1, j);

        if(cost < minCost)
        {
            minCost = cost;
        }
    }

    return minCost + sum(freq, i, j);
}

/* ---------------- DYNAMIC PROGRAMMING ---------------- */

int obstDP(int freq[], int n)
{
    int cost[MAX][MAX];

    for(int i = 0; i < n; i++)
    {
        cost[i][i] = freq[i];
    }

    for(int L = 2; L <= n; L++)
    {
        for(int i = 0; i <= n - L; i++)
        {
            int j = i + L - 1;

            cost[i][j] = INT_MAX;

            int fsum = sum(freq, i, j);

            for(int r = i; r <= j; r++)
            {
                int c = fsum;

                if(r > i)
                    c += cost[i][r - 1];

                if(r < j)
                    c += cost[r + 1][j];

                if(c < cost[i][j])
                {
                    cost[i][j] = c;
                }
            }
        }
    }

    return cost[0][n - 1];
}

/* ---------------- MAIN ---------------- */

int main()
{
    int sizes[] = {5, 10, 15, 20, 25};

    printf("\nCOMPARISON OF OBST METHODS\n");

    printf("---------------------------------------------------------------------------------\n");
    printf("| Keys | Recursive Time | Dynamic Programming Time |\n");
    printf("---------------------------------------------------------------------------------\n");

    for(int s = 0; s < 5; s++)
    {
        int n = sizes[s];

        int freq[MAX];

        for(int i = 0; i < n; i++)
        {
            freq[i] = rand() % 50 + 1;
        }

        clock_t start, end;

        double recursive_time, dp_time;

        /* ---------- Recursive ---------- */

        start = clock();

        obstRecursive(freq, 0, n - 1);

        end = clock();

        recursive_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        /* ---------- DP ---------- */

        start = clock();

        obstDP(freq, n);

        end = clock();

        dp_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("| %-4d | %-14f | %-24f |\n",
               n,
               recursive_time,
               dp_time);
    }

    printf("---------------------------------------------------------------------------------\n");

    return 0;
}