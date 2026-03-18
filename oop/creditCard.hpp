#include <iostream>
#include "client.hpp"

using namespace std;

class CreditCard {
    private:
        int num;
        string name;
        Client* client;
        string endDate;
        int secCode;
        int balance;
    
    public:
        CreditCard(int num, string n, Client* c, string e, int s, int b);
        ~CreditCard();
        string GetName();
        int GetBalance();
};