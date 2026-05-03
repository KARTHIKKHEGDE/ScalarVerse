#include <iostream>
using namespace std;

using ll = long long;

// Modular exponentiation
ll mod_pow(ll base, ll exp, ll mod)
{
    ll result = 1;
    base %= mod;

    while (exp > 0)
    {
        if (exp & 1)
        {
            result = result * base % mod;
        }

        base = base * base % mod;
        exp >>= 1;
    }

    return result;
}

int main()
{
    ll p, g, a, b;

    cout << "Enter prime (p): ";
    cin >> p;

    cout << "Enter generator (g): ";
    cin >> g;

    cout << "Alice's private key (a): ";
    cin >> a;

    cout << "Bob's private key (b): ";
    cin >> b;

    ll A = mod_pow(g, a, p); // Alice's public value
    ll B = mod_pow(g, b, p); // Bob's public value

    cout << "\nAlice sends: A = g^a mod p = " << A << "\n";
    cout << "Bob sends:   B = g^b mod p = " << B << "\n";

    ll key_alice = mod_pow(B, a, p);
    ll key_bob = mod_pow(A, b, p);

    cout << "\nAlice computes: B^a mod p = " << key_alice << "\n";
    cout << "Bob computes:   A^b mod p = " << key_bob << "\n";

    if (key_alice == key_bob)
    {
        cout << "\nShared secret key: " << key_alice << "\n";
    }
    else
    {
        cout << "\nError: keys do not match!\n";
    }

    return 0;
}