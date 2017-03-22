#define N 1000
#define M 1000

float A[][];
float s[];
float q[];
float p[];
float r[];

int i1, j1, i2;

void main(){
    for (i1 = 0; i1 < M; i1++){
        s[i1] = 0;
     }
    for (i2 = 0; i2 < N; i2++)
    {
        q[i2] = 0.0;
        for (j1 = 0; j1 < M; j1++)
	    {
	        s[j1] = s[j1] + r[i2] * A[i2][j1];
	        q[i2] = q[i2] + A[i2][j1] * p[j1];
	    }
    }

}
