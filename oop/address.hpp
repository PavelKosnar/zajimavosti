#include <iostream>

using namespace std;

class Address {
    private:
        string street;
        string zip;
        string city;
        string country;
        string post;
    
    public:
        Address(string s, string z, string city, string c, string p);
        ~Address();
        string GetStreet();
        string GetZip();
        string GetCity();
        string GetCountry();
        string GetPost();
};