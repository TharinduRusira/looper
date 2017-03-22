#define N 1000

float L[N][N];
float x[N];
float b[N];

int i1,j1;

void main(){

    for (i1 = 0; i1 < N; i1++)
    {
        x[i1] = b[i1];
        for (j1 = 0; j1 <i1; j1++){
            x[i1] = x[i1] - L[i1][j1] * x[j1];
        }
        x[i1] = x[i1] / L[i1][i1];
    }
}