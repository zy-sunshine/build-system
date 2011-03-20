// pair.h.  A pair like the STL
 namespace std {
    template<class T1, class T2> struct pair {
        T1 first;
        T2 second;
        pair() : first(T1()), second(T2()) { };
        pair(const T1 &f, const T2 &s) : first(f), second(s) { }
    };
 }
