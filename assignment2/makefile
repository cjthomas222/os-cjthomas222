CXX = g++

# Compiler flags
CXXFLAGS = -std=c++11 -pthread -Wall -Wextra

# Source files
SRC = threadedApp.cpp

# Executable name
EXE = threadedApp

# Build rule for the executable
$(EXE): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(EXE)

# Clean rule to remove temporary and output files
clean:
	rm -f $(EXE)

	run:
		./$(EXE)