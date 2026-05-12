#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 4

/* ---------------- BACKTRACKING ---------------- */

int board1[N][N];

int isSafeBacktracking(int row, int col)
{
    int i, j;

    for(i = 0; i < col; i++)
    {
        if(board1[row][i])
            return 0;
    }

    for(i = row, j = col; i >= 0 && j >= 0; i--, j--)
    {
        if(board1[i][j])
            return 0;
    }

    for(i = row, j = col; j >= 0 && i < N; i++, j--)
    {
        if(board1[i][j])
            return 0;
    }

    return 1;
}

int solveBacktracking(int col)
{
    if(col >= N)
        return 1;

    for(int i = 0; i < N; i++)
    {
        if(isSafeBacktracking(i, col))
        {
            board1[i][col] = 1;

            if(solveBacktracking(col + 1))
                return 1;

            board1[i][col] = 0;
        }
    }

    return 0;
}

/* ---------------- BRANCH AND BOUND ---------------- */

int board2[N][N];

int rowLookup[N];
int slashCodeLookup[2 * N];
int backslashCodeLookup[2 * N];

int isSafeBranchBound(int row,
                      int col,
                      int slashCode[N][N],
                      int backslashCode[N][N])
{
    if(rowLookup[row] ||
       slashCodeLookup[slashCode[row][col]] ||
       backslashCodeLookup[backslashCode[row][col]])
    {
        return 0;
    }

    return 1;
}

int solveBranchBound(int col,
                     int slashCode[N][N],
                     int backslashCode[N][N])
{
    if(col >= N)
        return 1;

    for(int i = 0; i < N; i++)
    {
        if(isSafeBranchBound(i,
                             col,
                             slashCode,
                             backslashCode))
        {
            board2[i][col] = 1;

            rowLookup[i] = 1;

            slashCodeLookup[slashCode[i][col]] = 1;

            backslashCodeLookup[
                backslashCode[i][col]
            ] = 1;

            if(solveBranchBound(col + 1,
                                slashCode,
                                backslashCode))
            {
                return 1;
            }

            board2[i][col] = 0;

            rowLookup[i] = 0;

            slashCodeLookup[
                slashCode[i][col]
            ] = 0;

            backslashCodeLookup[
                backslashCode[i][col]
            ] = 0;
        }
    }

    return 0;
}

/* ---------------- MAIN ---------------- */

int main()
{
    int iterations[] = {100, 500, 1000, 5000, 10000};

    printf("\nCOMPARISON OF 4-QUEEN METHODS\n");

    printf("-------------------------------------------------------------------------------\n");
    printf("| Iterations | Backtracking Time | Branch & Bound Time |\n");
    printf("-------------------------------------------------------------------------------\n");

    int slashCode[N][N];
    int backslashCode[N][N];

    for(int r = 0; r < N; r++)
    {
        for(int c = 0; c < N; c++)
        {
            slashCode[r][c] = r + c;
            backslashCode[r][c] = r - c + (N - 1);
        }
    }

    for(int s = 0; s < 5; s++)
    {
        int repeat = iterations[s];

        clock_t start, end;

        double backtracking_time, branch_time;

        /* ---------- Backtracking ---------- */

        start = clock();

        for(int i = 0; i < repeat; i++)
        {
            solveBacktracking(0);
        }

        end = clock();

        backtracking_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        /* ---------- Branch & Bound ---------- */

        start = clock();

        for(int i = 0; i < repeat; i++)
        {
            solveBranchBound(0,
                             slashCode,
                             backslashCode);
        }

        end = clock();

        branch_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("| %-10d | %-18f | %-20f |\n",
               repeat,
               backtracking_time,
               branch_time);
    }

    printf("-------------------------------------------------------------------------------\n");

    return 0;
}