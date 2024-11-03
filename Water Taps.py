import java.util.Scanner;

public class WaterTaps {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
       
        int A = sc.nextInt();
        int B = sc.nextInt();
      
        int timeToFill = (A * B) / (A + B);
        
        
        System.out.println(timeToFill);
    }
}
