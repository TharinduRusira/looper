#define N 1000

float alpha = 5.0;
float beta = 10.0;

float A[N][N];
float u1[N];
float v1[N];
float u2[N];
float v2[N];
float w[N];
float x[N];
float y[N];
float z[N];

int i1,j, i2,j2, i3,j3, i4,j4;

void main(){
#pragma scop
 	for(i1=0;i1<N;i1++){
        for(j=0;j<N;j++){
                  A[i1][j] = A[i1][j] + u1[i1] * v1[j] + u2[i1] * v2[j];
        }
    }
    for (i2 = 0; i2 < N; i2++){
        for (j2 = 0; j2 < N; j2++){
            x[i2] = x[i2] + beta * A[j2][i2] * y[j2];
        }
    }

    for (i3 = 0; i3 < N; i3++){
        x[i3] = x[i3] + z[i3];
    }
    for (i4 = 0; i4 < N; i4++){
        for (j4 = 0; j4 < N; j4++){
            w[i4] = w[i4] +  alpha * A[i4][j4] * x[j4];
        }
    }
#pragma endscop
}

