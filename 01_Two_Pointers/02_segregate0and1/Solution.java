import java.util.Scanner;

class Solution {
    void segregate0and1(int[] arr) {
        int k = 0;
        for (int i = 0; i < arr.length; i++){
            if (arr[i] == 0){
                int temp = arr[k];
                arr[k++] = arr[i];
                arr[i] = temp;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter array: ");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        Solution obj = new Solution();
        obj.segregate0and1(arr);

        System.out.println("Segregated array: ");
        for (int x : arr) {
            System.out.print(x + " ");
        }

        sc.close();
    }
}