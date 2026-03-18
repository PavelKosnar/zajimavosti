#include <iostream>
#include "account.hpp"
#include "client.hpp"

using namespace std;

class Bank {
    private:
        string name;
        Account** accounts;
        int accountsCount;
        Client** clients;
        int clientsCount;

    public:
        Bank(string n);
        ~Bank();
        string GetName();
        int GetAccountsCount();
        int GetClientsCount();
        Client* CreateClient(string name);
        Account* CreateAccount(Client* client);
};