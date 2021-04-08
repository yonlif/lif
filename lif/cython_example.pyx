# distutils: language=c++

cdef extern from "cpp_code/cppmult.hpp":
    float cppmult_f(int int_param, float float_param)

def pymult( int_param, float_param ):
    return cppmult_f( int_param, float_param )
