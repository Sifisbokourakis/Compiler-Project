#include <stdio.h>

int main()
{
int x ;
int fibonacci ;
int T$1 ;
int T$3 ;
int T$5 ;
int y ;
int T$6 ;
int T$7 ;
int z ;
int isPrime ;
int i ;
int k ;
int t ;
int T$8 ;
int T$11 ;

L1: 
L2: if (x <= 1) goto L4;
L3: goto L6;
L4: fibonacci=x;
L5: goto L16;
L6: T$1=x-1;
L7: 
L8: 
L9: 
L10: T$3=x-2;
L11: 
L12: 
L13: 
L14: T$5=fibonacci+fibonacci;
L15: fibonacci=T$5;
L16: 
L17: 
L18: T$6=y/x;
L19: T$7=T$6*x;
L20: if (y == T$7) goto L22;
L21: goto L24;
L22: z=1;
L23: goto L25;
L24: z=0;
L25: 
L26: 
L27: isPrime=1;
L28: i=2;
L29: if (i < k) goto L31;
L30: goto L42;
L31: 
L32: 
L33: 
L34: 
L35: if (t == 1) goto L37;
L36: goto L39;
L37: isPrime=0;
L38: goto L39;
L39: T$8=i+1;
L40: i=T$8;
L41: goto L29;
L42: 
L43: 
L44: scanf("%d",&x);
L45: 
L46: 
L47: 
L48: printf("%d\n",fibonacci);
L49: i=2;
L50: if (i <= 30) goto L52;
L51: goto L62;
L52: 
L53: 
L54: 
L55: if (isPrime == 1) goto L57;
L56: goto L59;
L57: printf("%d\n",i);
L58: goto L59;
L59: T$11=i+1;
L60: i=T$11;
L61: goto L50;
L62: 
L63: 
}

