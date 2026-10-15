class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)

        for s in sandwiches:
            queued = len(students)
            for _ in range(queued):
                pref = students.popleft()
                if pref == s:
                    break
                students.append(pref)
            if queued == len(students):
                return queued

        return 0
