import java.util.Scanner;

public class TwoSum {
    public static int[] twoSum(int[] numbers, int target){
        int i = 0, j = numbers.length - 1;

        while (i < j){
            int sum = numbers[i] + numbers[j];

            if (sum == target){
                return new int[]{i, j};
            } else if (sum < target){
                i++;
            }else{
                j--;
            }
        }
        return new int[]{-1, -1};    // safety
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of element: ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter sorted array elements: ");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        System.out.println("Enter target: ");
        int target = sc.nextInt();

        int[] result = twoSum(arr, target);

        System.out.println("Indices: " + result[0] + " " + result[1]);

        sc.close();
    }
}