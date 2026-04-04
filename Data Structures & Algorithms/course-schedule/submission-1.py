class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for after, before in prerequisites:
            in_degree[after] += 1
            graph[before].append(after)
        
        queue = deque()
        courses = 0

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            next_course = queue.popleft()
            courses += 1
            for nei in graph[next_course]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return courses == numCourses