#define N 1000
#define TSTEPS 1000

float A[N][N];
float B[N][N];

int t, i1, j1, i2, j2;

void main(){

    for (t = 0; t < TSTEPS; t++)
    {
        for (i1 = 1; i1 < N - 1; i1++){
	        for (j1 = 1; j1 < N - 1; j1++){
	            B[i1][j1] = (0.2) * (A[i1][j1] + A[i1][j1-1] + A[i1][1+j1] + A[1+i1][j1] + A[i1-1][j1]);
	         }
	    }
        for (i2 = 1; i2 < N - 1; i2++){
	        for (j2 = 1; j2 < N - 1; j2++){
	            A[i2][j2] = (0.2) * (B[i2][j2] + B[i2][j2-1] + B[i2][1+j2] + B[1+i2][j2] + B[i2-1][j2]);
	        }
	    }
    }

}