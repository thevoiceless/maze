#include "IOstuff.h"

void readInputFile(string& filename, vector<Line>& lines)
{
	ifstream inFile(filename.c_str());
	if (!inFile.is_open())
	{
		cout << "Error opening " << filename << endl;
		exit(1);
	}

	int numVillages, numEdges;
	char p1, p2, c, t;
	inFile >> numVillages >> numEdges;
	for (int i = 0; i < numEdges; ++i)
	{
		inFile >> p1 >> p2 >> c >> t;
		lines.push_back(Line(p1, p2, c, t));
	}
}