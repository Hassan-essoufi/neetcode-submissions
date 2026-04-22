class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = []
        for i in path:
            if i not in visited:
                visited.append(i)
            else:
                return True
        return False