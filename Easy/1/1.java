import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> store = new HashMap<>();
        int[] res = new int[2];
        int diff;

        for(int i = 0; i < nums.length; i++) {
            diff = target - nums[i];

            if (store.containsKey(diff)) {
                res[0] = store.get(diff);
                res[1] = i;

                return res;
            }

            store.put(nums[i], i);
        }

        return null;
    }
}