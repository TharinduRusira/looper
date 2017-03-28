


// this source derived from CHILL AST originally from file 'matvec_10000.c' as parsed by frontend compiler rose


#define N 10000

int main(  )
{
  int chill_t1;
  int i;
  int j;
  int A[10000][10000];
  int B[10000];
  int C[10000];
  for (i = 0; i < 10000; i++) {
    C[chill_t1] = 0;
    for (j = 0; j < 10000; j++) {
      C[i] = (C[i] + A[i][j] * B[j]);
    }
  }
  return(0);

}
