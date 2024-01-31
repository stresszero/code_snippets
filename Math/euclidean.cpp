#include <algorithm>
#include <iostream>

using namespace std;

int euclidean(int X, int Y) {
  if (X < Y)
    swap(X, Y);

  while (Y != 0) {
    int Temp = X % Y;
    X = Y;
    Y = Temp;
  }
  return X;
}

int main() {
  int X, Y;
  cin >> X >> Y;
  cout << euclidean(X, Y);
}