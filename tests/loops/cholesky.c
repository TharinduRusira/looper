#define N 1000

float A[N][N];

int i1, j1, k1, k2;

void main(){

    for (i1 = 0; i1 < N; i1++) {
     //j<i
        for (j1 = 0; j1 < i1; j1++) {
            for (k1 = 0; k1 < j1; k1++) {
                A[i1][j1] = A[i1][j1] - A[i1][k1] * A[j1][k1];
            }
            A[i1][j1] = A[i1][j1]/A[j1][j1];
        }
        // i==j case
        for (k2 = 0; k2 < i1; k2++) {
            A[i1][i1] = A[i1][i1] - A[i1][k2] * A[i1][k2];
        }

        // sqrt step omitted A[i][i] = SQRT_FUN(A[i][i]);
  }


}