
import java.io.File;

public class practical2a {
    public static void main(String[] args) {

        // Specify directory path
        File directory = new File("D:\\JavaPrograms");

        // Check if directory exists
        if (directory.exists() && directory.isDirectory()) {

            // Get list of files/directories
            String[] files = directory.list();

            System.out.println("Files and Directories:");

            // Display names
            for (String file : files) {
                System.out.println(file);
            }

        } else {
            System.out.println("Directory does not exist.");
        }
    }
} 