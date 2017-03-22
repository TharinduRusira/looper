#define TMAX 1000
#define NX 1000
#define NY 1000

float ex[NX][NY];
float ey[NX][NY];
float hz[NX][NY];
float _fict_[TMAX];

int t, i1, j1, i2,j2, i3, j3, j4;

void main(){

    for(t = 0; t < TMAX; t++)
    {
        for (j1 = 0; j1 < NY; j1++){
	        ey[0][j1] = _fict_[t];
	     }

        for (i1 = 1; i1 < NX; i1++){
	        for (j2 = 0; j2 < NY; j2++){
	            ey[i1][j2] = ey[i1][j2] - 0.5*(hz[i1][j2]-hz[i1-1][j2]);
	        }
	    }
        for (i2 = 0; i2 < NX; i2++){
	        for (j3 = 1; j3 < NY; j3++){
	            ex[i2][j3] = ex[i2][j3] - 0.5*(hz[i2][j3]-hz[i2][j3-1]);
	        }
	    }
        for (i3 = 0; i3 < NX - 1; i3++){
	        for (j4 = 0; j4 < NY - 1; j4++){
	            hz[i3][j4] = hz[i3][j4] - 0.7*  (ex[i3][j4+1] - ex[i3][j4] + ey[i3+1][j4] - ey[i3][j4]);
	        }
	     }
    }


}