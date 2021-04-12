#ifndef _POLLARDS_RHO_ALGORITHM
#define _POLLARDS_RHO_ALGORITHM
// https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm

#include <vector>
#include <stdio.h>
#include "../bigint/bigint.cpp"

bigint pollards_rho(bigint n);

#endif
