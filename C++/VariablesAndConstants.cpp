#include <iostream>

using namespace std;

//This program will calculate the area of a room in square meter

//int main()
//{	
//	int room_lenght;
//	int room_width;
//	int area;
//
//	cout << "What is your room length in meter: ";
//	cin >> room_lenght;
//
//	cout << "What is your room width in meter: ";
//	cin >> room_width;
//
//	area = room_lenght * room_width;
//	
//	cout << "The area of the room is " << area << " square meters." << endl;
//	return 0;
//}


/*
char type is used to represent single characters.
char = 1 byte (8 bits)
char16_6 = at least 2 bytes (16 bits)
char32_t = at least 4 bytes (32 bits)
wchar_t = largest available char set
*/

/*
(un)signed short int = at least 2 bytes (16 bits)
(un)signed int = at least 2 bytes (16 bits)
(un)signed long int = at least 4 bytes (32 bits)
(un)signed long long int = at least 8 bytes (64 bits)

unsigned vars are for nonnegative integers only
by default, integers are signed
*/

/*
float = 7 decimal digits
double = 15 decimal digits
long double = 19 decimal digits
*/

int main()
{
	char middle_initial{ 'j' }; //notice the single quotes around characters
	cout << "my middle initial is" << endl;

	unsigned short int exam_score{ 55 };
	cout << "my exam score is " << exam_score << endl;

	int countries_represented{ 65 };
	cout << "there were " << countries_represented << " countries represented in my meeting" << endl;

	long people_in_florida{ 20'610'000 };
	cout << "there are about " << people_in_florida << " people in florida" << endl;

	long long people_in_world{ 20'610'000'000 };
	cout << "there are about " << people_in_world << " people in florida" << endl;

	float car_payment{ 401.23 };
	double pi{ 3.14159 };
	long double large_amount{ 2.7e120 };

	bool gameover{ false };
	cout << "the value of gameover is " << gameover << endl;

	//be careful when you do math operations
	short val1{ 3000 };
	short val2{ 15000 };
	short product;

	product = val1 * val2;

	cout << "the multiplication result is: " << product << endl;

	//this will give a false answer since the multiplication result will not fit in short type


	//sizeof operator -> determines the size in bytes of a type or variable

	sizeof(int);
	sizeof(product);

	// <climits> includes the info for min max vals of types
	// char_max long_max llong_max...

	/*
	constants:
	literal constants
	declerad constants
	constant expressions
	enumerated constants
	defined constants
	*/

	//declared constant
	const double pi{ 3.14159 };
	
	#define pi 3.14159; //do not use these types of constants in modern c++

	return 0;
}
