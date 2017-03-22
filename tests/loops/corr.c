#define N 1000
#define M 1000

float data[N][M];
float corr[M][M];
float mean[M];
float stddev[M];

int i1,j1,k1, i2,j2,k2, i3,j3,k3;

void main(){

    for(j1=0;j1<M;j1++){
        mean[j] = 0.0;
        for(i1=0;i1<N;i1++){
            mean[j1] += data[i1][j1];
        }
        mean[j1] = mean[j1]/(N*1.0);
    }

    for(j2=0;j2<M;j2++){
        stddev[j2] = 0.0;
        for(i2=0;i2<N;i2++){
            stddev[j2] += (data[i2][j2] - mean[j2]) * (data[i2][j2] - mean[j2]);
        }
        stddev[j2] = stddev[j2]/(N*1.0);
        // should take the sqrt but we omit that for now
    }

    // omit 'reduce column vectors' loop
    for(i3=0;i3 < M-1; i3++){
        corr[i3][i3] = 0.0;
        for(j3 = i3+1; j3< M; j3++){
            corr[i3][j3] = 0.0;
            for(k3=0; k3< N; k3++){
                corr[i3][j3] += data[k3][i3] * data[k3][j3];
            }
            corr[j3][i3] = corr[i3][j3];
        }
    }

    corr[M-1][M-1] = 1.0;


}