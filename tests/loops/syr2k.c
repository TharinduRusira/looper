#define N 1000
#define M 1000

float alpha = 1.5;
float beta = 1.2;

float A[N][M];
float B[N][M];
float C[N][N];

int i1, j11, k1, j12;

void main(){
    for (i1 = 0; i1 < N; i1++) {
        for (j11 = 0; j11 <= i1; j11++){
            C[i1][j11] = beta*C[i1][j11];
         }
        for (k1 = 0; k1 < M; k1++){
            for (j12 = 0; j12 <= i1; j12++)
            {
                C[i1][j12] = C[i1][j12] + A[j12][k1]*alpha*B[i1][k1] + B[j12][k1]*alpha*A[i1][k1];
            }
        }
  }

}
