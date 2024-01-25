#include <bits/stdc++.h>
using namespace std;

int T;
string a, b, s, d;
int main() {
  /* std::getline() */
  cin >> T;
  string bufferflush;
  getline(cin, bufferflush);

  for (int i = 0; i < T; i++) {
    getline(cin, d);   // abc def 입력하면
    cout << d << "\n"; // abc def 출력
  }

  /* 입출력 싱크 해제 */
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  /* 입출력 싱크를 해제한 후엔 cin, cout만 쓸 것 */
  return 0;
}
