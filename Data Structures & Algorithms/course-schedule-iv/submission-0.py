class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre = [set() for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]

        for after, before in prerequisites:
            graph[before].append(after)

        visited = [False] * numCourses

        def dfs(curr_course):
            if not visited[curr_course]:
                visited[curr_course] = True
                for nei in graph[curr_course]:
                    pre[curr_course] = pre[curr_course] | {nei} | dfs(nei)
            return pre[curr_course]

        for course in range(numCourses):
            dfs(course)

        res = []
        for before, after in queries:
            res.append(before in pre[after])

        return res
