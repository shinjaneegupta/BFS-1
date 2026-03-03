# Time Complexity : O(V+E)
# Space Complexity : O(V+E)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Approach : BFS to perform topological sort by starting with nodes having indegree = 0.
# For each course, reduce the indegree of its dependents and add them to the queue if their indegree becomes 0.
# If we can visit all courses this way, there's no cycle, and the courses can be completed.


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adjacencyMatrix = {}

        for pr in prerequisites:
            indegrees[pr[0]] += 1
            if pr[1] not in adjacencyMatrix:
                adjacencyMatrix[pr[1]] = []
            adjacencyMatrix[pr[1]].append(pr[0])

        count = 0
        q = deque()

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
                count += 1

        if not q:
            return False
        if count == numCourses:
            return True

        while q:
            curr = q.popleft()
            deps = adjacencyMatrix.get(curr)
            if deps:
                for dep in deps:
                    indegrees[dep] -= 1
                    if indegrees[dep] == 0:
                        q.append(dep)
                        count += 1
                        if count == numCourses:
                            return True

        return False
        