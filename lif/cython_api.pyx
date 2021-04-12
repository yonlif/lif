# distutils: language=c++

from lif cimport cpp_vector
from libcpp.string cimport string
from typing import List

### External decelerations

cdef extern from "cpp_code/algorithms_interface.hpp":
    cpp_vector.vector[string] cpp_trial_division(char * n)

cdef extern from "cpp_code/algorithms_interface.hpp":
    string cpp_pollards_rho(char * n)


### Python decelerations

def trial_division(number: int) -> List[int]:
    string_param_utf8 = str(number).encode('utf-8')
    cdef cpp_vector.vector[string] v = cpp_trial_division(string_param_utf8)
    return parse_string_vector(v)


def pollards_rho(number: int) -> int:
    string_param_utf8 = str(number).encode('utf-8')
    cdef string str_result = cpp_pollards_rho(string_param_utf8)
    return int(str_result.decode("utf-8"))


# Helper functions

def parse_string_vector(v: cpp_vector.vector[string]) -> List[int]:
    ret_list = []
    for i in range(v.size()):
        ret_list.append(int(v.at(i).decode("utf-8")))
    return ret_list
