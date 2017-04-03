#define H 100
#define W 100


void main(){

float alpha = 0.25;

float imgIn[W][H];
float imgOut[W][H];
float y1[W][H];
float y2[W][H];


float xm1, tm1, ym1, ym2;
float xp1, xp2;
float tp1, tp2;
float yp1, yp2;
float k;

float a1, a2, a3, a4, a5, a6,a7, a8, b1,b2, c1, c2;

int i1,j, i2,j2, i3,j3, i4,j4, i5,j5, i6,j6;

   k = 5.0* alpha; // omitting the computation of exponential expression
   a1 = a5 = k;
   a2 = a6 = k*2*alpha;
   a3 = a7 = k*3* alpha;
   a4 = a8 = -1.0*k*4* alpha;
   b1 =  16.0 * alpha;
   b2 = 32.0 * alpha;
   c1 = c2 = 1;
   for (i1=0; i1< W; i1++) {
        ym1 = 0.0;
        ym2 = 0.0;
        xm1 = 0.0;
        for (j=0; j<H; j++) {
            y1[i1][j] = a1*imgIn[i1][j] + a2*xm1 + b1*ym1 + b2*ym2;
            xm1 = imgIn[i1][j];
            ym2 = ym1;
            ym1 = y1[i1][j];
        }
    }

    for (i2=0; i2<W; i2++) {
        yp1 = 0.0;
        yp2 = 0.0;
        xp1 = 0.0;
        xp2 = 0.0;
        for (j2= H-1; j2>=0; j2--) {
            y2[i2][j2] = a3*xp1 + a4*xp2 + b1*yp1 + b2*yp2;
            xp2 = xp1;
            xp1 = imgIn[i2][j2];
            yp2 = yp1;
            yp1 = y2[i2][j2];
        }
    }

   for (i3=0; i3<W; i3++){
        for (j3=0; j3<H; j3++) {
            imgOut[i3][j3] = c1 * (y1[i3][j3] + y2[i3][j3]);
        }
   }

    for (j4=0; j4<H; j4++) {
        tm1 = 0.0;
        ym1 = 0.0;
        ym2 = 0.0;
        for (i4=0; i4<W; i4++) {
            y1[i4][j4] = a5*imgOut[i4][j4] + a6*tm1 + b1*ym1 + b2*ym2;
            tm1 = imgOut[i4][j4];
            ym2 = ym1;
            ym1 = y1 [i4][j4];
        }
    }


    for (j5=0; j5<H; j5++) {
        tp1 = 0.0;
        tp2 = 0.0;
        yp1 = 0.0;
        yp2 = 0.0;
        for (i5=W-1; i5>=0; i5--) {
            y2[i5][j5] = a7*tp1 + a8*tp2 + b1*yp1 + b2*yp2;
            tp2 = tp1;
            tp1 = imgOut[i5][j5];
            yp2 = yp1;
            yp1 = y2[i5][j5];
        }
    }

    for (i6=0; i6<W; i6++){
        for (j6=0; j6<H; j6++){
            imgOut[i6][j6] = c2*(y1[i6][j6] + y2[i6][j6]);
        }
    }
}
