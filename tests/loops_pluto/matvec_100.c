#define N 100
int main()
{

int i,j;
static int A[N][N], B[N], C[N];

for (i=0;i<N;i++)
{
    C[i] = 0;
    for(j=0;j<N;j++)
    {
        C[i] = C[i]+ A[i][j]*B[j];
    }
}

return 0;

}
