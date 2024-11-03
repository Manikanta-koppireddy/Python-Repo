import java.util.Scanner;

public class AverageWeight {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int avg = sc.nextInt(), W1 = sc.nextInt(), W2 = sc.nextInt();
        System.out.println(3 * avg - W1 - W2);
    }
}
