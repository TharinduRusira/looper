#define N 1000

float path[N][N];

int i1, j1, k1;

void main(){

    for (k1 = 0; k1 < N; k1++)
    {
        for(i1 = 0; i1 < N; i1++){
	        for (j1 = 0; j1 < N; j1++){
	            path[i1][j1] = path[i1][j1] < path[i1][k1] + path[k1][j1] ? path[i1][j1] : path[i1][k1] + path[k1][j1];
	        }
	    }
    }
}