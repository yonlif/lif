#include "trial_division_algorithm.hpp"


std::vector<bigint> trial_division(bigint n)
{
    std::vector<bigint> v; bigint f;
    f = 2;
    while (n % 2 == 0) { v.push_back(f); n /= 2; }
    f = 3;
    while (n % 3 == 0) { v.push_back(f); n /= 3; }
    f = 5;
    bigint ac = 9, temp = 16;
    do {
        ac += temp; // Assume addition does not cause overflow with U type
        if (ac > n) break;
        if (n % f == 0) {
            v.push_back(f);
            n /= f;
            ac -= temp;
        }
        else {
            f += 2;
            temp += 8;
        }
    } while (1);
    if (n != 1) v.push_back(n);
    return v;
}
