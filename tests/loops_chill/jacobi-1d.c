#define N 100
#define TSTEPS 100


void main(){

float A[N];
float B[N];

int t, i1,i2;

    for (t = 0; t < TSTEPS; t++)
    {
        for (i1 = 1; i1 < N-1; i1++){
	        B[i1] = 0.33333 * (A[i1-1] + A[i1] + A[i1 + 1]);
	    }
        for (i2 = 1; i2 < N-1; i2++){
	        A[i2] = 0.33333 * (B[i2-1] + B[i2] + B[i2 + 1]);
	    }
    }

}
