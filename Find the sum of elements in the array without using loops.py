import java.util.Scanner;

public class ArraySum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        
        if (N < 1 || N > 30) {
            System.out.println("Enter a Valid Number");
            return;
        }
        
        int[] array = new int[N];
        for (int i = 0; i < N; i++) {
            array[i] = scanner.nextInt();
        }
        
        System.out.println(sum(array, N));
    }
    
    static int sum(int[] array, int N) {
        if (N == 0) return 0;
        return array[N - 1] + sum(array, N - 1);
    }
}
