#define N 1000
void main()
{
#pragma scop
int i,j,k;
int A[N][N], B[N][N], C[N][N];

for (i=0;i<N;i++)
{
    for(j=0;j<N;j++)
    {
        C[i][j] = 0;
        for(k=0; k<N; k++)
        {
            C[i][j] = C[i][j]+ A[i][k]*B[j][k];
        }

    }
}

#pragma endscop
}
