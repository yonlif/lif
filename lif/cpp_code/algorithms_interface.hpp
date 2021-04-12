#ifndef _ALGORITHMS_INTERFACE
#define _ALGORITHMS_INTERFACE

#include <stdio.h>
#include <vector>
#include "algorithms/trial_division_algorithm.hpp"
#include "algorithms/pollards_rho_algorithm.hpp"

std::vector<std::string> cpp_trial_division(char * n);
std::string cpp_pollards_rho(char * n);

#endif
