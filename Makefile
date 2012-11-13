OPT = -O2

CPPS = maze.cpp IOstuff.cpp
OBJS = maze.o IOstuff.o
EXES = maze

all: maze

maze: objects $(OBJS)
	g++ $(CPPS) -o maze $(OPT)

objects: $(CPPS)
	g++ -c $(CPPS) $(OPT)

clean:
	rm $(EXES) $(OBJS)