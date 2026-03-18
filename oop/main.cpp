#include <iostream>
#include "bank.hpp"
#include "client.hpp"

using namespace std;

int main() {
    Bank* bank = new Bank("International Bank");

    for (int i = 0; i < 10; i++) {
        string name = "Client-" + i;
        cout << name << endl;
    }
    /*
    Client* cl1 = bank->CreateClient("Client");
    Account* acc1 = new Account(cl1, 1, 0);

    cout << "Client: " << cl1->GetName() << ", code: " << cl1->GetCode() << endl;
    cout << "Balance: " << acc1->GetBalance() << endl;

    Client* cl2 = new Client(2, "Karel");
    Account* acc2 = new Account(cl2, 2, 0);

    cout << "Client: " << cl2->GetName() << ", code: " << cl2->GetCode() << endl;
    cout << "Balance: " << acc2->GetBalance() << endl;

    acc1->AddMoney(2000);
    cout << "Acc1 balance: " << acc1->GetBalance() << endl;

    acc1->SendMoney(acc2, 500);
    cout << "Balances after exchange:" << endl;
    cout << "Acc1: " << acc1->GetBalance() << ", acc2: " << acc2->GetBalance() << endl;*/

    delete bank;

    return 0;
}