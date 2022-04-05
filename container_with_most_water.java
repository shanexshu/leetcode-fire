class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int ans = 0;
        int minHeight;
        
        while (left<right) {
            minHeight = Math.min(height[left], height[right]);
            ans = Math.max(ans, minHeight * (right-left));
            if (minHeight==height[left]) {
                left++;
            }
            else {
                right--;
            }
        }
        return ans;
    }
}