#define M 1000
#define N 1000

float alpha = 1.5;
float beta = 1.2;

float A[M][M];
float B[M][N];
float C[M][N];

float tmp2;

int i1,j1,k1;

void main(){
    for(i1=0;i1<M;i1++){
        for(j1=0;j1<N;j1++){
            tmp2 = 0.0;
            for(k1=0; k1<i1;k1++){
                C[k1][j1] = C[k1][j1] + alpha*B[i1][j1] * A[i1][k1];
                tmp2 = tmp2 + B[k1][j1] * A[i1][k1];
            }
            C[i1][j1] = beta * C[i1][j1] + alpha*B[i1][j1] * A[i1][i1] + alpha * tmp2;
        }
    }


}