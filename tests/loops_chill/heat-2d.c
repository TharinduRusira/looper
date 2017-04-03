#define N 100
#define T 100
#define M 100



int main(){

float A[N][N][N];
int t, i,j;

for(t=1;t<T-1;t++){
    for(i=1;i<N-1;i++){
        for(j=2;j<M-1;j++){
            A[t][i][j] = (A[t-1][i][j-1] + A[t-1][i][j+1] + A[t-1][i][j] + A[t-1][i-1][j] + A[t-1][i+1][j])/5 ;
        }
    }
}
return 0;
}
