 // pair.i - SWIG interface
 %module pair
 %{
 #include "pair.h"
 %}
 
 // Ignore the default constructor
 %ignore std::pair::pair();      
 
 // Parse the original header file
 %include "pair.h"
 
 // Instantiate some templates
 
 %template(pairii) std::pair<int,int>;
 %template(pairdi) std::pair<double,int>;
