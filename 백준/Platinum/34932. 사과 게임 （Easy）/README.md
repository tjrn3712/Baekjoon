# [Platinum IV] 사과 게임 (Easy) - 34932 

[문제 링크](https://www.acmicpc.net/problem/34932) 

### 성능 요약

메모리: 111308 KB, 시간: 108 ms

### 분류

게임 이론, 홀짝성

### 제출 일자

2025년 12월 25일 05:16:51

### 문제 설명

<p><span style="color:#e67e22;"><strong>테라</strong></span>와 <span style="color:#8e44ad;"><strong>루루</strong></span>는 과수원을 운영하고 있다. <span style="color:#e67e22;"><strong>테라</strong></span>와 <span style="color:#8e44ad;"><strong>루루</strong></span>는 과수원에서 맛있는 사과 $N$개를 수확해 나눠 가지려고 한다. 사과를 나누던 방식이 지겨워진 <span style="color:#e67e22;"><strong>테라</strong></span>는 게임을 통해 사과를 나누자고 제안했다.</p>

<p>테이블에 사과를 무작위 순서대로 원형으로 올려둔다. <span style="color:#8e44ad;"><strong>루루</strong></span>는 테이블 위에 있는 사과 하나를 골라 시작 위치로 지정한다. <span style="color:#e67e22;"><strong>테라</strong></span>부터 시작해 번갈아가며 아래 과정을 반복한다.</p>

<ol>
<li>남아있는 사과 중 몇 개를 골라 반대쪽 사과와 위치를 바꾼다. 시작 위치에서 반시계 방향으로 $i$번째 사과를 고른 경우 시작 위치에서 시계 방향으로 $i$번째 사과와 위치를 바꾼다. 사과를 하나도 고르지 않을 수도 있다.</li>
<li>시작 위치에 있는 사과를 테이블에서 가져가고 반시계 방향으로 다음 사과가 시작 위치가 된다.</li>
</ol>

<p>모든 사과를 가져가면 게임이 종료되며, 가져간 사과의 맛의 합이 더 큰 사람이 승리한다. <strong>맛의 합이 동일하다면 <span style="color:#8e44ad;"><strong>루루</strong></span>가 승리한다.</strong> <span style="color:#e67e22;"><strong>테라</strong></span>와 <span style="color:#8e44ad;"><strong>루루</strong></span>는 항상 $($자신이 가져간 사과의 맛의 합$) - ($상대가 가져간 사과의 맛의 합$)$을 최대화 하기 위해 최선을 다한다. 테이블에 있는 사과의 맛이 주어질 때 누가 승리할지 구해보자.</p>

### 입력 

 <p>첫째 줄에 사과의 개수 $N$이 주어진다. $(1 \le N \le 5\ 000)$</p>

<p>둘째 줄에 사과의 맛을 나타내는 $N$개의 정수 $V_1,V_2,\cdots,V_N$이 반시계 방향 순서대로 공백으로 구분되어 주어진다. $(0 \le V_i \le 10^9)$</p>

### 출력 

 <p><span style="color:#e67e22;"><strong>테라</strong></span>가 승리한다면 <code><span style="color:#e74c3c;">Terra</span></code>, <span style="color:#8e44ad;"><strong>루루</strong></span>가 승리한다면 <span style="color:#e74c3c;"><code>Lulu</code></span>를 출력한다.</p>

