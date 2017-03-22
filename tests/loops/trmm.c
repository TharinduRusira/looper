#define M 1000
#define N 1000

float alpha = 1.5;
float beta = 1.2;

float A[M][M];
float B[M][N];

int i1,j1,k1    ;

void main(){
    for (i1 = 0; i1 < M; i1++){
        for (j1 = 0; j1 < N; j1++) {
            for (k1 = i1+1; k1 < M; k1++){
                B[i1][j1] = B[i1][j1] + A[k1][i1] * B[k1][j1];
            }
            B[i1][j1] = alpha * B[i1][j1];
        }
    }
}