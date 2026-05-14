import java.util.Iterator;
import java.util.LinkedList;

public class practical1a {
    public static void main(String[] args) {

        // Creating LinkedList
        LinkedList<String> list = new LinkedList<>();

        // Adding elements
        list.add("Apple");
        list.add("Banana");
        list.add("Mango");
        list.add("Orange");

        // Reverse iteration
        Iterator<String> itr = list.descendingIterator();

        System.out.println("Linked List in Reverse Order:");

        while (itr.hasNext()) {
            System.out.println(itr.next());
        }
    }
}