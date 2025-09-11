// 503. Next Greater Element II

// Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

// The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

// Example 1:

// Input: nums = [1,2,1]
// Output: [2,-1,2]
// Explanation: The first 1's next greater number is 2; 
// The number 2 can't find next greater number. 
// The second 1's next greater number needs to search circularly, which is also 2.
// Example 2:

// Input: nums = [1,2,3,4,3]
// Output: [2,3,4,-1,4]
 

// DOuble the Array when you see circular

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function(nums) {
    let arr = [...nums, ...nums]
    let n = arr.length; 
    let stack = []
    let ans = Array(n).fill(-1)
    stack.push(arr[n - 1])
    for (let i = n - 2; i >= 0; i--) {
        while(stack.length){
            let top = stack[stack.length - 1]
            if(arr[i] < top) {
                ans[i] = top
                break;
            } else {
                stack.pop()
            }
        }
        stack.push(arr[i])
    }
    return ans.slice(0, n/2)
};


// Without Circular

var nextGreaterElements2 = function(arr) {
    let n = arr.length; 
    let stack = []
    let ans = Array(n).fill(-1)
    stack.push(arr[n - 1])
    for (let i = (2 * n) - 2; i >= 0; i--) {
        while(stack.length){
            let top = stack[stack.length - 1]
            if(arr[i % n] < top) {
                ans[i % n] = top
                break;
            } else {
                stack.pop()
            }
        }
        stack.push(arr[i % n])
    }
    return ans.slice(0, n)
};

console.log(nextGreaterElements2([1,2,1]))
