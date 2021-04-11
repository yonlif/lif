# distutils: language=c++

cdef extern from "<vector>" namespace "std":
    cdef cppclass vector[T]:
        cppclass iterator:
            T operator*()
            iterator operator++()
            bint operator==(iterator)
            bint operator!=(iterator)
        vector()
        void push_back(T&)
        int size()
        T& operator[](int)
        T& at(int)
        iterator begin()
        iterator end()
