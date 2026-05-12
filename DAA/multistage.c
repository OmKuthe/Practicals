#include <stdio.h>
#include <limits.h>
#include <time.h>

#define N 8
#define INF 99999

void multistageGraph(int graph[N][N])
{
    int cost[N];
    int path[N];

    cost[N - 1] = 0;
    path[N - 1] = -1;

    /* Calculate minimum cost */

    for(int i = N - 2; i >= 0; i--)
    {
        cost[i] = INF;

        for(int j = i + 1; j < N; j++)
        {
            if(graph[i][j] != INF)
            {
                if(graph[i][j] + cost[j] < cost[i])
                {
                    cost[i] =
                        graph[i][j] + cost[j];

                    path[i] = j;
                }
            }
        }
    }

    /* Display Cost Table */

    printf("\nCOST TABLE\n");

    printf("-----------------------------------\n");
    printf("| Vertex | Minimum Cost |\n");
    printf("-----------------------------------\n");

    for(int i = 0; i < N; i++)
    {
        printf("| %-6d | %-12d |\n",
               i,
               cost[i]);
    }

    printf("-----------------------------------\n");

    /* Display Shortest Path */

    printf("\nSHORTEST PATH\n");

    int current = 0;

    while(current != -1)
    {
        printf("%d", current);

        current = path[current];

        if(current != -1)
        {
            printf(" -> ");
        }
    }

    printf("\n");

    /* Display Final Minimum Cost */

    printf("\nMinimum Cost from Source to Destination = %d\n",
           cost[0]);
}

int main()
{
    int graph[N][N] =
    {
        {INF, 1, 2, 5, INF, INF, INF, INF},
        {INF, INF, INF, INF, 4, 11, INF, INF},
        {INF, INF, INF, INF, 9, 5, 16, INF},
        {INF, INF, INF, INF, INF, INF, 2, INF},
        {INF, INF, INF, INF, INF, INF, INF, 18},
        {INF, INF, INF, INF, INF, INF, INF, 13},
        {INF, INF, INF, INF, INF, INF, INF, 2},
        {INF, INF, INF, INF, INF, INF, INF, INF}
    };

    clock_t start, end;

    double time_taken;

    start = clock();

    multistageGraph(graph);

    end = clock();

    time_taken =
        ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("\nExecution Time = %f seconds\n",
           time_taken);

    return 0;
}