OPT = -O2

CPPS = maze.cpp IOstuff.cpp Line.cpp
EXES = maze

all: maze

maze: $(CPPS)
	g++ $(CPPS) -o maze $(OPT)

clean:
	rm $(EXES)