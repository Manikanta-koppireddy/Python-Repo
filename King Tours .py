import java.util.Scanner;

public class KingTours {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); 
        int M = sc.nextInt();
        
        int maxPeople = (N * 5) + (M * 7);
        
        System.out.println(maxPeople);
    }
}
