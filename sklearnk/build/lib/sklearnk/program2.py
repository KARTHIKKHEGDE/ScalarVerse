#include <iostream>
using namespace std;

int main() {
    int bucketSize, outputRate, bucket = 0;

    cout << "Enter output rate: ";
    cin >> outputRate;

    cout << "Enter bucket size: ";
    cin >> bucketSize;

    while (true) {
        int incoming;
        cout << "\nEnter incoming packet (0 to stop): ";
        cin >> incoming;

        if (incoming == 0) break; // exit condition

        // Overflow check
        if (bucket + incoming > bucketSize) {
            cout << "Overflow! Dropped: " << (bucket + incoming - bucketSize) << endl;
            incoming = bucketSize - bucket;
        }

        bucket += incoming;
        cout << "Buffer now: " << bucket << endl;

        int timeGap;
        cout << "Enter time until next packet: ";
        cin >> timeGap;

        while (timeGap > 0) {
            if (bucket > 0) {
                int sent = min(bucket, outputRate);
                bucket -= sent;

                cout << "Transmitted: " << sent << endl;
                cout << "Remaining: " << bucket << endl;
            } else {
                cout << "No packets to transmit" << endl;
            }
            timeGap--;
        }
    }

    return 0;
}