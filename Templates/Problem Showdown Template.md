# Problem

You are given an integer array  `height`  of length  `n`. There are  `n`  vertical lines drawn such that the two endpoints of the  `ith`  line are  `(i, 0)`  and  `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return  _the maximum amount of water a container can store_.

**Notice**  that you may not slant the container.

Example 1:

![image](../../Images/question_11.jpg)

>**Input:** height = [1,8,6,2,5,4,8,3,7]
**Output:** 49
**Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

**Example 2:**

>**Input:** height = [1,1]
**Output:** 1

# Solution

If we need to find the maximum amount of water a container can store, we need to find the two lines that maximize the area formed between them, where the capacity of the container would be the distance between both lines and the minimum height between those.

In order to solve this problem, I used the 2 pointers strategy: `i` pointing at the start of the array `height` and `n` pointing at its end.

Then, while `i` is different than `n` I first get the height of those two points and I define the capacity as the minimum of `left` and `right` multiplied by the difference between `n` and `i`, I will call this temporary capacity as `x`.

If `x` is greater than the capacity `cpt` (which at the start is zero), then `cpt` becomes `x`. If it is not greater, I compare the heights of `left` and `right`: if left is smaller than right, I increase the `i` pointer by 1, if it's bigger, then I substract 1 from `n`.

At the end, `cpt` will be the largest amount of water.

### Python
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height) - 1
        cpt = 0
        x = 0
        i = 0
        
        while i != n:
            left = height[i]
            right = height[n]
            x = min(left, right) * (n-i)
            if x > cpt:
                cpt = x
            else:
                if left < right:
                    i = i + 1
                else:
                    n = n - 1
        return cpt  
```