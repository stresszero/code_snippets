// C++ code to print the first N terms of Moser-de Bruijn Sequence
#include <bits/stdc++.h>
using namespace std;

// recursive function to get the Nth term of the sequence
int rec(int N) {
  if (N == 0) // as M(0)=0
    return 0;

  else if (N == 1) // as M(1)=1
    return 1;

  else if (N & 1) // for the case when N is odd
    return 4 * rec(N / 2) + 1;

  else // for the case when N is even
    return 4 * rec(N / 2);
}

// function to update the vector using dp
void calculate_numbers(vector<int> &dp, int N) {

  dp[0] = 0; // as M(0)=0
  dp[1] = 1; // M(1)=1

  for (int i = 2; i < N; i++) {
    if ((i & 1) == 0) // if i is even
      dp[i] = 4 * dp[i / 2];
    else // if i is odd
      dp[i] = 4 * dp[i / 2] + 1;
  }
}

// function to print the first N terms of the Moser-de Bruijn sequence
void print_sequence(vector<int> &dp, int N) {
  for (int i = 0; i < N; i++)
    cout << dp[i] << "  ";
}

int main() {
  int N; // for taking input
  N = 35;

  vector<int> dp(N, 0); // to store first N terms of the sequence

  // calling the function to update the array up to N
  calculate_numbers(dp, N);

  // to print the sequence
  print_sequence(dp, N);

  return 0;
}