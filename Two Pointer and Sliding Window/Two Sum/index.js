function twoSum(arr, target){
    let n = arr.length
    let map = {}
    for (let i = 0; i < n; i++){
        map[arr[i]] = i
    }

    for(let i = 0 ; i < n; i++){
        let pF = target - arr[i]
        if(map[pF] && map[pF] != i){
            return [i, map[pF]]
        }
    }
}

let ans = twoSum([2,7,11,15], 9)

console.log(ans)

// Approach 2

function twoSum(arr, target) {
    const numToIndex = {};
    for (let i = 0; i < arr.length; i++) {
        const num = arr[i];
        const complement = target - num;
        if (complement in numToIndex) {
            return [numToIndex[complement], i];
        }
        numToIndex[num] = i;
    }
}

