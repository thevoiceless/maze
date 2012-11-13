#pragma once

class Line
{
private:
	int color;
	int type;

public:
	static const int COLOR_RED = 1;
	static const int COLOR_GREEN = 2;
	static const int COLOR_BLUE = 3;
	static const int TYPE_HORSE = 4;
	static const int TYPE_CAR = 5;
	static const int TYPE_TROLLEY = 6;
	static const int TYPE_BUS = 7;

	Line(int _color, int _type) : color(_color), type(_type) {}
};