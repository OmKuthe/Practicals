interface EvenOdd {
    void check(int num);
}

public class practical3b {
    public static void main(String[] args) {

        // Lambda expression
        EvenOdd result = (num) -> {

            if (num % 2 == 0) {
                System.out.println(num + " is Even");
            } else {
                System.out.println(num + " is Odd");
            }
        };

        // Calling lambda method
        result.check(10);
        result.check(7);
    }
}