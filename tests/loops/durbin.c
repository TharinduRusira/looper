#define N 1000

float r[N];
float y[N];

float z[N];
float alpha;
float beta;
float sum;

int i1,k1, i2, i3;

void main(){

    y[0] = -1.0*r[0];
    beta = 1.0;
    alpha = -1.0 * r[0];

    for (k1 = 1; k1 < N; k1++) {
        beta = (1-alpha*alpha)*beta;
        sum = 0.0;
        for (i1=0; i1<k1; i1++) {
            sum = sum + r[k1-i1-1]*y[i1];
        }
        alpha = -1.0* (r[k1] + sum)/beta;

        for (i2=0; i2<k1; i2++) {
            z[i2] = y[i2] + alpha*y[k1-i2-1];
        }
        for (i3=0; i3<k1; i3++) {
            y[i3] = z[i3];
        }
        y[k1] = alpha;
    }



}