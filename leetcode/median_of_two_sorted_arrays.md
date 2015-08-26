# Median of Two Sorted Arrays

## Question

There are two sorted arrays __nums1__ and __nums2__ of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


## Solution

### step 1. two small lists

Assume we have 2 small lists, how can we resolve this question? Maybe we just put nums1 and nums2 together, sort the new list again, then return the item in the mid position.


### step 2. shrink huge lists.

If we want to shrink the size of the lists, we have to consider two scenarios:

* S1

```
 nums1:   1 2 3 4 5 .... n
 nums2:                      n+x ....
```

There are no intersection between nums1 and nums2, so we just count two lists, and then return the proper value

* S2.0

```
 nums1:   1 2 3 4 5 6 .... n
 nums2:           5 ............ n+x
```

or

```
 nums1:   1 2 3 4 5 6 .... n
 nums2:           5 .. n-x
```

we handle these using the following algorithm:

1. get the mid item of nums1: __pivort__
2. get the index of the item in nums2 __whose value is the biggest among the items smaller than pivort__, let's call it __piv2__


then now we have two sub list groups:


__nums1[0] ... nums1[pivort],  nums2[0] ... nums2[piv2]__


and


__nums1[pivort] ... nums1[:end], nums2[piv2] ... nums[:end]__


what we do now is check which sub list group the target in, and do the previously steps recursively.
