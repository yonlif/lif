#include "algorithms_interface.hpp"

std::vector<std::string> cast_bigint_vector_to_string_vector(std::vector<bigint> bigint_vector) {
    std::vector<std::string> return_string_vector;
    std::stringstream tmp_stream;
    for(auto itr : bigint_vector) {
        tmp_stream << itr;
        return_string_vector.push_back(tmp_stream.str());
        tmp_stream.str("");
    }
    return return_string_vector;
}


std::vector<std::string> cpp_trial_division(char * n) {
    bigint bigint_input = bigint(n);
    std::vector<bigint> bigint_vector = trial_division(bigint_input);
    return cast_bigint_vector_to_string_vector(bigint_vector);
}
