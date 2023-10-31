import multiprocessing

def child_process(shared_buffer):
    for i in range(len(shared_buffer)):
        shared_buffer[i] = i
    print("Child process has written to the shared buffer.")

if __name__ == "__main__":
    shared_buffer = multiprocessing.Array('i', 10)

    p = multiprocessing.Process(target=child_process, args=(shared_buffer,))
    p.start()
    p.join()

    print("Parent process reads from the shared buffer:", list(shared_buffer))
