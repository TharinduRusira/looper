#define N 100


int main(){

float L[N][N];
float x[N];
float b[N];

int i1,j;

    for (i1 = 0; i1 < N; i1++)
    {
        x[i1] = b[i1];
        for (j = 0; j <i1; j++){
            x[i1] = x[i1] - L[i1][j] * x[j];
        }
        x[i1] = x[i1] / L[i1][i1];
    }
    return 0;
}
