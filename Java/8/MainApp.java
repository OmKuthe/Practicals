import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class MainApp {

    public static void main(String[] args) {

        // Create Configuration
        Configuration cfg = new Configuration();
        cfg.configure("hibernate.cfg.xml");
        cfg.addAnnotatedClass(Student.class);

        // Create SessionFactory
        SessionFactory factory = cfg.buildSessionFactory();

        // Create Session
        Session session = factory.openSession();

        // Create Student Object
        Student s = new Student(1, "Om", "om@gmail.com");

        // Transaction
        Transaction tx = session.beginTransaction();

        // Save Object
        session.save(s);

        // Commit Transaction
        tx.commit();

        System.out.println("Student Record Inserted Successfully!");

        // Close Session
        session.close();
        factory.close();
    }
}