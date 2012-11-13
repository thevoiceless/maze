CPPS = maze.cpp

all:
	g++ $(CPPS) -o maze

clean:
	rm maze