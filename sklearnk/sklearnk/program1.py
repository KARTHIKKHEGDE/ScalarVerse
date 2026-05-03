#include <iostream>
#include <string>
using namespace std;

string xorOp(string a, string b) {
    string res = "";

    for (int i = 1; i < b.length(); i++) {
        res += (a[i] == b[i]) ? '0' : '1';
    }

    return res;
}

string crc(string data, string divisor) {
    int n = divisor.length();
    string temp = data.substr(0, n);

    for (int i = n; i < data.length(); i++) {

        if (temp[0] == '1') {
            temp = xorOp(temp, divisor) + data[i];
        } else {
            temp = xorOp(temp, string(n, '0')) + data[i];
        }
    }

    if (temp[0] == '1') {
        temp = xorOp(temp, divisor);
    } else {
        temp = xorOp(temp, string(n, '0'));
    }

    return temp;
}


int main() {
    string data, divisor;

    cout << "Enter data: ";
    cin >> data;

    cout << "Enter divisor: ";
    cin >> divisor;

    string padded = data + string(divisor.length() - 1, '0');
    string remainder = crc(padded, divisor);
    string codeword = data + remainder;

    cout << "Codeword: " << codeword << endl;

    string check = crc(codeword, divisor);

    if (check.find('1') != string::npos) {
        cout << "Error detected\n";
    } else {
        cout << "No error\n";
    }

    return 0;
}