#include <bits/stdc++.h>
using namespace std;

vector<string> split(string input, string delimiter) {
  vector<string> ret;
  long long pos = 0;
  string token = "";
  while ((pos = input.find(delimiter)) != string::npos) {
    token = input.substr(0, pos);
    ret.push_back(token);
    input.erase(0, pos + delimiter.length());
  }
  ret.push_back(input);
  return ret;
}

// 문자열 split 함수의 구현, 시간복잡도 O(n)
// 인수 input: split 대상 문자열, delimiter: 구분자 문자열
vector<string> split(string input, string delimiter) {
  // 필요한 변수 초기화
  vector<string> ret;
  long long pos = 0;
  string token = "";

  // pos: 구분자의 위치, string::npos는 find()가 더 이상 구분자를 찾지 못했을 때 반환하는 값
  // 그러므로 구분자가 나올 때까지 반복하게 됨
  while ((pos = input.find(delimiter)) != string::npos) {
    token = input.substr(0, pos);             // 구분자가 있는 위치까지 string::substr()로 문자열을 자름
    ret.push_back(token);                     // 위에서 잘라온 문자열만 벡터의 끝에 삽입, 값은 원래 대상에서 복사됨
    input.erase(0, pos + delimiter.length()); // token과 구분자를 원래 문자열에서 제거
  }
  ret.push_back(input); // 반복이 끝나면 구분자가 모두 제거된 문자열의 마지막 부분을 벡터 ret에 삽입하고 반환
  return ret;
}

int main() {
  vector<string> str = split("ABCXDEFXTTTXQWER", "X");
  for (string i : str)
    cout << i << endl; // ABC DEF TTT QWER 한줄씩 출력
  return 0;
}