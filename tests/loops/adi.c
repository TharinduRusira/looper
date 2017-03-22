#define N 1000
#define TSTEPS 1000

float u[N][N];
float v[N][N];
float p[N][N];
float q[N][N];

float DX, DY, DT;
float B1, B2;
float mul1, mul2;
float a,b,c,d,e,f;

int t, i1, j1, i2, j2, j3, j4;

void main(){

    DX = 1.0/N;
    DY = 1.0/N;
    DT = 1.0/TSTEPS;
    B1 = 2.0;
    B2 = 1.0;
    mul1 = B1 * DT / (DX * DX);
    mul2 = B2 * DT / (DY * DY);

    a = -1.0* mul1 /  2.0;
    b = 1.0 + mul1;
    c = a;
    d = -1.0*mul2 / 2.0;
    e = 1.0 + mul2;
    f = d;

    for (t=1; t<=TSTEPS; t++) {
    //Column Sweep
        for (i1=1; i1<N-1; i1++) {
            v[0][i1] = 1.0;
            p[i1][0] = 0.0;
            q[i1][0] = v[0][i1];
            for (j1=1; j1<N-1; j1++) {
                p[i1][j1] = -c / (a*p[i1][j1-1]+b);
                q[i1][j1] = (-d*u[j1][i1-1]+(1.0+ 2.0*d)*u[j1][i1] - f*u[j1][i1+1]-a*q[i1][j1-1])/(a*p[i1][j1-1]+b);
            }

            v[N-1][i1] = 1.0;
            for (j2=N-2; j2>=1; j2--) {
                v[j2][i1] = p[i1][j2] * v[j2+1][i1] + q[i1][j2];
            }
        }
        //Row Sweep
        for (i2=1; i2<N-1; i2++) {
            u[i2][0] = 1.0;
            p[i2][0] = 0.0;
            q[i2][0] = u[i2][0];
            for (j3=1; j3<N-1; j3++) {
                p[i2][j3] = -f / (d*p[i2][j3-1]+e);
                q[i2][j3] = (-a*v[i2-1][j3]+(1.0+2.0*a)*v[i2][j3] - c*v[i2+1][j3]-d*q[i2][j3-1])/(d*p[i2][j3-1]+e);
            }
            u[i2][N-1] = 1.0;
            for (j4=N-2; j4>=1; j4--) {
                u[i2][j4] = p[i2][j4] * u[i2][j4+1] + q[i2][j4];
            }
        }
    }
}
