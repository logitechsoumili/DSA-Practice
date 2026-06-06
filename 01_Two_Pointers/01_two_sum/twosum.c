#include <stdio.h>

void search(int arr[], int n, int X){
	int i = 0, j = n - 1;
	while (i < j){
		int res = arr[i] + arr[j];
		if (res == X){
			printf("%d %d", arr[i], arr[j]);
			return;
		} else if (res < X)
			i++;
		else
			j--;
	}
	printf("No pair found");
}

int main(){
	int n, target;
	printf("Enter size of array: ");
	scanf("%d", &n);
	int arr[n];

	printf("Enter sorted array: ");
	for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

	printf("Enter target: ");
	scanf("%d", &target);

	search(arr, n, target);

	return 0;
}