#include<stdio.h>
main()
{
int i;
int j;
int contador = 0;
  for (i = 1; i<= 9; i++){
    if( i!=3){
      for (j = 1; j<=6; j++){
          printf("oi\n");
          contador = contador + 1;
          }
    }
  }
printf ("o numero de vezes que 'oi' foi impresso foi: %d", contador);

//resultado do contador: 48
//explicação: 'oi' eh impresso em todas as instancias do laco exceto quando i = 3
}
