#define N 1000
#define M 1000

float A[M][N];
float R[N][N];
float Q[M][N];

float nrm;

int i1, j, k1, i2, i3, i4;

void main(){
#pragma scop
    for (k1 = 0; k1 < N; k1++)
    {
        nrm = 0.0;
        for (i1 = 0; i1 < M; i1++){
            nrm = nrm + A[i1][k1] * A[i1][k1];
        }
        R[k1][k1] = nrm; //SQRT_FUN(nrm);

        for (i2 = 0; i2 < M; i2++){
            Q[i2][k1] = A[i2][k1] / R[k1][k1];
        }
        for (j = k1 + 1; j < N; j++)
	    {
	        R[k1][j] = 0.0;
	        for (i3 = 0; i3 < M; i3++){
	            R[k1][j] = R[k1][j] + Q[i3][k1] * A[i3][j];
	        }
	        for (i4 = 0; i4 < M; i4++){
	            A[i4][j] = A[i4][j] - Q[i4][k1] * R[k1][j];
	        }
	    }
    }

#pragma endscop
}
