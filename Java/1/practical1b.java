import java.util.LinkedList;

public class practical1b {
    public static void main(String[] args) {

        // Creating LinkedList
        LinkedList<String> list = new LinkedList<>();

        // Adding elements
        list.add("Apple");
        list.add("Banana");
        list.add("Mango");
        list.add("Apple");
        list.add("Orange");
        list.add("Apple");

        // Element to search
        String element = "Apple";

        // Finding occurrences
        int first = list.indexOf(element);
        int last = list.lastIndexOf(element);

        // Display result
        System.out.println("Linked List: " + list);
        System.out.println("First occurrence of " + element + " is at index: " + first);
        System.out.println("Last occurrence of " + element + " is at index: " + last);
    }
}