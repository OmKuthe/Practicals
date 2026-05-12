#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 10
#define INF 99999

/* ---------------- RECURSIVE TSP ---------------- */

int tspRecursive(int graph[MAX][MAX],
                 int visited[],
                 int curr,
                 int n,
                 int count,
                 int cost,
                 int ans)
{
    if(count == n && graph[curr][0])
    {
        if(cost + graph[curr][0] < ans)
        {
            ans = cost + graph[curr][0];
        }

        return ans;
    }

    for(int i = 0; i < n; i++)
    {
        if(visited[i] == 0 && graph[curr][i])
        {
            visited[i] = 1;

            ans = tspRecursive(graph,
                               visited,
                               i,
                               n,
                               count + 1,
                               cost + graph[curr][i],
                               ans);

            visited[i] = 0;
        }
    }

    return ans;
}

/* ---------------- DP TSP ---------------- */

int dp[1 << MAX][MAX];

int tspDP(int graph[MAX][MAX],
          int mask,
          int pos,
          int n)
{
    if(mask == (1 << n) - 1)
    {
        return graph[pos][0];
    }

    if(dp[mask][pos] != -1)
    {
        return dp[mask][pos];
    }

    int ans = INF;

    for(int city = 0; city < n; city++)
    {
        if((mask & (1 << city)) == 0)
        {
            int newAns =
                graph[pos][city] +
                tspDP(graph,
                      mask | (1 << city),
                      city,
                      n);

            if(newAns < ans)
            {
                ans = newAns;
            }
        }
    }

    return dp[mask][pos] = ans;
}

/* ---------------- GENERATE GRAPH ---------------- */

void generateGraph(int graph[MAX][MAX], int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(i == j)
                graph[i][j] = 0;
            else
                graph[i][j] = rand() % 50 + 1;
        }
    }
}

/* ---------------- MAIN ---------------- */

int main()
{
    int sizes[] = {4, 5, 6, 7, 8};

    int graph[MAX][MAX];

    printf("\nCOMPARISON OF TSP METHODS\n");

    printf("---------------------------------------------------------------------------------\n");
    printf("| Cities | Recursive Time | Dynamic Programming Time |\n");
    printf("---------------------------------------------------------------------------------\n");

    for(int s = 0; s < 5; s++)
    {
        int n = sizes[s];

        generateGraph(graph, n);

        int visited[MAX] = {0};

        visited[0] = 1;

        clock_t start, end;

        double recursive_time, dp_time;

        /* ---------- Recursive TSP ---------- */

        start = clock();

        tspRecursive(graph,
                     visited,
                     0,
                     n,
                     1,
                     0,
                     INF);

        end = clock();

        recursive_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        /* ---------- DP TSP ---------- */

        for(int i = 0; i < (1 << MAX); i++)
        {
            for(int j = 0; j < MAX; j++)
            {
                dp[i][j] = -1;
            }
        }

        start = clock();

        tspDP(graph, 1, 0, n);

        end = clock();

        dp_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("| %-6d | %-14f | %-24f |\n",
               n,
               recursive_time,
               dp_time);
    }

    printf("---------------------------------------------------------------------------------\n");

    return 0;
}