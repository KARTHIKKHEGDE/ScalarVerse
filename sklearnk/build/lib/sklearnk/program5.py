#include <iostream>
#include <string>
#include <vector>
using namespace std;

using ll = long long;

// Modular exponentiation
ll mod_pow(ll base, ll exp, ll mod) {
    ll result = 1;
    base %= mod;

    while (exp > 0) {
        if (exp & 1)
            result = result * base % mod;

        base = base * base % mod;
        exp >>= 1;
    }

    return result;
}

// GCD
ll gcd(ll a, ll b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

// Modular inverse (Extended Euclidean)
ll mod_inverse(ll e, ll phi) {
    ll t = 0, new_t = 1;
    ll r = phi, new_r = e;

    while (new_r != 0) {
        ll q = r / new_r;

        ll temp = new_t;
        new_t = t - q * new_t;
        t = temp;

        temp = new_r;
        new_r = r - q * new_r;
        r = temp;
    }

    if (t < 0)
        t += phi;

    return t;
}

// Prime check
bool is_prime(ll n) {
    if (n < 2)
        return false;

    for (ll i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }

    return true;
}

int main() {
    ll p, q;

    cout << "Enter prime p: ";
    cin >> p;

    cout << "Enter prime q: ";
    cin >> q;

    if (!is_prime(p) || !is_prime(q)) {
        cout << "Both must be prime!\n";
        return 1;
    }

    ll n = p * q;
    ll phi = (p - 1) * (q - 1);

    ll e;
    cout << "Enter public exponent e (coprime to " << phi << "): ";
    cin >> e;

    if (gcd(e, phi) != 1) {
        cout << "e must be coprime to phi!\n";
        return 1;
    }

    ll d = mod_inverse(e, phi);

    cout << "\n";
    cout << "Public key:  (e = " << e << ", n = " << n << ")\n";
    cout << "Private key: (d = " << d << ", n = " << n << ")\n\n";

    int mode;
    cout << "1 = Encrypt  2 = Decrypt: ";
    cin >> mode;
    cin.ignore();

    if (mode == 1) {
        string text;

        cout << "Enter plaintext: ";
        getline(cin, text);

        cout << "Encrypted: ";
        for (int i = 0; i < text.length(); i++) {
            cout << mod_pow(text[i], e, n) << " ";
        }
        cout << "\n";
    }
    else {
        string line;

        cout << "Enter ciphertext (space-separated): ";
        getline(cin, line);

        cout << "Decrypted: ";

        std::size_t pos = 0;
        while (pos < line.length()) {
            std::size_t next = line.find(' ', pos);
            if (next == string::npos)
                next = line.length();

            ll value = stoll(line.substr(pos, next - pos));
            char ch = char(mod_pow(value, d, n));

            cout << ch;
            pos = next + 1;
        }

        cout << "\n";
    }

    return 0;
}