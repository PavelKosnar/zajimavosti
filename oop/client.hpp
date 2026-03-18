#include <iostream>
#include "address.hpp"
#include "creditCard.hpp"

using namespace std;

class Client {
    private:
        static int objectsCount;
        int code;
        string name;
        Address* address;
        Address** mailingAddresses;
        int mailingAddressesCount;
        CreditCard* creditCard;

    public:
        static int GetObjectsCount();
        Client(int c, string n);
        ~Client();
        int GetCode();
        string GetName();
        Address* CreateAddress(string s, string z, string city, string c, string p);
        Address* CreateMailingAddress(string s, string z, string city, string c, string p);
        CreditCard* CreateCreditCard(int num, string n, Client* c, string e, int s, int b);
};