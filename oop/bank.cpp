#include <iostream>
#include "bank.hpp"

using namespace std;

Bank::Bank(string n) {
    this->name = n;
    this->accounts = nullptr;
    this->accountsCount = 0;
    this->clients = nullptr;
    this->clientsCount = 0;
}

Bank::~Bank() {
    this->accounts = nullptr;
    this->clients = nullptr;
}

string Bank::GetName() {
    return this->name;
}

int Bank::GetAccountsCount() {
    return this->accountsCount;
}

int Bank::GetClientsCount() {
    return this->clientsCount;
}

Client* Bank::CreateClient(string name) {
    Client* newClient = new Client(this->clientsCount, name);
    this->clients[this->clientsCount++] = newClient;
    return newClient;
}

Account* Bank::CreateAccount(Client* client) {
    Account* newAcc = new Account(client, accountsCount);
    this->accounts[this->accountsCount++] = newAcc;
    return newAcc;
}