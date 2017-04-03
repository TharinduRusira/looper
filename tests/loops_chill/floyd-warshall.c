#define N 100


int main(){

float path[N][N];

int i1, j, k1;

    for (k1 = 0; k1 < N; k1++)
    {
        for(i1 = 0; i1 < N; i1++){
	        for (j = 0; j < N; j++){
	            path[i1][j] = path[i1][j] < path[i1][k1] + path[k1][j] ? path[i1][j] : path[i1][k1] + path[k1][j];
	        }
	    }
    }
    return 0;
}
