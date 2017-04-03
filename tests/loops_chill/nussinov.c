#define N 100

#define match(b1, b2) (((b1)+(b2)) == 3 ? 1 : 0)
#define max_score(s1, s2) ((s1 >= s2) ? s1 : s2)


void main(){

float seq[N];
float table[N][N];

int i1, j, k1;

    for (i1 = N-1; i1 >= 0; i1--) {
        for (j=i1+1; j<N; j++) {
            if (j-1>=0)
                table[i1][j] = max_score(table[i1][j], table[i1][j-1]);
            if (i1+1<N)
                table[i1][j] = max_score(table[i1][j], table[i1+1][j]);

            if (j-1>=0 && i1+1<N) {
            /* don't allow adjacent elements to bond */
                if (i1<j-1)
                    table[i1][j] = max_score(table[i1][j], table[i1+1][j-1]+match(seq[i1], seq[j]));
                else
                    table[i1][j] = max_score(table[i1][j], table[i1+1][j-1]);
            }

            for (k1=i1+1; k1<j; k1++) {
                table[i1][j] = max_score(table[i1][j], table[i1][k1] + table[k1+1][j]);
            }
        }
    }
}
