class Solution {
    public static int countCompleteComponents(int n, int[][] edges) {
        // Graph adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        // Build the graph
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        boolean[] visited = new boolean[n];
        int completeCount = 0;

        // Traverse all nodes
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                List<Integer> component = new ArrayList<>();
                int edgeCount = bfs(graph, i, visited, component);

                int size = component.size();
                int expectedEdges = (size * (size - 1)) / 2;
                
                // If the component forms a complete graph, count it
                if (edgeCount == expectedEdges) {
                    completeCount++;
                }
            }
        }
        return completeCount;
    }

    private static int bfs(List<List<Integer>> graph, int start, boolean[] visited, List<Integer> component) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = true;
        component.add(start);

        int edgeCount = 0;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int neighbor : graph.get(node)) {
                edgeCount++;
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.offer(neighbor);
                    component.add(neighbor);
                }
            }
        }

        // Since each edge is counted twice, divide by 2
        return edgeCount / 2;
    }

}
