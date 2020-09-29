#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
	int num1 = 0, num2 = 0;
	printf("Fizz Buzz Code Challenge:\nFirst, enter 2 numbers and you will get fizz for multiples\nof the first number and buzz for multiples of the second.\n\n");
	// Taking in 1st and second number
	printf("Enter the first number:\n");
	scanf("%d",&num1);
	
	printf("Enter the second number:\n");
        scanf("%d",&num2);
	
	// Taking through for loop to 100
	for(int  i = 1; i<=100;i++)
	{
		if(i%num1==0 && i%num2!=0) // If I is divisible by number 1 and not divisible by number 2 print Fizz  
			printf("Fizz ");
		else if(i%num2==0 && i%num1!=0) // If I is divisible by number 2 and not divisible by number 1 print Buzz
			printf("Buzz ");
		else if(i%num1==0 && i%num2==0) // If I is divisible by number 1 and divisible by number 2 print FizzBuzz
			printf("FizzBuzz ");
		else // Just print the number of I
		{	
			printf("%d ",i);
			
		}
		 if(i%10==0) // This is to line up the number to print 10 then a newline
			printf("\n");
	}



	return 0;
}
