interface NumberCheck {
    void checkNumber(int num);
}

public class practical3a {
    public static void main(String[] args) {

        // Lambda expression
        NumberCheck result = (num) -> {

            if (num > 0) {
                System.out.println(num + " is Positive");
            } else if (num < 0) {
                System.out.println(num + " is Negative");
            } else {
                System.out.println("Number is Zero");
            }
        };

        // Calling lambda method
        result.checkNumber(15);
        result.checkNumber(-8);
        result.checkNumber(0);
    }
}