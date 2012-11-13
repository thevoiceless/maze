#pragma once

class Line
{
private:
	int color;
	int type;
	char point1, point2;

public:
	static const char COLOR_RED = 'R';
	static const char COLOR_GREEN = 'G';
	static const char COLOR_BLUE = 'B';
	static const char TYPE_HORSE = 'H';
	static const char TYPE_CAR = 'C';
	static const char TYPE_TROLLEY = 'T';
	static const char TYPE_BUS = 'B';

	Line(char _point1, char _point2, int _color, int _type) : point1(_point1), point2(_point2), color(_color), type(_type) {}
};