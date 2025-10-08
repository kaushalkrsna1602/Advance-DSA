// 540. Single Element in a Sorted Array
// You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

// Return the single element that appears only once.

// Your solution must run in O(log n) time and O(1) space.

 

// Example 1:

// Input: nums = [1,1,2,3,3,4,4,8,8]
// Output: 2
// Example 2:

// Input: nums = [3,3,7,7,10,11,11]
// Output: 10
 

// Constraints:

// 1 <= nums.length <= 105
// 0 <= nums[i] <= 105

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(arr) {
  let l = 0; 
  let r = arr.length - 1
  while ( l <= r) {
    let m = l + Math.floor((r - l )/ 2)
    // pair exists on left sode
    if(arr[m] === arr[m-1]) {
        leftCount = m - 1 - l
        if(leftCount % 2 === 1) {
            r = m - 2
        }else {
            l = m + 1
        }
    }
    // Pair exist on right side
    else if (arr[m] === arr[m+1]){
        leftCount = m - l
        if(leftCount % 2 === 1) {
            r = m - 1
        } else {
            l = m + 2
        }
    }
    else {
        return arr[m]
    }
  }  
};