// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}


// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public boolean isSubPath(ListNode head, TreeNode root) {
        boolean pathRes;

        if (root == null) {
            return false;
        }

        if (root.val == head.val) {
            pathRes = findPath(head, root);

            if (pathRes) {
                return true;
            }
        }


        boolean[] res = new boolean[]{isSubPath(head, root.left), isSubPath(head, root.right)};
        return found(res);

    }

    boolean findPath(ListNode head, TreeNode root) {
        if (head == null) {
            return true;
        }

        if (root == null) {
            return false;
        }

        if (head.val == root.val) {
            boolean[] res = new boolean[]{findPath(head.next, root.left), findPath(head.next, root.right)};

            return found(res);
        }

        return false;
    }

    boolean found(boolean[] boolList) {
        return (boolList[0] || boolList[1]);
    }
}
