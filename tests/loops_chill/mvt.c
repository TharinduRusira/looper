#define N 100


void main(){

float x1[N];
float x2[N];
float y_1[N];
float y_2[N];
float A[N][N];

int i1,j,i2,j2;

 	for (i1 = 0; i1 < N; i1++){
        for (j = 0; j < N; j++){
            x1[i1] = x1[i1] + A[i1][j] * y_1[j];
        }
    }
    for (i2 = 0; i2 < N; i2++){
        for (j2 = 0; j2 < N; j2++){
            x2[i2] = x2[i2] + A[j2][i2] * y_2[j2];
        }
    }
}
