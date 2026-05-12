#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 100

/* ---------------- RECURSIVE METHOD ---------------- */

int max(int a, int b)
{
    return (a > b) ? a : b;
}

int knapsackRecursive(int W, int wt[], int val[], int n)
{
    if(n == 0 || W == 0)
        return 0;

    if(wt[n - 1] > W)
    {
        return knapsackRecursive(W, wt, val, n - 1);
    }
    else
    {
        return max(
            val[n - 1] +
            knapsackRecursive(W - wt[n - 1],
                              wt,
                              val,
                              n - 1),

            knapsackRecursive(W,
                              wt,
                              val,
                              n - 1)
        );
    }
}

/* ---------------- DYNAMIC PROGRAMMING ---------------- */

int knapsackDP(int W, int wt[], int val[], int n)
{
    int K[MAX][MAX];

    for(int i = 0; i <= n; i++)
    {
        for(int w = 0; w <= W; w++)
        {
            if(i == 0 || w == 0)
            {
                K[i][w] = 0;
            }
            else if(wt[i - 1] <= w)
            {
                K[i][w] = max(
                    val[i - 1] +
                    K[i - 1][w - wt[i - 1]],

                    K[i - 1][w]
                );
            }
            else
            {
                K[i][w] = K[i - 1][w];
            }
        }
    }

    return K[n][W];
}

/* ---------------- MAIN ---------------- */

int main()
{
    int sizes[] = {5, 10, 15, 20, 25};

    printf("\nCOMPARISON OF 0/1 KNAPSACK METHODS\n");

    printf("---------------------------------------------------------------------------------\n");
    printf("| Input Size | Recursive Time | Dynamic Programming Time |\n");
    printf("---------------------------------------------------------------------------------\n");

    for(int s = 0; s < 5; s++)
    {
        int n = sizes[s];

        int wt[MAX], val[MAX];

        for(int i = 0; i < n; i++)
        {
            wt[i] = rand() % 20 + 1;
            val[i] = rand() % 100 + 1;
        }

        int W = 50;

        clock_t start, end;

        double recursive_time, dp_time;

        /* ---------- Recursive Method ---------- */

        start = clock();

        knapsackRecursive(W, wt, val, n);

        end = clock();

        recursive_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        /* ---------- Dynamic Programming ---------- */

        start = clock();

        knapsackDP(W, wt, val, n);

        end = clock();

        dp_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("| %-10d | %-14f | %-24f |\n",
               n,
               recursive_time,
               dp_time);
    }

    printf("---------------------------------------------------------------------------------\n");

    return 0;
}