class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        gragh = defaultdict(list)
        in_degree = [0] * numCourses

        for course,pre in prerequisites:
            gragh[pre].append(course)
            in_degree[course] += 1

        completed = 0

        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        while q:
            prev = q.popleft()
            completed += 1

            for course in gragh[prev]:

                in_degree[course] -= 1
                if in_degree[course] == 0:
                    q.append(course)
        return completed == numCourses


