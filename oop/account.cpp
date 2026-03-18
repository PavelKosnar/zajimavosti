#include <iostream>
#include "account.hpp"

using namespace std;

Account::Account(Client* c, int id) {
    this->client = c;
    this->partner = nullptr;
    this->id = id;
    this->balance = 0;
}

Account::~Account() {
    this->client = nullptr;
    this->partner = nullptr;
    this->id = -1;
    this->balance = 0;
}

int Account::GetID() {
    return this->id;
}

int Account::GetBalance() {
    return this->balance;
}

void Account::AddMoney(int m) {
    this->balance += m;
}

bool Account::SendMoney(Account* a, int m) {
    if (a == nullptr || this->balance < m) return false;
    this->balance -= m;
    a->AddMoney(m);
    return true;
}

Client* Account::CreatePartner(Client* c) {
    this->partner = c;
    return c;
}

CreditCard* Account::CreateCreditCard(int num, string n, Client* c, string e, int s, int b) {
    CreditCard* newCard = new CreditCard(num, n, c, e, s, b);
    this->creditCard = newCard;
    return newCard;
}