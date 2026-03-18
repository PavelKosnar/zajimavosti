#include <iostream>
#include "creditCard.hpp"

using namespace std;

CreditCard::CreditCard(int num, string n, Client* c, string e, int s, int b) {
    this->num = num;
    this->name = n;
    this->client = c;
    this->endDate = e;
    this->secCode = s;
    this->balance = b;
}

CreditCard::~CreditCard() {
    this->client = nullptr;
}

string CreditCard::GetName() {
    return this->name;
}

int CreditCard::GetBalance() {
    return this->balance;
}