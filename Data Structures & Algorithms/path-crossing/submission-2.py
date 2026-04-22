class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = [(0,0)]
        x = 0
        y = 0
        for z in path:
            if z == 'N':
                x += 1
            elif z == 'S':
                x -= 1
            elif z == 'E':
                y += 1
            else:
                y -= 1
            if (x,y) in visited:
                return True
            visited.append((x,y))
            

        return False