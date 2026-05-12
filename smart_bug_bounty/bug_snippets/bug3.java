
public class UserCheck {
    public static void main(String[] args) {
        String user1 = new String("Alice");
        String user2 = new String("Alice");
        // BUG: Using == for object comparison instead of .equals()
        if (user1 == user2) {
            System.out.println("Users are the same.");
        } else {
            System.out.println("Users are different.");
        }
    }
}
