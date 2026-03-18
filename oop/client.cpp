#include <iostream>
#include "client.hpp"

using namespace std;

int Client::objectsCount = 0;

Client::Client(int c, string n) {
    this->code = c;
    this->name = n;
    Client::objectsCount += 1;
    this->address = nullptr;
    this->mailingAddresses = nullptr;
    this->creditCard = nullptr;
}

Client::~Client() {
    Client::objectsCount -= 1;
    this->address = nullptr;
    this->mailingAddresses = nullptr;
    this->mailingAddressesCount = 0;
    this->creditCard = nullptr;
}

int Client::GetObjectsCount() {
    return Client::objectsCount;
}

int Client::GetCode() {
    return this->code;
}

string Client::GetName() {
    return this->name;
}

Address* Client::CreateAddress(string s, string z, string city, string c, string p) {
    Address* newAdd = new Address(s, z, city, c, p);
    this->address = newAdd;
    return newAdd;
}

Address* Client::CreateMailingAddress(string s, string z, string city, string c, string p) {
    Address* newAdd = new Address(s, z, city, c, p);
    this->mailingAddresses[this->mailingAddressesCount++] = newAdd;
    return newAdd;
}

CreditCard* Client::CreateCreditCard(int num, string n, Client* c, string e, int s, int b) {
    CreditCard* newCard = new CreditCard(num, n, c, e, s, b);
    this->creditCard = newCard;
    return newCard;
}