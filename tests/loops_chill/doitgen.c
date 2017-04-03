#define nr 100
#define nq 100
#define np 100


void main(){

float A[nr][nq][np];
float C4[np][np];
float sum[np];

int r1, q1, p1,s1, p2;

 	for (r1 = 0; r1 < nr; r1++){
        for (q1 = 0; q1 < nq; q1++)  {
            for (p1 = 0; p1 < np; p1++)  {
	            sum[p1] = 0.0;
	            for (s1 = 0; s1 < np; s1++){
	                sum[p1] = sum[p1] + A[r1][q1][s1] * C4[s1][p1];
	            }
            }
            for (p2 = 0; p2 < np; p2++){
	            A[r1][q1][p2] = sum[p2];
	        }
        }
    }

}
