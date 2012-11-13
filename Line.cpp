#include "Line.h"

bool Line::alreadyVisitedDirection(char start, char end)
{
	// Direction 1 = From point1 to point2
	if (start == point1 && end == point2)
	{
		if (visitedDir1)
		{
			return true;
		}
		visitedDir1 = true;
		return false;
	}
	// Direction 2 = From point2 to point1
	else if (start == point2 && end == point1)
	{
		if (visitedDir2)
		{
			return true;
		}
		visitedDir2 = true;
		return false;
	}
	else
	{
		cout << "Error in graph representation." << endl;
		exit(1);
	}
}