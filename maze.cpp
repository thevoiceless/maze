/* Riley Moses */

#include <cstdlib>
#include <iostream>

#include "IOstuff.h"

using namespace std;

string filename = "";
vector<Line> lines;
int numVillages, numLines;

int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		filename = "input.txt";
	}
	else
	{
		filename = argv[1];
	}

	readInputFile(filename, lines, numVillages, numLines);

	return 0;
}