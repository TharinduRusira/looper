#define N 100
#define TSTEPS 1000

float A[N][N][N];
float B[N][N][N];

int t, i1,j1,k1, i2,j2, k2;

void main(){

    for (t = 1; t <= TSTEPS; t++) {
        for (i1 = 1; i1 < N-1; i1++) {
            for (j1 = 1; j1 < N-1; j1++) {
                for (k1 = 1; k1 < N-1; k1++) {
                    B[i1][j1][k1] =   0.125 * (A[i1+1][j1][k1] - 2.0 * A[i1][j1][k1] + A[i1-1][j1][k1])
                                     + 0.125 * (A[i1][j1+1][k1] - 2.0 * A[i1][j1][k1] + A[i1][j1-1][k1])
                                     + 0.125 * (A[i1][j1][k1+1] - 2.0 * A[i1][j1][k1] + A[i1][j1][k1-1])
                                     + A[i1][j1][k1];
                }
            }
        }
        for (i2 = 1; i2 < N-1; i2++) {
            for (j2 = 1; j2 < N-1; j2++) {
                for (k2 = 1; k2 < N-1; k2++) {
                    A[i2][j2][k2] =   (0.125) * (B[i2+1][j2][k2] - (2.0) * B[i2][j2][k2] + B[i2-1][j2][k2])
                                    + (0.125) * (B[i2][j2+1][k2] - (2.0) * B[i2][j2][k2] + B[i2][j2-1][k2])
                                    + (0.125) * (B[i2][j2][k2+1] - (2.0) * B[i2][j2][k2] + B[i2][j2][k2-1])
                                    + B[i2][j2][k2];
                }
            }
        }
     }

}