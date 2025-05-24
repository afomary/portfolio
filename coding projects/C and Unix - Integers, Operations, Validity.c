#Q1

#include <stdio.h>

int main() {
    int number;

    
    printf("Enter an integer: ");
    scanf("%d", &number);

    
    if (number % 2 == 0) {
        printf("%d is even.\n", number);
    } else {
        printf("%d is odd.\n", number);
    }

    return 0;
}

#Q2

#include <stdio.h>
#include <stdlib.h>
void main(){
	
	
	float X,Y,Z;
	
	printf("Enter the first angle X: "); 
	scanf("%f",&X); 
	
	printf("Enter the second angle Y: ");
	scanf("%f",&Y); 
	
	printf("Enter the third angle Z: ");
	scanf("%f",&Z);
	if((X+Y+Z == 180) && X!=0 && Y!=0 && Z!=0){
		
		printf("VALID");
	}
	else{
		printf("INVALID");
	}
}

#Q3

#include <stdio.h>
#include <math.h>
int main()
{
    double operand1, operand2;
    char operation;
    scanf("%lf %c %lf", &operand1, &operation, &operand2);
    switch (operation)
    {

    case '+':
        printf("%.2lf", operand1 + operand2);
        break;

    case '-':
        printf("%.2lf", operand1 - operand2);
        break;

    case '*':
        printf("%.2lf", operand1 * operand2);
        break;

    case '/':
        if (operand2 == 0)
        {
            printf("Error: dividing by zero");
        }
        else
        {
            printf("%.2lf", operand1 / operand2);
        }
        break;

    case '%':
        if (operand2 == 0)
        {
            printf("Error: modulo by zero");
        }
        else
        {
            int int_operand1 = (int)operand1;
            int int_operand2 = (int)operand2;
            printf("%d", int_operand1 % int_operand2);
        }
        break;
    case '^':
        printf("%.2lf", pow(operand1, operand2));
        break;
    case 'r':
        if (operand2 < 0)
        {
            printf("Error: Base can't be negative.");
        }
        else
        {
            printf("%.2lf", pow(operand2, (double)(1 / operand1)));
        }
        break;
    }
    return 0;
}

#Q4

#include <stdio.h>
 
int main()
{
    int dd,mm,yy;
     
    printf("Enter a year:"); 
	printf("Enter a month:");
	printf("Enter a day:");
	  
    scanf("%d", &yy);
	scanf("%d", &mm);
	scanf("%d", &dd);
     
    
    if(yy>=1900 && yy<=9999)
    {
        
        if(mm>=1 && mm<=12)
        {
            
            if((dd>=1 && dd<=31) && (mm==1 || mm==3 || mm==5 || mm==7 || mm==8 || mm==10 || mm==12))
                printf("The date is valid.\n");
            else if((dd>=1 && dd<=30) && (mm==4 || mm==6 || mm==9 || mm==11))
                printf("The date is valid.\n");
            else if((dd>=1 && dd<=28) && (mm==2))
                printf("The date is valid.\n");
            else if(dd==29 && mm==2 && (yy%400==0 ||(yy%4==0 && yy%100!=0)))
                printf("The date is valid.\n");
            else
                printf("The date is invalid.\n");
        }
        else
        {
            printf("The date is invalid.\n");
        }
    }
    else
    {
        printf("The date is invalid.\n");
    }
 
    return 0;    
}






