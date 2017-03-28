#define N 1000
#define M 1000

float A[M][N];
float x[N];
float y[N];
float tmp[M];

int i1, j, i2,j2;

void main(){
    for (i1 = 0; i1 < N; i1++){
        y[i1] = 0;
    }

    for (i2 = 0; i2 < M; i2++)
    {
        tmp[i2] = 0.0;
        for (j = 0; j < N; j++){
	        tmp[i2] = tmp[i2] + A[i2][j] * x[j1];
            for (j2 = 0; j2 < N; j2++){
	            y[j2] = y[j2] + A[i2][j2] * tmp[i2];
	        }
	     }
    }
}
