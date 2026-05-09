#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string vigenere(string text, string key, bool encrypt) {
    string result = "";
    int j = 0;

    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        if (!isalpha(ch)) {
            result += ch;
            continue;
        }

        char base;
        if (isupper(ch))
            base = 'A';
        else
            base = 'a';

        int shift = toupper(key[j % key.length()]) - 'A';

        if (!encrypt)
            shift = 26 - shift;

        result += (ch - base + shift) % 26 + base;
        j++;
    }

    return result;
}

int main() {
    int mode;
    string text, key;

    cout << "Enter text: ";
    getline(cin, text);

    cout << "Enter key: ";
    getline(cin, key);

    cout << "1 = Encrypt, 2 = Decrypt: ";
    cin >> mode;

    string output = vigenere(text, key, mode == 1);

    cout << "Result: " << output << endl;

    return 0;
}