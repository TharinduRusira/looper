#define I 1000
#define J 1000
#define K 1000

float alpha = 5.0;
float beta = 10.0;

float A[I][K];
float B[K][J];
float C[I][J];

int i1,j,k1;

void main(){

    for(i1=0;i1<I; i1++){
        for(j=0;j<J; j++){
            C[i1][j] = C[i1][j]*beta;
            for(k1=0;k1<K; k1++){
                C[i1][j] = C[i1][j] + alpha*A[i1][k1]*B[k1][j];
            }
        }
    }
}
