public class Main {
    public static void main(String[] args) {
        String s1 = new String("test");
        String s2 = new String("test");
        // BUG: Reference comparison
        if (s1 == s2) {
            System.out.println("Equal");
        } else {
            System.out.println("Not Equal");
        }
    }
}
// Line 13
// Line 14
