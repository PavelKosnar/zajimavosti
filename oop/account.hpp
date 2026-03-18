#include <iostream>
#include "client.hpp"

using namespace std;

class Account {
    private:
        Client* client;
        Client* partner;
        int id;
        int balance;
        CreditCard** creditCards;
        int creditCardsCount;

    public:
        Account(Client* c, int id);
        ~Account();
        int GetID();
        int GetBalance();
        void AddMoney(int m);
        bool SendMoney(Account* a, int m);
        Client* CreatePartner(Client* c);
        CreditCard* CreateCreditCard(int num, string n, Client* c, string e, int s, int b);
};