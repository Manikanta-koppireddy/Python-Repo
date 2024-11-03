import java.util.Scanner;

public class LastTwoDigits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt(); 
        
        int lastTwoDigits = year % 100;
        
        System.out.printf("%02d\n", lastTwoDigits);
    }
}
