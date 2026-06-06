import java.util.Scanner;

class Solution{
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 0) return 0;
        int k = 1;
        for (int i = 1; i < nums.length; i++){
            if (nums[i] != nums[i-1]){
                nums[k++] = nums[i];
            }
        }
        return k;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        System.out.println("Enter sorted array: ");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        Solution obj = new Solution();

        System.out.println("Number of unique elements: " + obj.removeDuplicates(arr));

        sc.close();
    }
}