#define N 1000

float alpha = 1.5;
float beta = 1.2;

float A[N][N];
float B[N][N];
float tmp[N];
float x[N];
float y[N];

int i1,j1;

void main(){
    for(i1=0;i1<N;i1++){
        tmp[i1] = 0.0;
        y[i1] = 0.0;
        for(j1=0; j1< N; j1++){
            tmp[i1] = A[i1][j1]*x[j1] + tmp[i1];
            y[i1] = B[i1][j1]*x[j1] + y[i1];
        }
        y[i1] = alpha*tmp[i1] + beta*y[i1];
    }


}