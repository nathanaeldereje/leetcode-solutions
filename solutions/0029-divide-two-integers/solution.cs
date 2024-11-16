public class Solution {
    public int Divide(int dividend, int divisor) {
  if (divisor == 0)
    {
        throw new DivideByZeroException("Divisor cannot be zero.");
    }

    // Handle edge case for dividend = int.MinValue and divisor = -1
    if (dividend == int.MinValue && divisor == -1)
    {
        return int.MaxValue; // Prevent overflow
    }

    // Determine the sign of the result
    bool isNegative = (dividend < 0) ^ (divisor < 0);

    // Convert to long and work with absolute values to prevent overflow
    long absDividend = Math.Abs((long)dividend);
    long absDivisor = Math.Abs((long)divisor);

    int result = 0;

    // Perform bit manipulation-based division
    while (absDividend >= absDivisor)
    {
        long tempDivisor = absDivisor;
        int multiple = 1;

        // Double the divisor until it exceeds the dividend
        while (absDividend >= (tempDivisor << 1))
        {
            tempDivisor <<= 1;
            multiple <<= 1;
        }

        // Subtract the largest found divisor and add the multiple
        absDividend -= tempDivisor;
        result += multiple;
    }

    // Apply the sign to the result
    return isNegative ? -result : result;
    }
    }



