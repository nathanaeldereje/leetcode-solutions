class Solution {
    public int lengthOfLongestSubstring(String s) {
         String lon = "";

        for (int i = 0; i < s.length(); i++) {
            StringBuilder x = new StringBuilder();
            for (int j = i; j < s.length(); j++) {
                String h = String.valueOf(s.charAt(j));
                if (x.toString().contains(h)) {
                    break;
                } else
                    x.append(h);
            }
            if (x.length() > lon.length())
                lon = String.valueOf(x);

        }

        return lon.length();
    }
}

