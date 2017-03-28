/*
Out of place 5-pt
stencil computation on a 2-D grid
*/
#define N 10

int main()
{

int i,j;
int A[N][N];
double B[N-2][N-2]; //boundary is not computed
#pragma scop
for (i=1;i<N-1;i++)
{
    for(j=1;j<N-1;j++)
    {
        B[i][j] = 0.6*A[i][j] + 0.1*A[i-1][j] + 0.1*A[i+1][j] + 0.1*A[i][j-1] + 0.1*A[i][j+1];
    }
}
#pragma endscop
return 0;

}
