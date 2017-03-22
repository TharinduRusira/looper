#define N 1000
#define M 1000

float alpha = 1.5;
float beta = 1.2;

float A[N][M];
float B[N][M];
float C[N][N];

int i1, j1, k1, j2;

void main(){
    for (i1 = 0; i1 < N; i1++) {
        for (j1 = 0; j1 <= i1; j1++){
            C[i1][j1] = beta*C[i1][j1];
         }
        for (k1 = 0; k1 < M; k1++){
            for (j2 = 0; j2 <= i1; j2++)
            {
                C[i1][j2] = C[i1][j2] + A[j2][k1]*alpha*B[i1][k1] + B[j2][k1]*alpha*A[i1][k1];
            }
        }
  }

}