import java.util.HashSet;
import java.util.TreeSet;

public class practical1c {
    public static void main(String[] args) {

        // Creating HashSet
        HashSet<String> hashSet = new HashSet<>();

        // Adding elements
        hashSet.add("Mango");
        hashSet.add("Apple");
        hashSet.add("Banana");
        hashSet.add("Orange");

        // Display HashSet
        System.out.println("HashSet: " + hashSet);

        // Converting HashSet to TreeSet
        TreeSet<String> treeSet = new TreeSet<>(hashSet);

        // Display TreeSet
        System.out.println("TreeSet: " + treeSet);
    }
}