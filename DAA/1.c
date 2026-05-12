#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generateSortedArray(int arr[], int n)
{
    for(int i = 0; i < n; i++)
    {
        arr[i] = i * 2;
    }
}

int linearSearch(int arr[], int n, int key)
{
    for(int i = 0; i < n; i++)
    {
        if(arr[i] == key)
            return i;
    }
    return -1;
}

int binarySearch(int arr[], int n, int key)
{
    int low = 0, high = n - 1;

    while(low <= high)
    {
        int mid = (low + high) / 2;

        if(arr[mid] == key)
            return mid;

        else if(arr[mid] < key)
            low = mid + 1;

        else
            high = mid - 1;
    }

    return -1;
}

int main()
{
    int sizes[] = {1000, 5000, 10000, 20000, 50000};

    printf("\nCOMPARISON OF LINEAR SEARCH AND BINARY SEARCH\n");
    printf("-------------------------------------------------------------------------------\n");
    printf("| Input Size | Linear Search Time | Binary Search Time |\n");
    printf("-------------------------------------------------------------------------------\n");

    for(int i = 0; i < 5; i++)
    {
        int n = sizes[i];

        int *arr = (int *)malloc(n * sizeof(int));

        generateSortedArray(arr, n);

        int key = -1;

        clock_t start1, end1;
        clock_t start2, end2;

        double linear_time, binary_time;

        // Linear Search Timing
        start1 = clock();

        linearSearch(arr, n, key);

        end1 = clock();

        linear_time = ((double)(end1 - start1)) / CLOCKS_PER_SEC;

        // Binary Search Timing
        start2 = clock();

        binarySearch(arr, n, key);

        end2 = clock();

        binary_time = ((double)(end2 - start2)) / CLOCKS_PER_SEC;

        printf("| %-10d | %-18f | %-18f |\n",
               n, linear_time, binary_time);

        free(arr);
    }

    printf("-------------------------------------------------------------------------------\n");

    return 0;
}