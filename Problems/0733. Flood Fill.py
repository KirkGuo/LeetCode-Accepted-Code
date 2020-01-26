class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        q = [[sr, sc]]
        tgt = image[sr][sc]
        if tgt==newColor:
            return image
        while q:
            r, c = q.pop(0)
            if 0<=r<len(image) and 0<=c<len(image[0]) and image[r][c]==tgt:
                image[r][c] = newColor
                steps = [[0,1],[0,-1],[-1,0],[1,0]]
                for step in steps:
                    q.append([r+step[0], c+step[1]])
        return image
