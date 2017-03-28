#define N 1000

float A[N][N];
float b[N];
float x[N];
float y[N];

float w;

int i1,j,k1, j2,k2, i2, j3, i3, j4;

void main(){
#pragma scop
    for (i1 = 0; i1 < N; i1++) {
        for (j = 0; j <i1; j++) {
            w = A[i1][j];
            for (k1 = 0; k1 < j; k1++) {
                w = w -  A[i1][k1] * A[k1][j];
            }
            A[i1][j] = w / A[j][j];
        }
        for (j2 = i1; j2 < N; j2++) {
            w = A[i1][j2];
            for (k2 = 0; k2 < i1; k2++) {
                w = w - A[i1][k2] * A[k2][j2];
            }
            A[i1][j2] = w;
        }
    }

    for (i2 = 0; i2 < N; i2++) {
        w = b[i2];
        for (j3 = 0; j3 < i2; j3++){
            w = w - A[i2][j3] * y[j3];
        }
        y[i2] = w;
    }

    for (i3 = N-1; i3 >=0; i3--) {
        w = y[i3];
        for (j4 = i3+1; j4 <  N; j4++)
            w = w - A[i3][j4] * x[j4];
        x[i3] = w / A[i3][i3];
    }
#pragma endscop
}
