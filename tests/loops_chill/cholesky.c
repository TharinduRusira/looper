#define N 1000
#include <math.h>

float A[N][N];

int i1, j, k1, k2;

void main(){
    for (i1 = 0; i1 < N; i1++) {
     //j<i
        for (j = 0; j < i1; j++) {
            for (k1 = 0; k1 < j; k1++) {
                A[i1][j] = A[i1][j] - A[i1][k1] * A[j][k1];
            }
            A[i1][j] = A[i1][j]/A[j][j];
        }
        // i==j case
        for (k2 = 0; k2 < i1; k2++) {
            A[i1][i1] = A[i1][i1] - A[i1][k2] * A[i1][k2];
        }

        A[i1][i1] = sqrt(A[i1][i1]);
  }

}
