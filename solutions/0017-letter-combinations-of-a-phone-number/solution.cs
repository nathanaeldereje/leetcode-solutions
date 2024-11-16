public class Solution {
    public IList<string> LetterCombinations(string input) {
   Dictionary<int, string> phonePad = new Dictionary<int, string>
        {
            { 1, null },
            { 2, "abc" },
            { 3, "def" },
            { 4, "ghi" },
            { 5, "jkl" },
            { 6, "mno" },
            { 7, "pqrs" },
            { 8, "tuv" },
            { 9, "wxyz" },
            { 0, " " } // 0 maps to space
        };

        // If the input is null or empty, return an empty list
        if (string.IsNullOrEmpty(input))
        {
            return new List<string>(); // Returns an empty list as IList
        }

        // Recursive function to build combinations
        return GetCombinations(input, phonePad);
    }

    static IList<string> GetCombinations(string input, Dictionary<int, string> phonePad)
    {
        // Base case: if input is empty, return a list with an empty string
        if (string.IsNullOrEmpty(input))
        {
            return new List<string> { "" };
        }

        // Get the first digit and the rest of the input
        int digit = int.Parse(input[0].ToString());
        string remainingInput = input.Substring(1);

        // Get the letters for the current digit
        string letters = phonePad.ContainsKey(digit) ? phonePad[digit] : null;

        // Get combinations for the remaining input
        IList<string> subCombinations = GetCombinations(remainingInput, phonePad);

        // IList to hold all the result combinations
        IList<string> result = new List<string>();

        if (string.IsNullOrEmpty(letters))
        {
            // If no letters (e.g., digit 1), propagate sub-combinations as-is
            foreach (var combo in subCombinations)
            {
                result.Add(combo);
            }
        }
        else
        {
            // Combine each letter with each sub-combination
            foreach (char letter in letters)
            {
                foreach (string combo in subCombinations)
                {
                    result.Add(letter + combo);
                }
            }
        }

        return result;
    }
}
