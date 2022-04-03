class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 1;
        int j;
        int temp;
        if (i==0) {
            return;
        }
        //go backwards and find if number decreases
        boolean done = false;
        for (i = i-1; i>=0; i--) {
            if (nums[i+1] > nums[i]) {
                //if it does, that number needs to be replaced by the next highest number after it
                for (j = nums.length-1; j > i; j--) {
                    if (nums[j] > nums[i]) {
                        temp = nums[i];
                        nums[i] = nums[j];
                        nums[j] = temp;
                        done = true;
                        break;
                    }
                }
                if (done) {
                    break;
                }
            }
        }

        //flip the rest, from the point where you found the decrese (from i+1 to end)
        i++;
        j = nums.length - 1;
        while (j>i) {
            temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
        
    }
}

/*
123
 i
  j
132
213
231
312
321
123

12345
12354
-12534

12435
12453
-12543

12534
12543
13245
...
14532
 i
   j


93081294182093809842312
*/