#include <iostream>
#include <list>
#include <queue>

using namespace std;

// Graph class
class Graph {
  int V; // Number of vertices

  // Pointer to an array containing adjacency lists
  list<int> *adj;

public:
  // Constructor
  Graph(int V);

  // Function to add an edge to the graph
  void addEdge(int v, int w);

  // BFS traversal of the vertices reachable from s
  void BFS(int s);
};

// Constructor
Graph::Graph(int V) {
  this->V = V;
  adj = new list<int>[V];
}

// Function to add an edge to the graph
void Graph::addEdge(int v, int w) {
  adj[v].push_back(w); // Add w to v’s list
}

// BFS traversal of the vertices reachable from s
void Graph::BFS(int s) {
  // Mark all the vertices as not visited
  bool *visited = new bool[V];
  for (int i = 0; i < V; i++)
    visited[i] = false;

  // Create a queue for BFS
  queue<int> queue;

  // Mark the current node as visited and enqueue it
  visited[s] = true;
  queue.push(s);

  while (!queue.empty()) {
    // Dequeue a vertex from queue and print it
    s = queue.front();
    cout << s << " ";
    queue.pop();

    // Get all adjacent vertices of the dequeued vertex s
    // If an adjacent has not been visited, then mark it
    // visited and enqueue it
    for (auto it = adj[s].begin(); it != adj[s].end(); ++it) {
      if (!visited[*it]) {
        visited[*it] = true;
        queue.push(*it);
      }
    }
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

  cout << "Breadth First Traversal (starting from vertex 2): ";
  g.BFS(2);

  return 0;
}
