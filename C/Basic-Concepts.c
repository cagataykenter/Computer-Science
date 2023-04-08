#include <stdio.h>
#include <stdbool.h>

int main()
{
    //Basic Concepts
    char str[100];
    int i;

    printf("Enter a value: ");

    //read input in specific format
    scanf("%s %d", str, &i);

    printf("\nYou entered: %s %d\n", str, i);

    //Basic Data Types
    int age;
    float gpa;
    double gravity;
    _Bool trueFalse = 1; //equals to 'bool trueFalse = true' in c99 standard

    //C offers three adj keywords to modify basic int, and double
    //short, long and unsigned
    //unsigned is used for variables that have only nonnegative values


    //define a variable and specify the valid values that could be stored into that variable
    enum primaryColor {red, yellow, blue};
    
    //declare variable to be of type enum primaryColor
    enum primaryColor myColor;

    //this will assign the value 0 to myColor
    myColor = red;

    //this will set the values of data types as: 0, 1, 10, 11
    enum dir {up, down, left = 10, right};

    //char declares single characters or numbers
    char isTrue;
    isTrue = 'T';
    /*
    These are not okay:
    isTrue = T;
    isTrue = "T";
    */

    char grade = 65; /* ok for ASCII, but poor style */

    //escape chars
    char x = '\n';


}   

