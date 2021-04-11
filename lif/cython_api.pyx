# distutils: language=c++

from lif cimport cpp_vector
from libcpp.string cimport string
from typing import List


cdef extern from "cpp_code/algorithms_interface.hpp":
    cpp_vector.vector[string] cpp_trial_division(char * n)

def trial_division(number: int) -> List[int]:
    string_param_utf8 = str(number).encode('utf-8')
    cdef cpp_vector.vector[string] v = cpp_trial_division(string_param_utf8)
    ret_list = []
    for i in range(v.size()):
        ret_list.append(int(v.at(i).decode("utf-8")))
    return ret_list
