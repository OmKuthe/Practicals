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

/* ---------------- MERGE SORT ---------------- */

void merge(int arr[], int left, int mid, int right)
{
    int i, j, k;

    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];

    for(i = 0; i < n1; i++)
        L[i] = arr[left + i];

    for(j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    i = 0;
    j = 0;
    k = left;

    while(i < n1 && j < n2)
    {
        if(L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while(i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    while(j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int left, int right)
{
    if(left < right)
    {
        int mid = (left + right) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}

/* ---------------- QUICK SORT ---------------- */

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];

    int i = low - 1;

    for(int j = low; j < high; j++)
    {
        if(arr[j] < pivot)
        {
            i++;

            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}

void quickSort(int arr[], int low, int high)
{
    if(low < high)
    {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

/* ---------------- MAIN ---------------- */

int main()
{
    int sizes[] = {1000, 5000, 10000, 20000, 50000};

    printf("\nCOMPARISON OF MERGE SORT AND QUICK SORT\n");

    printf("-------------------------------------------------------------------------------\n");
    printf("| Input Size | Merge Sort Time | Quick Sort Time |\n");
    printf("-------------------------------------------------------------------------------\n");

    for(int s = 0; s < 5; s++)
    {
        int n = sizes[s];

        int *original = (int *)malloc(n * sizeof(int));
        int *arr1 = (int *)malloc(n * sizeof(int));
        int *arr2 = (int *)malloc(n * sizeof(int));

        generateArray(original, n);

        copyArray(original, arr1, n);
        copyArray(original, arr2, n);

        clock_t start, end;

        double merge_time, quick_time;

        /* Merge Sort Timing */

        start = clock();

        mergeSort(arr1, 0, n - 1);

        end = clock();

        merge_time = ((double)(end - start)) / CLOCKS_PER_SEC;

        /* Quick Sort Timing */

        start = clock();

        quickSort(arr2, 0, n - 1);

        end = clock();

        quick_time = ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("| %-10d | %-16f | %-16f |\n",
               n,
               merge_time,
               quick_time);

        free(original);
        free(arr1);
        free(arr2);
    }

    printf("-------------------------------------------------------------------------------\n");

    return 0;
}