#include <iostream>
#include <string>
#include <cctype>
using namespace std;

// ---------- CAESAR CIPHER ----------
string caesar(string text, int shift, bool encrypt) {
    string result = "";

    if (!encrypt) shift = 26 - shift;

    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        if (isalpha(ch)) {
            char base;

            if (islower(ch)) base = 'a';
            else base = 'A';

            result += (ch - base + shift) % 26 + base;
        } else {
            result += ch;
        }
    }

    return result;
}

// ---------- PLAYFAIR CIPHER ----------
char matrix[5][5];

// Generate matrix
void generateMatrix(string key) {
    bool used[26] = {false};
    used['J' - 'A'] = true;

    string temp = "";

    for (int i = 0; i < key.length(); i++) {
        char ch = toupper(key[i]);
        if (ch == 'J') ch = 'I';

        if (!used[ch - 'A']) {
            temp += ch;
            used[ch - 'A'] = true;
        }
    }

    for (char ch = 'A'; ch <= 'Z'; ch++) {
        if (!used[ch - 'A']) {
            temp += ch;
        }
    }

    int k = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            matrix[i][j] = temp[k++];
        }
    }
}

// Find position
void findPos(char ch, int &row, int &col) {
    if (ch == 'J') ch = 'I';

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (matrix[i][j] == ch) {
                row = i;
                col = j;
            }
        }
    }
}

// Playfair encryption/decryption
string playfair(string text, bool encrypt) {
    string result = "";

    for (int i = 0; i < text.length(); i += 2) {
        char a = toupper(text[i]);
        char b = (i + 1 < text.length()) ? toupper(text[i + 1]) : 'X';

        int r1, c1, r2, c2;
        findPos(a, r1, c1);
        findPos(b, r2, c2);

        if (r1 == r2) {
            if (encrypt) {
                result += matrix[r1][(c1 + 1) % 5];
                result += matrix[r2][(c2 + 1) % 5];
            } else {
                result += matrix[r1][(c1 + 4) % 5];
                result += matrix[r2][(c2 + 4) % 5];
            }
        }
        else if (c1 == c2) {
            if (encrypt) {
                result += matrix[(r1 + 1) % 5][c1];
                result += matrix[(r2 + 1) % 5][c2];
            } else {
                result += matrix[(r1 + 4) % 5][c1];
                result += matrix[(r2 + 4) % 5][c2];
            }
        }
        else {
            result += matrix[r1][c2];
            result += matrix[r2][c1];
        }
    }

    return result;
}

// ---------- MAIN ----------
int main() {
    int choice, mode;
    string text, key;

    cout << "1. Caesar  2. Playfair\nChoice: ";
    cin >> choice;
    cin.ignore();

    cout << "Enter text: ";
    getline(cin, text);

    cout << "1. Encrypt  2. Decrypt: ";
    cin >> mode;
    cin.ignore();

    if (choice == 1) {
        int shift;
        cout << "Enter shift: ";
        cin >> shift;

        cout << "Result: " << caesar(text, shift, mode == 1);
    }
    else {
        cout << "Enter key: ";
        getline(cin, key);

        generateMatrix(key);

        cout << "Result: " << playfair(text, mode == 1);
    }
}