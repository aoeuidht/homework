#Longest Substring Without Repeating Characters 


## Question

Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

## Solution

Assume we have a string, and two pointers: __head__, __tail__, between which there are no duplicate chars:

```
... c0 c1 c2 c3 c4 c5 ....
       |            |
       header       tail
       
```

If we move the __tail__ forward, then there are 2 cases:

* still no duplicate chars between head and tail
* the character tail pointer point at is dup with some char between head and tail, we call it __p_dup__, now we have the head pointer to the char next to __p_dup__, to keep the distinction of chars between head and tail, as described below:

```
... c0 c1 c2 c3 ... c_dup c_next c4 c5 c_dup....
       |                  |              |
       header  ---------> new_head       tail
       
```

as we move the tail pointer forward, we do two things:

* calculate the length of the valid substring, record the longest
* move head pointer, if necessary

then we can get the correct result.

How can we know the chars between two pointers? I use a list with length 256, and use the value at index __ord(char)__ to remember the position of the character. While moving the head pointer forward, remember cleaning the chars we parsed