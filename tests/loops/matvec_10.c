#include <stdlib.h>
#define N 10
int main()
{

int i,j;
int **A = (int**)malloc(N*sizeof(int*)); 
int *B = (int*)malloc(N*sizeof(int));
int *C = (int*)malloc(N*sizeof(int));

for (i=0;i<N;i++)
{
    C[i] = 0;
    for(j=0;j<N;j++)
    {
        C[i] = C[i]+ A[i][j]*B[j];
    }
}
free(A); free(B); free(C);
return 0;

}
