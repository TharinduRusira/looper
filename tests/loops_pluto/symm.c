#define M 1000
#define N 1000

float alpha = 1.5;
float beta = 1.2;

float A[M][M];
float B[M][N];
float C[M][N];

float tmp2;

int i1,j,k1;

void main(){
#pragma scop
    for(i1=0;i1<M;i1++){
        for(j=0;j<N;j++){
            tmp2 = 0.0;
            for(k1=0; k1<i1;k1++){
                C[k1][j] = C[k1][j] + alpha*B[i1][j] * A[i1][k1];
                tmp2 = tmp2 + B[k1][j] * A[i1][k1];
            }
            C[i1][j] = beta * C[i1][j] + alpha*B[i1][j] * A[i1][i1] + alpha * tmp2;
        }
    }
#pragma endscop

}
