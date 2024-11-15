public class Solution {
    public string IntToRoman(int num) {
        
        int[] mainNums = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        string[] symbols = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        StringBuilder roman = new StringBuilder();
        for (int i = 0; i < mainNums.Length && num > 0; i++)
        {
            while (num >= mainNums[i])
            {
                roman.Append(symbols[i]);
                num -= mainNums[i];
            }
        }

        return roman.ToString();

    }
}
