#include "pollards_rho_algorithm.hpp"

bigint pollards_rho(bigint n)
{
    bigint loop = 1, count;
    bigint x_fixed = 2, x = 2, size = 2, factor;
    do {
        count = size;
        do {
            x = (x * x + 1) % n;
            factor = gcd((x - x_fixed).abs(), n);
            count -= 1;
        } while ((count != 0) && (factor == 1));
        size *= 2;
        x_fixed = x;
        loop = loop + 1;
    } while (factor == 1);
    return factor;
}
