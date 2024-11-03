import java.util.Scanner;

public class DiskCapacity {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(), S = sc.nextInt(), B = sc.nextInt();
        System.out.println(2 * T * S * B * 512 / 1024 + " KB");
    }
}
