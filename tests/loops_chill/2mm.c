#define I 1000
#define J 1000
#define K 1000
#define L 1000

float alpha = 1.5;
float beta = 1.2;

float tmp[I][J];
float A[I][K];
float B[K][J];
float C[J][L];
float D[I][L];

int i1, j, k1, i2,j2, k2;

void main(){
    for (i1 = 0; i1 < I; i1++){
        for (j = 0; j < J; j++)
        {
            tmp[i1][j] = 0.0;
            for (k1 = 0; k1 < K; ++k1){
                tmp[i1][j] = tmp[i1][j] + alpha * A[i1][k1] * B[k1][j];
            }
        }
    }
	for (i2 = 0; i2 < I; i2++){
        for (j2 = 0; j2 < L; j2++)
        {
	        D[i2][j2] = beta*D[i2][j2];
	        for (k2 = 0; k2 < J; ++k2){
	            D[i2][j2] = D[i2][j2] + tmp[i2][k2] * C[k2][j2];
	        }
        }
    }
}
