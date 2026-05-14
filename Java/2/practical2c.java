import java.io.File;
import java.util.Date;

public class practical2c {
    public static void main(String[] args) {

        // Specify file path
        File file = new File("D:\\JavaPrograms\\Program1.java");

        // Check file existence
        if (file.exists()) {

            // Get last modified time
            long milliseconds = file.lastModified();

            // Convert to Date object
            Date date = new Date(milliseconds);

            // Display result
            System.out.println("Last Modified Date: " + date);

        } else {
            System.out.println("File does not exist.");
        }
    }
}