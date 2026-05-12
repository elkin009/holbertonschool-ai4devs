cat <<EOF > smart_bug_bounty/bug_snippets/bug3.java
public class Calculator {
    public static double getAverage(int[] nums) {
        if (nums.length == 0) return 0.0;
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }
        // BUG: Integer division truncates decimals before returning double
        return sum / nums.length;
    }
}
EOF
