#include <iostream>
#include <vector>

using namespace std;

//arrays just like they are in python etc.

int rakamlar[10]; //cannot change the size

// Vectors can grow unlike the arrays. Much more efficient.
// All vector elements must be same type

vector <char> vowels (5);
vector <int> test_scores { 75, 80, 55, 30, 80, 65 };

int main()
{
	//arrays
	cout << rakamlar[0] << endl;
	cout << rakamlar[9] << endl;

	int matris[3][2]; //rows cols matrix, multiple dimension arrays

	//vectors
	cout << test_scores[0] << endl;
	cout << test_scores.at(0) << endl; //same as above

	test_scores.push_back(95); //this will add 95 to the end of the vector test_scores

	cout << test_scores.size() << endl; // returns the length of vector

	int vector_length = test_scores.size();
	cout << test_scores[vector_length-1] << endl; // get the last element of vector

	vector <vector<int>> movie_ratings //nested vectors
	{
		{1,2,3,4},
		{2,4,1,3}
	};

	return 0;
}
