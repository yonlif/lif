#include <stdio.h>

float cppmult_f(int int_param, float float_param) {
    float return_value = int_param * float_param;
    printf("    In cppmult : int: %d float %.1f returning  %.1f\n", int_param,
            float_param, return_value);
    return return_value;
}