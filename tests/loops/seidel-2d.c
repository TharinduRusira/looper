#define TSTEPS 1000
#define N 1000

float A[N][N];

int t, i1,j1;

void main(){

    for (t = 0; t <=  TSTEPS - 1; t++)
        for (i1 = 1; i1<= N - 2; i1++)
            for (j1 = 1; j1 <= N - 2; j1++)
	            A[i1][j1] = (A[i1-1][j1-1] + A[i1-1][j1] + A[i1-1][j1+1]
		                    + A[i1][j1-1] + A[i1][j1] + A[i1][j1+1]
		                    + A[i1+1][j1-1] + A[i1+1][j1] + A[i1+1][j1+1])/9.0;


}