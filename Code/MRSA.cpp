#include<bits/stdc++.h>
using namespace std;



int gcd(int a, int b)
{
    int temp;
    while (1) {
        temp = a % b;
        if (temp == 0)
            return b;
        a = b;
        b = temp;
    }
}

int inverse(int a, int m) {
    int m0 = m, t, q, x0 = 0, x1 = 1;
 
    while (a > 1) {
        q = a / m;
        t = m, m = a % m, a = t;
        t = x0, x0 = x1 - q * x0, x1 = t;
    }
 
    if (x1 < 0) x1 += m0;
 
    return x1;
}

int modPow(int base, int exponent, int modulus) {
    int result = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1)
            result = (result * base) % modulus;
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

int main()
{
    int p, q, r;
    cout<<"Enter p: ";
    cin>>p;

    cout<<"Enter q: ";
    cin>>q;

    cout<<"Enter r: ";
    cin>>r;

    int n=p*q*r;
    int fi=(p-1)*(q-1)*(r-1);
    
    int e = 2;
    // cout<<"Enter e: ";
    // cin>>e;

    while (e < fi) 
    {
        if (gcd(e, fi) == 1)
            break;
        else
            e++;
    }

    int ec = e;
    
    int d = inverse(e, fi);

    cout<<"Enter the Plain Text: ";
    int m;
    cin>>m;
 
    int c = modPow(m, e, n);
    cout<<"\nCipher Text is: "<<c<<endl;
 
    m = modPow(c, d, n);
    cout<<"\nOriginal Text is: "<<m<<endl;

    return 0;
}
