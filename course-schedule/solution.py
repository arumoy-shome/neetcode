from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        course_map = defaultdict(list)
        { course_map[k].append(v) for k, v in prerequisites }
        visited = set()
        
        def dfs(curr):
            if not course_map[curr]:
                return True
            if curr in visited:
                return False
            
            visited.add(curr)
            
            for pre in course_map[curr]:
                dfs(pre)

    
if __name__ == "__main__":
    pass
