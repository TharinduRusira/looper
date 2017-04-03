#define NI 100
#define NJ 100
#define NK 100
#define NL 100
#define NM 100

float E[NI][NJ];
float A[NI][NK];
float B[NK][NJ];
float F[NJ][NL];
float C[NJ][NM];
float D[NM][NL];
float G[NI][NL];


int i1, j, k1, i2,j2, k2, i3,j3,k3;

void main(){
	/* E := A*B */
    for (i1 = 0; i1 < NI; i1++){
        for (j = 0; j < NJ; j++)
        {
	        E[i1][j] = 0.0;
	        for (k1 = 0; k1 < NK; ++k1){
	            E[i1][j] = E[i1][j] + A[i1][k1] * B[k1][j];
	        }
        }
    }
    /* F := C*D */
    for (i2 = 0; i2 < NJ; i2++){
        for (j2 = 0; j2 < NL; j2++)
        {
	        F[i2][j2] = 0.0;
	        for (k2 = 0; k2 < NM; ++k2){
	            F[i2][j2] = F[i2][j2] + C[i2][k2] * D[k2][j2];
	        }
        }
    }
    /* G := E*F */
    for (i3 = 0; i3 < NI; i3++){
        for (j3 = 0; j3 < NL; j3++)
        {
	        G[i3][j3] = 0.0;
	        for (k3 = 0; k3 < NJ; ++k3){
	            G[i3][j3] = G[i3][j3] + E[i3][k3] * F[k3][j3];
	        }
        }
    }
}
