public class Solution {
    public int MySqrt(int x) {
        double tolerance = 0.0001;
         if (x < 0)
        {
            throw new ArgumentException("Cannot compute the square root of a negative number.");
        }

        // Initial guess is half of the number
        double guess = x / 2.0;

        // Keep refining the guess until the difference is within tolerance
        while (Math.Abs(guess * guess - x) > tolerance)
        {
            guess = (guess + x / guess) / 2.0;
        }

        return (int)guess;
    }
    
}
