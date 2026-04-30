#include <iostream>
#include <time.h>

using namespace std;

void bubble_sort(int* arr, int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - i - 1; j++) {
			int temp = arr[j];
			if (temp > arr[j + 1]) {
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

void selection_sort(int* arr, int n) {
	for (int i = 0; i < n - 1; i++) {
		int min_idx = i;
		for (int j = i + 1; j < n; j++) {
			if (arr[j] < arr[min_idx])
				min_idx = j;
		}
		int tmp = arr[min_idx];
		arr[min_idx] = arr[i];
		arr[i] = tmp;
	}
}

void insertion_sort(int* arr, int n) {
	for (int i = 1; i < n; i++) {
		int out = arr[i];
		int j = i - 1;
		while (j >= 0 && arr[j] > out) {
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = out;
	}
}

bool binary_search(int* arr, int n, int value) {
	int left = 0;
	int right = n - 1;

	while (right >= left) {
		int mid = (left + right) / 2;
		if (value == arr[mid])
			return true;
		if (value < arr[mid])
			right = mid - 1;
		if (value > arr[mid])
			left = mid + 1;
	}
	return false;
}

int partition(int* arr, int left, int right) {
	int pivot = arr[right];
	int last = left;
	
	for (int i = left; i < right; i++) {
		if (arr[i] < pivot) {
			swap(arr[i], arr[last]);
			last++;
		}
	}

	swap(arr[right], arr[last]);
	return last;
}

void quick_sort(int* arr, int left, int right) {
	if (right <= left)
		return;

	int pivot_index = partition(arr, left, right);

	quick_sort(arr, left, pivot_index - 1);
	quick_sort(arr, pivot_index + 1, right);
}

bool is_sorted_asc(int* arr, int n) {
	for (int i = 0; i < n - 1; i++) {
		if (arr[i] > arr[i + 1])
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
	int larger_num = 20000000; // 20m
	int* arr = new int[num];
	int* arr2 = new int[num];
	int* arr3 = new int[num];
	int* larger_arr = new int[larger_num];

	for (int i = 0; i < num; i++) {
		arr[i] = rand();
		arr2[i] = rand();
		arr3[i] = rand();
	}

	for (int i = 0; i < larger_num; i++) {
		larger_arr[i] = rand();
	}

	time_t start_time = time(nullptr);
	bubble_sort(arr, num);
	time_t end_time = time(nullptr);

	time_t start_time2 = time(nullptr);
	selection_sort(arr2, num);
	time_t end_time2 = time(nullptr);

	time_t start_time3 = time(nullptr);
	insertion_sort(arr3, num);
	time_t end_time3 = time(nullptr);

	time_t start_time4 = time(nullptr);
	quick_sort(larger_arr, 0, larger_num - 1);
	time_t end_time4 = time(nullptr);

	time_t start_time_search = time(nullptr);
	bool found = binary_search(larger_arr, larger_num, 67);
	time_t end_time_search = time(nullptr);

	cout << "ARRAY 1:" << endl;
	cout << "Is sorted? " << ((is_sorted_asc(arr, num) == true) ? "Yes" : "No") << endl;
	cout << "Bubble sort time for size of " << num << ": " << end_time - start_time << " seconds" << endl;

	cout << "\nARRAY 2:" << endl;
	cout << "Is sorted? " << ((is_sorted_asc(arr2, num) == true) ? "Yes" : "No") << endl;
	cout << "Selection sort time for size of " << num << ": " << end_time2 - start_time2 << " seconds" << endl;

	cout << "\nARRAY 3:" << endl;
	cout << "Is sorted? " << ((is_sorted_asc(arr3, num) == true) ? "Yes" : "No") << endl;
	cout << "Insertion sort time for size of " << num << ": " << end_time3 - start_time3 << " seconds" << endl;

	cout << "\nARRAY 4:" << endl;
	cout << "Is sorted? " << ((is_sorted_asc(larger_arr, larger_num) == true) ? "Yes" : "No") << endl;
	cout << "Quick sort time for size of " << larger_num << ": " << end_time4 - start_time4 << " seconds" << endl;

	cout << "\nBINARY SEARCH:" << endl;
	cout << "Number was " << (found == true ? "" : "NOT ") << "found" << endl;
	cout << "Binary search time for size of " << larger_num << ": " << end_time_search - start_time_search << " seconds" << endl;

	int fact = 5;
	cout << "\n\nFactorial " << fact << " = " << factorial(fact) << endl;
	
	return 0;
}
