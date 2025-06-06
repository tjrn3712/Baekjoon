# [Gold I] 독수리 - 16238 

[문제 링크](https://www.acmicpc.net/problem/16238) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 5월 24일 14:23:27

### 문제 설명

<p>독수리는 양을 먹으면서 살고 있다. 양이 사는 곳은 크기가 1×N인 직사각형으로 나타낼 수 있고, 1×1 크기의 칸으로 나누어져 있다. 칸은 왼쪽에서부터 1번, 2번, ..., N번으로 번호가 매겨져 있다. i번 칸에 사는 양의 수는 A<sub>i</sub>마리이다.</p>

<p>독수리는 매일 아침 양을 먹으러 간다. 1번 칸의 왼쪽이나 N번 칸의 오른쪽에서 날기 시작해 먹으려고 하는 양이 있는 칸까지 날아간다. 독수리는 칸을 벗어나서 날 수 없다. 먹으려고 하는 양이 있는 곳이 x번이라면, x번까지 날아간 다음, x번 칸에 있는 양을 모두 먹는다. 독수리는 하루에 한 칸에 있는 양만 먹을 수 있다.</p>

<p>양은 독수리를 매우 무서워하기 때문에, 독수리가 나는 모습을 보면 도망간다. 양은 칸의 위에 독수리가 나는 것을 확인하면 도망간다. 양이 도망가면, 그 칸에 있는 양의 수는 0마리가 된다. 예를 들어, 1번 칸의 왼쪽에서 날기 시작해서 x번 칸에 도착했다면, 1번부터 x-1번 칸까지에 있던 양이 모두 도망가 0마리가 된다. N번 칸의 오른쪽에서 날기 시작했다면, x+1번칸 부터 N번 칸까지에 있던 양이 모두 도망간다.</p>

<p>또한, 이곳은 위험한 곳이기 때문에, 매일 밤에 모든 칸에 있던 양의 수가 1마리씩 줄어든다.</p>

<p>독수리가 매일 매일 어떤 칸에 있는 양을 먹는지와 어느 쪽에서부터 날기 시작하는지에 따라 먹을 수 있는 양의 수가 달라진다.</p>

<p>양의 수가 주어졌을 때, 독수리가 먹을 수 있는 양의 수의 최댓값을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 칸의 개수 N이 주어진다. (1 ≤ N ≤ 1,000)</p>

<p>둘째 줄에 각 칸에 있는 양의 수 A<sub>1</sub>, A<sub>2</sub>, .., A<sub>N</sub>이 주어진다. (0 ≤ A<sub>i</sub> ≤ 100,000)</p>

### 출력 

 <p>첫째 줄에 독수리가 먹을 수 있는 양의 최대 수를 출력한다.</p>

