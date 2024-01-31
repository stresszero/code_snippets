#include <iostream>
#include <vector>
using namespace std;

vector<int> sieveOfEratosthenes(int n) {
  vector<bool> isPrime(n + 1, true);
  vector<int> primes;

  for (int p = 2; p * p <= n; p++) {
    if (!isPrime[p])
      continue;
    for (int i = p * p; i <= n; i += p)
      isPrime[i] = false;
  }

  for (int p = 2; p <= n; p++) {
    if (isPrime[p])
      primes.push_back(p);
  }

  return primes;
}

int main() {
  vector<int> primes = sieveOfEratosthenes(50);
  for (int i = 0; i < primes.size(); i++)
    cout << primes[i] << "\n";

  return 0;
}