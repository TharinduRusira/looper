#define N 100
#define M 100

int main(){

float A[N][M];
float s[M];
float q[N];
float p[M];
float r[N];

int i1, j, i2;

 	for (i1 = 0; i1 < M; i1++){
        s[i1] = 0;
     }
    for (i2 = 0; i2 < N; i2++)
    {
        q[i2] = 0.0;
        for (j = 0; j < M; j++)
	    {
	        s[j] = s[j] + r[i2] * A[i2][j];
	        q[i2] = q[i2] + A[i2][j] * p[j];
	    }
    }
return 0;
}
