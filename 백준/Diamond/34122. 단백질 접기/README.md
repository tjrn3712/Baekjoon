# [Diamond II] 단백질 접기 - 34122 

[문제 링크](https://www.acmicpc.net/problem/34122) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

애드 혹, 해 구성하기

### 제출 일자

2025년 8월 17일 07:27:13

### 문제 설명

<p>2024년 노벨 화학상은 단백질의 구조를 분석, 설계 및 예측할 수 있는 인공지능 모델을 개발한 연구자에게 수여되었다.</p>

<p>단순한 모형을 가정하고 단백질 접힘 문제를 풀어보자.</p>

<p>이 문제에서 사용할 단백질을 다음과 같은 단순한 모형으로 모델링하자.</p>

<ul>
	<li><strong>구성</strong>: 단백질은 다수의 아미노산 구슬이 끈으로 순서대로 연결된, 가지가 없는 하나의 사슬이다.</li>
	<li><strong>배치</strong>: 각 구슬은 2차원 정사각형 그리드 위의 점에 위치할 수 있다.</li>
	<li><strong>연결</strong>: 각 구슬을 잇는 끈의 길이는 그리드 간격과 동일하다. 끈으로 연결된 두 구슬은 상하좌우로 인접해야 한다.</li>
	<li><strong>아미노산 종류</strong>: 아미노산 구슬의 종류는 A, B, C 3가지다.</li>
	<li>각 아미노산 구슬은 겹치지 않아야 한다.</li>
</ul>

<p>예를 들어, 5개의 아미노산 구슬로 구성된 단백질1, 2와 10개의 아미노산 구슬로 구성된 단백질3은 각각 다음과 같은 모양을 가질 수 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/2fb0ebe6-c915-4f89-ad6a-8df709d7ebd1/-/preview/" style="width: 930px; height: 380px;"></p>

<p>서로 인접한 두 아미노산 구슬 쌍은 연결 상태와 구슬의 종류에 따라 서로 다른 에너지를 가진다. 각 구슬 쌍의 에너지는 다음과 같이 가정한다.</p>

<ul>
	<li><strong>연결된 상태</strong>: 에너지 값은 구슬의 종류와 연결 방식에 따라 결정된다.</li>
</ul>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/c0c88967-a88d-48af-922d-e22c6456f68a/-/preview/" style="width: 427px; height: 167px;"></p>

<ul>
	<li><strong>에너지 합산</strong>: 전체 단백질의 에너지는 모든 인접 구슬 쌍의 에너지 합으로 계산된다.</li>
</ul>

<p>위에서 예시로 나온 단백질들은 각각 다음과 같이 전체 에너지가 각각 +1, +5, +2로 계산된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/24466946-fe0d-48ba-8992-c992e327430d/-/preview/" style="width: 923px; height: 377px;"></p>

<p>아미노산 구슬 <strong>111개</strong>가 연결된 단백질을 2차원 정사각형 그리드에 배치하고, 각 구슬의 종류를 결정하여 모든 인접한 구슬 쌍의 에너지 합이 <strong>최소</strong>가 되도록 해야 한다. 점수는 모든 인접한 구슬 쌍의 에너지 합 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D438 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$E$</span></mjx-container>에 대해 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c6D"></mjx-c><mjx-c class="mjx-c61"></mjx-c><mjx-c class="mjx-c78"></mjx-c></mjx-mo><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D438 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo data-mjx-texclass="OP" movablelimits="true">max</mo><mo stretchy="false">(</mo><mo>−</mo><mi>E</mi><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\max(-E, 0)$</span></mjx-container>으로 계산된다. 즉, 에너지 합이 낮을 수록 점수가 높아진다.</p>

<p>정답 제출을 위해 총 <strong>221개의 문자</strong>를 제출해야 한다.</p>

<ol>
	<li><strong>아미노산 종류 (첫 111개 문자)</strong>

	<ul>
		<li>각 문자는 <strong>A</strong>, <strong>B</strong>, <strong>C</strong> 중 하나로 아미노산 구슬의 종류를 결정한다.</li>
		<li>예: <code>ABCABCABC...</code></li>
	</ul>
	</li>
	<li><strong>구슬 배치 방향 (마지막 110개 문자)</strong>
	<ul>
		<li>각 문자는 <strong>U</strong>, <strong>D</strong>, <strong>R</strong>, <strong>L</strong> 중 하나로 다음 구슬의 방향을 나타낸다.</li>
		<li>예: <code>URDDDLLL...</code></li>
	</ul>
	</li>
</ol>

<p>다음은 아미노산 구슬이 10개인 단백질일 때, 이 단백질을 나타내는 답안이다. 실제로는 111개의 아미노산 구슬에 대한 답안을 제출해야함에 주의하자.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/143508b8-e4e5-4f0c-a642-b099c359a69c/-/preview/" style="width: 292px; height: 288px;"></p>

### 입력 

 Empty

### 출력 

 Empty

