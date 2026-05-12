import java.util.Objects;

public class UserValidator {
    public static void main(String[] args) {
        // Simulating user input comparison
        String registeredUser = new String("admin_user");
        String loginAttempt = new String("admin_user");

        System.out.println("Checking credentials for: " + loginAttempt);

        // BUG: Using == for string object comparison instead of .equals()
        // This compares memory references rather than content.
        if (loginAttempt == registeredUser) {
            System.out.println("Login Successful: Identity verified.");
        } else {
            System.out.println("Login Failed: Strings do not match reference.");
        }
    }
}
