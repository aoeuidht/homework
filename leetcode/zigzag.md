# ZigZag Conversion

## Question

The string __"PAYPALISHIRING"__ is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)


```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: __"PAHNAPLSIIGYIR"__


Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string text, int nRows);
```

__convert("PAYPALISHIRING", 3)__ should return __"PAHNAPLSIIGYIR"__.

## Solution

### step 1.

for a zigzag string (with height __6__), we can get the minium element like this

```
0   
1       9
2     8
3   7
4 6 
5
```

You can count the numbers in the element, it has __2 * N - 2__ numbers.

### step 2.

So how many elements in the final zigzag string?

__(len(s) - 1) / (2 * N - 2) + 1__

now we can loop from 0 to __2 * N - 2__, mark it as __i__.

### step 3.

What's the rules of nums in line __i__?

the 1st line:

```
0 2N-2 4N-4
```

the 2nd line:

```
1 2N-2-1 2N-2+1 4N-4-1 4N-4+1
```

the 3rd line:

```
2 2N-2-2 2N-2+2 4N-4-2 4N-4+2
```

the last line:

```
N-1, 2N-2+N-1, 4N-4+N-1, ...
```

so we have the code like:

```
# nRows is the height of zigzag string
# glen = nRows * 2 - 2
# gnum = (str(s) - 1) / glen + 1
for i in range(nRows):
    # columns
    for offset in range(gnum):
        idx = offset * glen + i
        if idx < slen:
            rst[piv] = s[idx]
            piv += 1
        # another to add
        if 0 < i < (nRows - 1):
            idx = offset * glen + glen - i
            if idx < slen:
                rst[piv] = s[idx]
                piv += 1
```

