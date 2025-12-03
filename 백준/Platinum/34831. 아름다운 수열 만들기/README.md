# [Platinum V] 아름다운 수열 만들기 - 34831 

[문제 링크](https://www.acmicpc.net/problem/34831) 

### 성능 요약

메모리: 120340 KB, 시간: 120 ms

### 분류

애드 혹, 해 구성하기

### 제출 일자

2025년 12월 3일 21:05:12

### 문제 설명

<p>형진이는 길이 $N$의 <strong>아름다운 수열</strong>을 만들고 싶다.</p>

<p>수열 $A_1,A_2,\dots ,A_N$에 대해서, 다음 조건을 모두 만족하면 이를 <strong>아름다운 수열</strong>이라고 부른다.</p>

<ul>
<li>수열의 모든 원소는 <span style="color:#e74c3c;"><code>0</code></span>, <span style="color:#e74c3c;"><code>1</code></span>, <span style="color:#e74c3c;"><code>2</code></span>중 하나이다.</li>
<li>인접한 모든 원소는 서로 다르다.</li>
<li><span style="color:#e74c3c;"><code>0</code></span> 원소들의 모든 인접한 원소들의 차이의 총합과, <span style="color:#e74c3c;"><code>1</code></span> 원소들의 모든 인접한 원소들의 차이의 총합과, <span style="color:#e74c3c;"><code>2</code></span> 원소들의 모든 인접한 원소들의 차이의 총합은 같다.</li>
</ul>

<p>예를 들어, $[0,1,2,0,1,2]$은 <strong>아름다운 수열</strong>이다. 수열의 모든 원소가 <span style="color:#e74c3c;"><code>0</code></span>, <span style="color:#e74c3c;"><code>1</code></span>, <span style="color:#e74c3c;"><code>2</code></span>중 하나이며 인접한 모든 원소는 서로 다르다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e1ae1c33-e44f-44c2-89be-e3b124b02b90/-/preview/" style="height: 156px; width: 400px;"></p>

<p>또한, <span style="color:#e74c3c;"><code>0</code></span> 원소들의 인접한 차이의 총합을 구해보면, 우선 첫 번째 원소 <span style="color:#e74c3c;"><code>0</code></span>은 왼쪽 원소는 없고 오른쪽 원소와의 인접한 차이가 $\vert 0-1\vert =1$이므로 $1$을 기여하고, 네번째 원소 <span style="color:#e74c3c;"><code>0</code></span>은 $\vert 2-0\vert +\vert 0-1\vert =3$이므로 $3$을 기여하여, <span style="color:#e74c3c;"><code>0</code></span> 원소들의 인접한 차이의 총합은 $4$이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/9eb4530c-dba3-4273-b56b-5de3f6bd7840/-/preview/" style="height: 177px; width: 800px;"></p>

<p>비슷하게 <span style="color:#e74c3c;"><code>1</code></span> 원소들의 인접한 차이의 총합은 $\vert 0-1\vert +\vert 1-2\vert =2$인 원소 하나와 $\vert 0-1\vert +\vert 1-2\vert =2$인 원소 하나가 있으므로 총 $4$이며, <span style="color:#e74c3c;"><code>2</code></span> 원소들의 인접한 차이의 총합은 $\vert 1-2\vert +\vert 2-0\vert =3$인 원소 하나와 $\vert 1-2\vert =1$인 원소 하나가 있으므로 총 $4$이다. 따라서 <span style="color:#e74c3c;"><code>0</code></span>, <span style="color:#e74c3c;"><code>1</code></span>, <span style="color:#e74c3c;"><code>2</code></span>원소들의 모든 인접한 원소들의 차이의 총합은 서로 같다.</p>

<p>한편, $[0,0,0]$은 <strong>아름다운 수열</strong>이 아니다. <span style="color:#e74c3c;"><code>0</code></span>, <span style="color:#e74c3c;"><code>1</code></span>, <span style="color:#e74c3c;"><code>2</code></span>원소들의 모든 인접한 원소들의 차이의 총합은 같으나, 인접한 원소들 중 서로 같은 것이 존재하기 때문이다.</p>

<p>조건을 만족하도록 하는 길이 $N$의 <strong>아름다운 수열</strong>을 구성할 수 있는지 판단하고, 구성할 수 있다면 그러한 수열 $A_1,A_2,\dots ,A_N$을 구성하여라.</p>

### 입력 

 <p>첫째 줄에 수열의 길이를 나타내는 정수 $N$이 주어진다. ($3\le N\le 100\, 000$)</p>

### 출력 

 <p>첫째 줄에 조건을 만족하도록 하는 길이 $N$의 아름다운 수열을 구성할 수 있다면 <span style="color:#e74c3c;"><code>Yes</code></span>를, 없다면 <span style="color:#e74c3c;"><code>No</code></span>를 출력한다.</p>

<p>길이 $N$의 아름다운 수열을 구성할 수 있다면, 둘째 줄에 조건을 만족하는 수열 $A_1,A_2,\dots ,A_N$을 공백을 사이에 두고 출력한다.</p>

