import java.util.Scanner;

public class ProfitPercentage {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cp = sc.nextInt();
        int sp = sc.nextInt();
        double profitPercentage = ((double)(sp - cp) / cp) * 100;
        System.out.printf("%.2f\n", profitPercentage);
    }
}
