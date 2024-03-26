#include <iostream>
#include <stack>
#include <vector>

using namespace std;

// Graph class
class Graph {
  int V; // Number of vertices

  // Pointer to an array containing adjacency lists
  vector<int> *adj;

public:
  // Constructor
  Graph(int V);

  // Function to add an edge to the graph
  void addEdge(int v, int w);

  // DFS traversal of the vertices reachable from v
  void DFS(int v);
};

// Constructor
Graph::Graph(int V) {
  this->V = V;
  adj = new vector<int>[V];
}

// Function to add an edge to the graph
void Graph::addEdge(int v, int w) {
  adj[v].push_back(w); // Add w to v’s list
}

// DFS traversal of the vertices reachable from v
void Graph::DFS(int v) {
  // Mark all the vertices as not visited
  vector<bool> visited(V, false);

  // Create a stack for DFS
  stack<int> stack;

  // Push the current source node
  stack.push(v);

  while (!stack.empty()) {
    // Pop a vertex from stack and print it
    v = stack.top();
    stack.pop();

    // Stack may contain same vertex twice. So
    // we need to print the popped item only
    // if it is not visited.
    if (!visited[v]) {
      cout << v << " ";
      visited[v] = true;
    }

    // Get all adjacent vertices of the popped vertex v
    // If an adjacent has not been visited, then push it
    // to the stack.
    for (auto it = adj[v].begin(); it != adj[v].end(); ++it)
      if (!visited[*it])
        stack.push(*it);
  }
}

int main() {
  Graph g(4); // Create a graph with 4 vertices
  g.addEdge(0, 1);
  g.addEdge(0, 2);
  g.addEdge(1, 2);
  g.addEdge(2, 0);
  g.addEdge(2, 3);
  g.addEdge(3, 3);

  cout << "Depth First Traversal (starting from vertex 2): ";
  g.DFS(2);

  return 0;
}
