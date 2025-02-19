# [Diamond IV] 퀸 게임 - 5642 

[문제 링크](https://www.acmicpc.net/problem/5642) 

### 성능 요약

메모리: 133280 KB, 시간: 332 ms

### 분류

게임 이론, 런타임 전의 전처리, 스프라그–그런디 정리

### 제출 일자

2024년 12월 12일 16:33:13

### 문제 설명

<p>퀸 게임은 R행 C열 체스판에서 즐길 수 있는 게임이다. 행은 1부터 R까지, 열은 1부터 C까지 번호가 매겨져 있다. 가장 왼쪽 위 사각형은 1행 1열이다.</p>

<p>이 게임은 두명이서 즐기는 게임이다. 체스판 위에는 퀸 N개가 칸에 놓여져 있다. 플레이어는 자신의 턴이 돌아오면, 퀸을 하나 선택한 다음 위쪽 방향, 왼쪽 방향, 왼쪽 위 대각선 방향중 하나로 움직일 수 있다. 움직이는 칸의 수는 제한이 없으나 퀸은 체스판 밖으로 나갈 수 없다. 퀸이 (1,1)에 도착하면, 퀸은 보드에서 제거된다. 마지막 퀸을 보드에서 제거하는 사람이 게임을 이기는 사람이다. 각 칸은 매우 커서 퀸을 무한히 많이 포함할 수 있다. 플레이어는 턴을 번갈아가면서 게임을 한다. </p>

<p>체스판의 크기와 퀸 N개의 위치가 주어진다. 두 플레이어가 항상 완벽하게 게임을 할 때, 누가 이기는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 R (1 ≤ R ≤ 25), C (1 ≤ C ≤ 10<sup>15</sup>), N (1 ≤ N ≤ 1000)이 주어진다. 다음 N개 줄에는 퀸의 위치가 주어진다. 첫 번째 숫자는 행 번호이고, 두 번째 숫자는 열 번호이다.</p>

### 출력 

 <p>각 테스트 케이스 마다 첫 번째 플레이어가 이기는 전략을 가지고 있으면 "YES"를, 아니면 "NO"를 출력한다.</p>

