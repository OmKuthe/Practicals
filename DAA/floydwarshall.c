#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define INF 99999
#define MAX 100

void generateGraph(int graph[MAX][MAX], int V)
{
    for(int i = 0; i < V; i++)
    {
        for(int j = 0; j < V; j++)
        {
            if(i == j)
                graph[i][j] = 0;

            else
                graph[i][j] = rand() % 20 + 1;
        }
    }
}

void floydWarshall(int graph[MAX][MAX], int V)
{
    int dist[MAX][MAX];

    for(int i = 0; i < V; i++)
    {
        for(int j = 0; j < V; j++)
        {
            dist[i][j] = graph[i][j];
        }
    }

    for(int k = 0; k < V; k++)
    {
        for(int i = 0; i < V; i++)
        {
            for(int j = 0; j < V; j++)
            {
                if(dist[i][k] + dist[k][j] < dist[i][j])
                {
                    dist[i][j] =
                        dist[i][k] + dist[k][j];
                }
            }
        }
    }
}

int main()
{
    int sizes[] = {10, 20, 30, 40, 50};

    int graph[MAX][MAX];

    printf("\nFLOYD WARSHALL ANALYSIS\n");

    printf("---------------------------------------------------\n");
    printf("| Number of Vertices | Time Taken |\n");
    printf("---------------------------------------------------\n");

    for(int s = 0; s < 5; s++)
    {
        int V = sizes[s];

        generateGraph(graph, V);

        clock_t start, end;

        start = clock();

        floydWarshall(graph, V);

        end = clock();

        double time_taken =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("| %-18d | %-12f |\n",
               V,
               time_taken);
    }

    printf("---------------------------------------------------\n");

    return 0;
}