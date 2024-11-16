public class Solution {
    public int CountDigitOne(int n) {
    int counter = 0;
    for (int place = 1; place <= n; place *= 10)
    {
        int divisor = place * 10;
        int current = (n / place) % 10;     // Current digit
        int left = n / divisor;            // Left part of the number
        int right = n % place;             // Right part of the number

        // Add counts based on the current digit
        if (current > 1)
            counter += (left + 1) * place;
        else if (current == 1)
            counter += left * place + (right + 1);
        else
            counter += left * place;
    }
    return counter;
    }
}
