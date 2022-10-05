/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
    
class Solution {
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth==1) {
            TreeNode newTree = new TreeNode(val, root, null);
            return newTree;
        }
        
        Deque<TreeNode> queue = new ArrayDeque<TreeNode>();
        queue.add(root);
        int currentDepth = 1;
        
        while (currentDepth < depth-1) {
            // basically create a list of next level nodes to process
            Deque<TreeNode> nextDepthQueue = new ArrayDeque<TreeNode>();
            
            // take each node in previous list and put its children here
            while (!queue.isEmpty()) {
                TreeNode node = queue.poll();
                if (node.left!=null) { nextDepthQueue.add(node.left); }
                if (node.right!=null) { nextDepthQueue.add(node.right); }
            }
            currentDepth++;
            queue = nextDepthQueue;
        }
        
        // now we have a list of nodes whose children will be replaced
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            node.left = new TreeNode(val, node.left, null);
            node.right = new TreeNode(val, null, node.right);
        }
        
        return root;
    }
}