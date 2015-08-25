# Add two numbers

## Question
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

__Input:__ (2 -> 4 -> 3) + (5 -> 6 -> 4)

__Output:__ 7 -> 0 -> 8

## Solution

This question is kind of like a "sum of linked list", so the scenario with __carry__ are complex, such as:

* list a is as long as list b, but carry happens at the last num
* a is shorter/longger than list b, and carry happens at the last item of a/b
* a is shorter/longger than list b, and carry happens at the last item of a/b, and any other item in the b/a left

In the solution, use a __carry mark__ to remember the carry value, and in the compuation, when the carry_mark is not 0.

* either list is not blank, we sum carry_mark and the non-blank list item togher
* both lists are blank, we create a new node, put the carry_mark as the value, then end the task

What happens when the carry_mark is 0? There are 2 cases:

* if both lists are blank, termitane the task
* if one list left, then just contact the result with the left list