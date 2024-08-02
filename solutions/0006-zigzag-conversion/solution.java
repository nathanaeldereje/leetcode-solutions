class Solution {
    public String convert(String s, int numRows) {
        String []sArr=new String[numRows];
        int max=numRows-1;
        int x=0;
        int prev=-1;
        for(int i=0;i<s.length();i++){
            if(numRows==1)return s;
            if(x==max) {
                if(sArr[x]==null)
                    sArr[x]= String.valueOf(s.charAt(i));
                else {
                    sArr[x] = sArr[x] + String.valueOf(s.charAt(i));

                }
                prev = x;
                x--;
            }
            else if(x==0){
                if(sArr[x]==null)
                    sArr[x]= String.valueOf(s.charAt(i));
                else {
                    sArr[x] = sArr[x] + String.valueOf(s.charAt(i));

                }
                prev = x;
                x++;
            }
//            else if(prev<0){
//                System.out.println("invalid ");
//            }
            else if(x>prev){
                if(sArr[x]==null)
                    sArr[x]= String.valueOf(s.charAt(i));
                else {
                    sArr[x] = sArr[x] + String.valueOf(s.charAt(i));

                }
                prev = x;
                x++;
            }
            else if(x<prev){
                if(sArr[x]==null)
                    sArr[x]= String.valueOf(s.charAt(i));
                else {
                    sArr[x] = sArr[x] + String.valueOf(s.charAt(i));

                }
                prev = x;
                x--;

            }
        }
        StringBuilder main = new StringBuilder(sArr[0]);
        for(int i=1;i<numRows;i++){
            if(sArr[i]!=null)
                main.append(sArr[i]);
        }
        String mm=main.toString();

        return mm;
    }
}
