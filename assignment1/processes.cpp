#include <iostream>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <sys/wait.h>

using namespace std;

int main() {
    pid_t pid;


    for (int i = 0; i < 9; ++i) { 
        pid = fork();

        if (pid < 0) {
            cerr << "Fork failed!" << endl;
            return 1;
        }

        if (pid == 0) { 
            cout << "Child process: PID = " << getpid() << ", Parent PID = " << getppid() << endl;
            exit(0); 
        }
    }

    cout << "Parent process: PID = " << getpid() << endl;

    for (int i = 0; i < 9; ++i) {
        wait(NULL);
    }

    return 0;
}