"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
"""
#DFS or BFS (I think is BFS), Traverse each array recursively, starting from the starting point.
#Color it 4 directionally, unless it goes out of bounds (< 0) or hits a zero, or if it is already new color.

class Solution():
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        old_color = image[sr][sc]

        #if current cell is not new color, execute helper function, which is recursive
        if old_color != newColor:
            self.helper(image, sr, sc, old_color, newColor)
        return image

    def helper(self, image, i, j , old_color, new_color):
        #if row value is out of bounds (< 0) or exceeds maximum (len(image)-1), return False
        if i < 0 or i > len(image) - 1:
            return
        #if column value is out of bounds (< 0 ) or exceeds maximum (len(image)-1), return False
        if j < 0 or j > len(image) - 1:
            return
        #check if current cell is NOT old color, meaning it is ALREADY COLORED. Then we just skip this iteration.
        if image[i][j] != old_color:
            return
        else:
            #Set current cell to new color.
            image[i][j] = new_color
            #Followed by recursively running through all 4 directions: i = row, j = column
            self.helper(image, i, j - 1, old_color, new_color) #left
            self.helper(image, i, j + 1, old_color, new_color) #right
            self.helper(image, i - 1, j, old_color, new_color) #bottom
            self.helper(image, i + 1, j, old_color, new_color) #top

#Time Complexity: O(M*N)
#Space Complexity: O(1)