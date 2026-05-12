#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generateArray(int arr[], int n)
{
    for(int i = 0; i < n; i++)
    {
        arr[i] = rand() % 100000;
    }
}

void copyArray(int source[], int destination[], int n)
{
    for(int i = 0; i < n; i++)
    {
        destination[i] = source[i];
    }
}

void selectionSort(int arr[], int n)
{
    int i, j, min, temp;

    for(i = 0; i < n - 1; i++)
    {
        min = i;

        for(j = i + 1; j < n; j++)
        {
            if(arr[j] < arr[min])
            {
                min = j;
            }
        }

        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}

void bubbleSort(int arr[], int n)
{
    int i, j, temp;

    for(i = 0; i < n - 1; i++)
    {
        for(j = 0; j < n - i - 1; j++)
        {
            if(arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void insertionSort(int arr[], int n)
{
    int i, key, j;

    for(i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;

        while(j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}

int main()
{
    int sizes[] = {1000, 3000, 5000, 7000, 10000};

    printf("\nCOMPARISON OF SORTING ALGORITHMS\n");

    printf("---------------------------------------------------------------------------------------------------\n");
    printf("| Input Size | Selection Sort | Bubble Sort | Insertion Sort |\n");
    printf("---------------------------------------------------------------------------------------------------\n");

    for(int s = 0; s < 5; s++)
    {
        int n = sizes[s];

        int *original = (int *)malloc(n * sizeof(int));
        int *arr1 = (int *)malloc(n * sizeof(int));
        int *arr2 = (int *)malloc(n * sizeof(int));
        int *arr3 = (int *)malloc(n * sizeof(int));

        generateArray(original, n);

        copyArray(original, arr1, n);
        copyArray(original, arr2, n);
        copyArray(original, arr3, n);

        clock_t start, end;

        double selection_time, bubble_time, insertion_time;

        // Selection Sort
        start = clock();

        selectionSort(arr1, n);

        end = clock();

        selection_time = ((double)(end - start)) / CLOCKS_PER_SEC;

        // Bubble Sort
        start = clock();

        bubbleSort(arr2, n);

        end = clock();

        bubble_time = ((double)(end - start)) / CLOCKS_PER_SEC;

        // Insertion Sort
        start = clock();

        insertionSort(arr3, n);

        end = clock();

        insertion_time = ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("| %-10d | %-14f | %-11f | %-14f |\n",
               n,
               selection_time,
               bubble_time,
               insertion_time);

        free(original);
        free(arr1);
        free(arr2);
        free(arr3);
    }

    printf("---------------------------------------------------------------------------------------------------\n");

    return 0;
}