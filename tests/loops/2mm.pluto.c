#include <math.h>
#define ceild(n,d)  ceil(((double)(n))/((double)(d)))
#define floord(n,d) floor(((double)(n))/((double)(d)))
#define max(x,y)    ((x) > (y)? (x) : (y))
#define min(x,y)    ((x) < (y)? (x) : (y))

#define I 1000
#define J 1000
#define K 1000
#define L 1000

float alpha = 1.5;
float beta = 1.2;

float tmp[I][J];
float A[I][K];
float B[K][J];
float C[J][L];
float D[I][L];

int i1, j, k1, i2,j2, k2;

void main(){
/* Copyright (C) 1991-2016 Free Software Foundation, Inc.
   This file is part of the GNU C Library.

   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <http://www.gnu.org/licenses/>.  */
/* This header is separate from features.h so that the compiler can
   include it implicitly at the start of every compilation.  It must
   not itself include <features.h> or any other header that includes
   <features.h> because the implicit include comes before any feature
   test macros that may be defined in a source file before it first
   explicitly includes a system header.  GCC knows the name of this
   header in order to preinclude it.  */
/* glibc's intent is to support the IEC 559 math functionality, real
   and complex.  If the GCC (4.9 and later) predefined macros
   specifying compiler intent are available, use them to determine
   whether the overall intent is to support these features; otherwise,
   presume an older compiler has intent to support these features and
   define these macros by default.  */
/* wchar_t uses Unicode 8.0.0.  Version 8.0 of the Unicode Standard is
   synchronized with ISO/IEC 10646:2014, plus Amendment 1 (published
   2015-05-15).  */
/* We do not support C11 <threads.h>.  */
  int t1, t2, t3, t4, t5;
 register int lbv, ubv;
/* Start of CLooG code */
if (I >= 1) {
  if ((J >= L+1) && (L >= 1)) {
    for (t2=0;t2<=I-1;t2++) {
      lbv=0;
      ubv=L-1;
#pragma ivdep
#pragma vector always
      for (t3=lbv;t3<=ubv;t3++) {
        D[t2][t3] = beta*D[t2][t3];;
        tmp[t2][t3] = 0.0;;
      }
      lbv=L;
      ubv=J-1;
#pragma ivdep
#pragma vector always
      for (t3=lbv;t3<=ubv;t3++) {
        tmp[t2][t3] = 0.0;;
      }
    }
  }
  if ((J >= 1) && (J <= L-1)) {
    for (t2=0;t2<=I-1;t2++) {
      lbv=0;
      ubv=J-1;
#pragma ivdep
#pragma vector always
      for (t3=lbv;t3<=ubv;t3++) {
        D[t2][t3] = beta*D[t2][t3];;
        tmp[t2][t3] = 0.0;;
      }
      lbv=J;
      ubv=L-1;
#pragma ivdep
#pragma vector always
      for (t3=lbv;t3<=ubv;t3++) {
        D[t2][t3] = beta*D[t2][t3];;
      }
    }
  }
  if ((J >= 1) && (J == L)) {
    for (t2=0;t2<=I-1;t2++) {
      lbv=0;
      ubv=J-1;
#pragma ivdep
#pragma vector always
      for (t3=lbv;t3<=ubv;t3++) {
        D[t2][t3] = beta*D[t2][t3];;
        tmp[t2][t3] = 0.0;;
      }
    }
  }
  if ((J >= 1) && (L <= 0)) {
    for (t2=0;t2<=I-1;t2++) {
      lbv=0;
      ubv=J-1;
#pragma ivdep
#pragma vector always
      for (t3=lbv;t3<=ubv;t3++) {
        tmp[t2][t3] = 0.0;;
      }
    }
  }
  if ((J <= 0) && (L >= 1)) {
    for (t2=0;t2<=I-1;t2++) {
      lbv=0;
      ubv=L-1;
#pragma ivdep
#pragma vector always
      for (t3=lbv;t3<=ubv;t3++) {
        D[t2][t3] = beta*D[t2][t3];;
      }
    }
  }
  if ((J >= 1) && (K >= 1) && (L >= 1)) {
    for (t2=0;t2<=I-1;t2++) {
      for (t3=0;t3<=J-1;t3++) {
        for (t5=0;t5<=K-1;t5++) {
          tmp[t2][t3] = tmp[t2][t3] + alpha * A[t2][t5] * B[t5][t3];;
        }
        lbv=0;
        ubv=L-1;
#pragma ivdep
#pragma vector always
        for (t5=lbv;t5<=ubv;t5++) {
          D[t2][t5] = D[t2][t5] + tmp[t2][t3] * C[t3][t5];;
        }
      }
    }
  }
  if ((J >= 1) && (K >= 1) && (L <= 0)) {
    for (t2=0;t2<=I-1;t2++) {
      for (t3=0;t3<=J-1;t3++) {
        for (t5=0;t5<=K-1;t5++) {
          tmp[t2][t3] = tmp[t2][t3] + alpha * A[t2][t5] * B[t5][t3];;
        }
      }
    }
  }
  if ((J >= 1) && (K <= 0) && (L >= 1)) {
    for (t2=0;t2<=I-1;t2++) {
      for (t3=0;t3<=J-1;t3++) {
        lbv=0;
        ubv=L-1;
#pragma ivdep
#pragma vector always
        for (t5=lbv;t5<=ubv;t5++) {
          D[t2][t5] = D[t2][t5] + tmp[t2][t3] * C[t3][t5];;
        }
      }
    }
  }
}
/* End of CLooG code */
}
