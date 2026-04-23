#include <iostream>
#include <time.h>

using namespace std;

void bubble_sort(int* pole, int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - i - 1; j++) {
			int temp = pole[j];
			if (temp > pole[j + 1]) {
				pole[j] = pole[j + 1];
				pole[j + 1] = temp;
			}
		}
	}
}

void selection_sort(int* pole, int n) {
	for (int i = 0; i < n - 1; i++) {
		int min_idx = i;
		for (int j = i + 1; j < n; j++) {
			if (pole[j] < pole[min_idx])
				min_idx = j;
		}
		int tmp = pole[min_idx];
		pole[min_idx] = pole[i];
		pole[i] = tmp;
	}
}

void insertion_sort(int* pole, int n) {
	for (int i = 1; i < n; i++) {
		int out = pole[i];
		int j = i - 1;
		while (j >= 0 && pole[j] > out) {
			pole[j + 1] = pole[j];
			j--;
		}
		pole[j + 1] = out;
	}
}

bool is_sorted_asc(int* pole, int n) {
	for (int i = 0; i < n - 1; i++) {
		if (pole[i] > pole[i + 1])
			return false;
	}
	return true;
}

long long int factorial(int n) {
	if (n == 0)
		return 1;
	return n * factorial(n - 1);
}

int main() {
	srand(time(nullptr));
	int num = 100000;
	int* pole = new int[num];
	int* pole2 = new int[num];
	int* pole3 = new int[num];

	for (int i = 0; i < num; i++) {
		pole[i] = rand();
		pole2[i] = rand();
		pole3[i] = rand();
	}

	time_t start_time = time(nullptr);
	bubble_sort(pole, num);
	time_t end_time = time(nullptr);

	time_t start_time2 = time(nullptr);
	selection_sort(pole2, num);
	time_t end_time2 = time(nullptr);

	time_t start_time3 = time(nullptr);
	insertion_sort(pole3, num);
	time_t end_time3 = time(nullptr);

	cout << "POLE 1:" << endl;
	cout << "Is sorted? " << ((is_sorted_asc(pole, num) == true) ? "Yes" : "No") << endl;
	cout << "Bubble sort time for size of " << num << ": " << end_time - start_time << " seconds" << endl;

	cout << "\nPOLE 2:" << endl;
	cout << "Is sorted? " << ((is_sorted_asc(pole2, num) == true) ? "Yes" : "No") << endl;
	cout << "Selection sort time for size of " << num << ": " << end_time2 - start_time2 << " seconds" << endl;

	cout << "\nPOLE 3:" << endl;
	cout << "Is sorted? " << ((is_sorted_asc(pole3, num) == true) ? "Yes" : "No") << endl;
	cout << "Insertion sort time for size of " << num << ": " << end_time3 - start_time3 << " seconds" << endl;

	int fact = 5;
	cout << "\n\nFactorial " << fact << " = " << factorial(fact) << endl;

	return 0;
}
