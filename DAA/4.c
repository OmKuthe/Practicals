#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 100

/* ---------------- KRUSKAL ALGORITHM ---------------- */

struct Edge
{
    int src, dest, weight;
};

int parent[MAX];

int find(int i)
{
    while(parent[i] != i)
        i = parent[i];

    return i;
}

void unionSet(int a, int b)
{
    parent[a] = b;
}

void sortEdges(struct Edge edges[], int e)
{
    for(int i = 0; i < e - 1; i++)
    {
        for(int j = 0; j < e - i - 1; j++)
        {
            if(edges[j].weight > edges[j + 1].weight)
            {
                struct Edge temp = edges[j];
                edges[j] = edges[j + 1];
                edges[j + 1] = temp;
            }
        }
    }
}

void kruskal(struct Edge edges[], int v, int e)
{
    sortEdges(edges, e);

    for(int i = 0; i < v; i++)
        parent[i] = i;

    int count = 0;
    int i = 0;

    while(count < v - 1 && i < e)
    {
        int srcParent = find(edges[i].src);
        int destParent = find(edges[i].dest);

        if(srcParent != destParent)
        {
            unionSet(srcParent, destParent);
            count++;
        }

        i++;
    }
}

/* ---------------- HUFFMAN CODING ---------------- */

struct Node
{
    char data;
    unsigned freq;
    struct Node *left, *right;
};

struct Node* createNode(char data, unsigned freq)
{
    struct Node* temp =
        (struct Node*)malloc(sizeof(struct Node));

    temp->left = temp->right = NULL;
    temp->data = data;
    temp->freq = freq;

    return temp;
}

void huffmanCoding(char data[], int freq[], int size)
{
    struct Node* nodes[MAX];

    for(int i = 0; i < size; i++)
    {
        nodes[i] = createNode(data[i], freq[i]);
    }

    while(size > 1)
    {
        int min1 = 0, min2 = 1;

        if(nodes[min1]->freq > nodes[min2]->freq)
        {
            int t = min1;
            min1 = min2;
            min2 = t;
        }

        for(int i = 2; i < size; i++)
        {
            if(nodes[i]->freq < nodes[min1]->freq)
            {
                min2 = min1;
                min1 = i;
            }
            else if(nodes[i]->freq < nodes[min2]->freq)
            {
                min2 = i;
            }
        }

        struct Node* left = nodes[min1];
        struct Node* right = nodes[min2];

        struct Node* newNode =
            createNode('$',
                       left->freq + right->freq);

        newNode->left = left;
        newNode->right = right;

        nodes[min1] = newNode;
        nodes[min2] = nodes[size - 1];

        size--;
    }
}

/* ---------------- MAIN ---------------- */

int main()
{
    int sizes[] = {10, 20, 30, 40, 50};

    printf("\nCOMPARISON OF GREEDY ALGORITHMS\n");

    printf("-------------------------------------------------------------------------------\n");
    printf("| Input Size | Kruskal Time | Huffman Coding Time |\n");
    printf("-------------------------------------------------------------------------------\n");

    for(int s = 0; s < 5; s++)
    {
        int n = sizes[s];

        /* ---------- Kruskal Input ---------- */

        int vertices = n;
        int edgesCount = n + 5;

        struct Edge edges[MAX];

        for(int i = 0; i < edgesCount; i++)
        {
            edges[i].src = rand() % vertices;
            edges[i].dest = rand() % vertices;
            edges[i].weight = rand() % 100;
        }

        /* ---------- Huffman Input ---------- */

        char data[MAX];
        int freq[MAX];

        for(int i = 0; i < n; i++)
        {
            data[i] = 'A' + (i % 26);
            freq[i] = rand() % 100 + 1;
        }

        clock_t start, end;

        double kruskal_time, huffman_time;

        /* ---------- Kruskal Timing ---------- */

        start = clock();

        kruskal(edges, vertices, edgesCount);

        end = clock();

        kruskal_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        /* ---------- Huffman Timing ---------- */

        start = clock();

        huffmanCoding(data, freq, n);

        end = clock();

        huffman_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("| %-10d | %-13f | %-21f |\n",
               n,
               kruskal_time,
               huffman_time);
    }

    printf("-------------------------------------------------------------------------------\n");

    return 0;
}