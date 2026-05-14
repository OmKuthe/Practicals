import java.util.ArrayList;
import java.util.List;

class Employee {
    int id;
    String name;
    double salary;

    // Constructor
    Employee(int id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }
}

public class practical4 {
    public static void main(String[] args) {

        // Creating employee list
        List<Employee> empList = new ArrayList<>();

        empList.add(new Employee(1, "Om", 20000));
        empList.add(new Employee(2, "Rahul", 1200));
        empList.add(new Employee(3, "Sneha", 45000));
        empList.add(new Employee(4, "Amit", 60000));
        empList.add(new Employee(5, "Priya", 30000));

        // Counting employees with salary between 1500 and 50000
        long count = empList.stream()
                .filter(emp -> emp.salary >= 1500 && emp.salary <= 50000)
                .count();

        // Display result
        System.out.println("Number of Employees with salary between 1500 and 50000: " + count);
    }
}