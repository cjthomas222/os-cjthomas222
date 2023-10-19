#include <iostream>
#include <thread>
#include <mutex>
#include <vector>


using namespace std;
mutex car_wash_mutex;

void car_wash(int car_id) {
    lock_guard<mutex> lock(car_wash_mutex);
    cout << "Car " << car_id << " is being washed.\n";
    this_thread::sleep_for(chrono::seconds(2));
    cout << "Car " << car_id << " is done washing.\n";
}

int main() {
    const int num_cars = 5;
    vector<thread> car_threads;

    for (int i = 1; i <= num_cars; ++i) {
        car_threads.emplace_back(car_wash, i);
    }

    for (auto& t : car_threads) {
        t.join();
    }

    return 0;
}