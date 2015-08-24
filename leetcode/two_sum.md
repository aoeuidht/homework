#two sum

## question
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

__Input:__ numbers={2, 7, 11, 15}, target=9

__Output:__ index1=1, index2=2

## solution

Let's simplify this question a little bit:

__Give an array with ascender numbers, find two nums whose sum is a specific number(N)__

To resolve it, we can use two pointers: one point at the head of the list, the other one point at the tail. Then

* __*phead + *ptail > N__, it means we should move the tail pointer left;
*  __< N__, then we move the head pointer right
*  __= N__ , then we found the result

Back to the question, how can we gen the index of the numbers we found using the method descripted? Before we lookup for the numbers, we generate a new map, with number as key, and index as the value. After we found the two correct numbers, we just get their index from the map.