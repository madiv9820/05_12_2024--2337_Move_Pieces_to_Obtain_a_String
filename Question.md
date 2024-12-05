# [2337. Move Pieces to Obtain a String](https://leetcode.com/problems/move-pieces-to-obtain-a-string?envType=daily-question&envId=2024-12-05)

__Type:__ Medium <br>
__Topics:__ Two Pointers, String <br>
__Companies:__ Google, Amazon 
<hr>

You are given two strings `start` and `target`, both of length `n`. Each string consists **only** of the characters `'L'`, `'R'`, and `'_'` where:

- The characters `'L'` and `'R'` represent pieces, where a piece `'L'` can move to the **left** only if there is a **blank** space directly to its left, and a piece `'R'` can move to the **right** only if there is a **blank** space directly to its right.
- The character `'_'` represents a blank space that can be occupied by **any** of the `'L'` or `'R'` pieces.

Return `true` *if it is possible to obtain the string* `target` *by moving the pieces of the string* `start` ***any** number of times.* Otherwise, return `false`.
<hr>

### Examples:
- **Example 1:** <br>
**Input:** start = "_L__R__R_", target = "L______RR" <br>
**Output:** true <br>
**Explanation:** We can obtain the string target from start by doing the following moves: <br> - Move the first piece one step to the left, start becomes equal to "L___R__R_". <br> - Move the last piece one step to the right, start becomes equal to "L___R___R".<br> - Move the second piece three steps to the right, start becomes equal to "L______RR". <br> Since it is possible to get the string target from start, we return true.

- **Example 2:** <br>
**Input:** start = "R_L_", target = "__LR" <br>
**Output:** false <br>
**Explanation:** The 'R' piece in the string start can move one step to the right to obtain "_RL_". <br>
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.

- **Example 3:** <br>
**Input:** start = "_R", target = "R_" <br>
**Output:** false <br>
**Explanation:** The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.
<hr>

### Constraints:
- `n == start.length == target.length`
- <code>1 <= n <= 10<sup>5</sup></code>
- `start` and `target` consist of the characters `'L'`, `'R'`, and `'_'`.
<hr>

### Hints:
- After some sequence of moves, can the order of the pieces change?
- Try to match each piece in s with a piece in e.