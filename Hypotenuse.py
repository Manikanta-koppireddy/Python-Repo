import java.util.Scanner;

public class Hypotenuse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int Y = sc.nextInt();
        
        double hypotenuse = Math.sqrt(X * X + Y * Y);
        
        System.out.printf("%.2f\n", hypotenuse);
    }
}
