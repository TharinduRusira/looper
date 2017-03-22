#define M 1000
#define N 1000

float data[N][M];
float cov[M][M];
float mean[M];

int i1,j1,k1, i2,j2,k2, i3,j3,k3 ;

void main(){

    for (j1 = 0; j1 < M; j1++){
        mean[j1] = 0.0;
        for (i1 = 0; i1 < N; i1++){
            mean[j] += data[i][j];
         }
         mean[j1] = mean[j1]/(N*1.0);
     }

    for (i2 = 0; i2 < N; i2++){
        for (j2 = 0; j2 < M; j2++){
          data[i2][j2] = data[i2][j2] - mean[j2];
        }
    }

    for (i3 = 0; i3 < M; i3++){
        for (j3 = i3; j3 < M; j3++){
            cov[i3][j3] = 0.0;
            for (k3 = 0; k3 < N; k3++){
                cov[i3][j3] += data[k3][i3] * data[k3][j3];
            }
            cov[i3][j3] = cov[i3][j3]/(N-1)*1.0;
            cov[j3][i3] = cov[i3][j3];
          }
     }

}