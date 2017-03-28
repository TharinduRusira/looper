#define TSTEPS 1000
#define N 1000

float A[N][N];

int t, i1,j;

void main(){

    for (t = 0; t <=  TSTEPS - 1; t++)
        for (i1 = 1; i1<= N - 2; i1++)
            for (j = 1; j <= N - 2; j++)
	            A[i1][j] = (A[i1-1][j-1] + A[i1-1][j] + A[i1-1][j+1]
		                    + A[i1][j-1] + A[i1][j] + A[i1][j+1]
		                    + A[i1+1][j-1] + A[i1+1][j] + A[i1+1][j+1])/9.0;


}
