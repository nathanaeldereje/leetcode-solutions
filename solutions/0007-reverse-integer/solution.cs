public class Solution {
    public int Reverse(int x) {
       string s = new string(x.ToString().Reverse().ToArray());
        StringBuilder bld = new StringBuilder(s);
        if (bld[bld.Length-1] == '-')
        {
            bld.Replace(bld[bld.Length - 1].ToString(), "");
            bld.Insert(0, '-');
            s= bld.ToString();
        }
        long newx=long.Parse(s);
        if (!(newx >= Int32.MinValue) || !(newx <= Int32.MaxValue))
        {
            return 0;
        }
        
        return (int)newx;

    } 
    }

