class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = [0]*len(queries)
        for i in range(len(points)):
            for j in range(len(queries)):
                if (points[i][0] - queries[j][0])**2 + (points[i][1] - queries[j][1])**2 <= queries[j][2]**2:
                    answer[j] += 1
        return answer
