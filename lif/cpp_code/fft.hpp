#ifndef _FFT_FUNCTIONS
#define _FFT_FUNCTIONS

// https://github.com/indy256/codelibrary/tree/master/cpp/numeric

#include <vector>
#include <complex>

using namespace std;

using cpx = complex<double>;

void ensure_capacity(int min_capacity);
void fft(vector<cpx> &z, bool inverse);
vector<int> multiply_bigint(const vector<int> &a, const vector<int> &b, int base);
vector<int> multiply_mod(const vector<int> &a, const vector<int> &b, int m);

#endif
