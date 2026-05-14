import java.io.File;

public class practical2b {
    public static void main(String[] args) {

        // Specify path
        File file = new File("D:\\JavaPrograms\\Program1.java");

        // Check existence
        if (file.exists()) {

            System.out.println("Path exists.");

            // Check whether file or directory
            if (file.isFile()) {
                System.out.println("It is a File.");
            } else if (file.isDirectory()) {
                System.out.println("It is a Directory.");
            }

        } else {
            System.out.println("Path does not exist.");
        }
    }
}