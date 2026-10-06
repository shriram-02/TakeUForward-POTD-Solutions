class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)

        state = [0] * n

        def dfs(node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            if not graph[node]:
                return node == destination

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            return True

        return dfs(source)