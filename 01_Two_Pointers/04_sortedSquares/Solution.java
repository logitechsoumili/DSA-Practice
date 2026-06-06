import java.util.Scanner;

class Solution {
    public int[] sortedSquares(int[] arr) {
        int n = arr.length;
        int[] res = new int[n];

        int i = 0, j = n - 1, k = n - 1;

        while (i <= j){
            int left = arr[i] * arr[i];
            int right = arr[j] * arr[j];

            if (left >= right){
                res[k] = left;
                i++;
            }else{
                res[k] = right;
                j--;
            }
            k--;
        }

        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of array: ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter elements (sorted): ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Solution obj = new Solution();
        int[] result = obj.sortedSquares(arr);

        System.out.println("Sorted Squares:");
        for (int num : result) {
            System.out.print(num + " ");
        }

        sc.close();
    }
}