#define I 1000
#define J 1000
#define K 1000

float alpha = 5.0;
float beta = 10.0;

float A[I][K];
float B[K][J];
float C[I][J];

int i1,j1,k1;

void main(){

    for(i1=0;i1<I; i1++){
        for(j1=0;j1<J; j1++){
            C[i1][j1] = C[i1][j1]*beta;
            for(k1=0;k1<K; k1++){
                C[i1][j1] = C[i1][j1] + alpha*A[i1][k1]*B[k1][j1];
            }
        }
    }
}