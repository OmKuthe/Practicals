import java.sql.*;

public class practical5 {
    public static void main(String[] args) {

        // Database credentials
        String url = "jdbc:mysql://localhost:3306/company";
        String user = "root";
        String password = "root";

        try {
            // Load JDBC Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Establish connection
            Connection con = DriverManager.getConnection(url, user, password);

            System.out.println("Database Connected Successfully!");

            // Create statement
            Statement stmt = con.createStatement();

            // Insert record
            String insertQuery = "INSERT INTO employee VALUES(101, 'Om', 25000)";
            stmt.executeUpdate(insertQuery);

            System.out.println("Record Inserted Successfully!");

            // Fetch records
            String selectQuery = "SELECT * FROM employee";
            ResultSet rs = stmt.executeQuery(selectQuery);

            System.out.println("\nEmployee Records:");

            while (rs.next()) {
                System.out.println(
                        rs.getInt("id") + " " +
                        rs.getString("name") + " " +
                        rs.getDouble("salary"));
            }

            // Close connection
            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}