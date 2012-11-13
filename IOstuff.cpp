#include "IOstuff.h"

void readInputFile(string& filename, vector<Line>& lines, int& numVillages, int& numLines)
{
	ifstream inFile(filename.c_str());
	if (!inFile.is_open())
	{
		cout << "Error opening " << filename << endl;
		exit(1);
	}

	char p1, p2, c, t;
	inFile >> numVillages >> numLines;
	for (int i = 0; i < numLines; ++i)
	{
		inFile >> p1 >> p2 >> c >> t;
		lines.push_back(Line(p1, p2, c, t));
	}
}