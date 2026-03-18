#include <iostream>
#include "address.hpp"

using namespace std;

Address::Address(string s, string z, string city, string c, string p) {
    this->street = s;
    this->zip = z;
    this->city = city;
    this->country = c;
    this->post = p;
}

Address::~Address() {
    
}

string Address::GetStreet() {
    return this->street;
}

string Address::GetZip() {
    return this->zip;
}

string Address::GetCity() {
    return this->city;
}

string Address::GetCountry() {
    return this->country;
}

string Address::GetPost() {
    return this->post;
}