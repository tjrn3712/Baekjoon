# [Platinum I] 돌 게임 - 32659 

[문제 링크](https://www.acmicpc.net/problem/32659) 

### 성능 요약

메모리: 113768 KB, 시간: 128 ms

### 분류

게임 이론, 스프라그–그런디 정리

### 제출 일자

2024년 11월 14일 21:10:02

### 문제 설명

<p>크기가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>×</mo><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \times N$</span></mjx-container>인 게임판 위의 짝수 개의 칸에 흑돌과 백돌이 같은 개수로 번갈아서 배치되어 있다.</p>

<p>이 게임판을 이용해 게임을 하는데 규칙은 다음과 같다.</p>

<ul>
	<li>선공과 후공이 한 턴씩 번갈아가면서 게임을 진행한다. 선공은 흑, 후공은 백으로 게임을 진행한다.</li>
	<li>두 플레이어는 자신의 턴에 자신의 색깔의 돌을 하나 선택하여 좌우로 원하는 만큼 움직일 수 있다. 돌을 움직이지 않을 수는 없으며, 다른 돌을 뛰어넘거나 이미 돌이 있는 칸으로 움직이는 것은 불가능하다.</li>
	<li>자신의 턴에 돌을 움직일 수 없는 플레이어가 게임에서 패배한다.</li>
</ul>

<p>두 플레이어가 최선의 전략으로 게임을 할 때 누가 이길지 알아보자. 만약 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mn>100</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^{100}$</span></mjx-container> 턴이 지나도 승부가 결정되지 않으면 무승부로 판정한다.</p>

### 입력 

 <p>첫 번째 줄에 게임판의 상태를 나타내는 문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>2</mn><mo>≤</mo><mo data-mjx-texclass="ORD" fence="false" stretchy="false">|</mo><mi>S</mi><mo data-mjx-texclass="ORD" fence="false" stretchy="false">|</mo><mo>≤</mo><mn>5</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(2 \le \vert S\vert \le 5\,000)$</span> </mjx-container></p>

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container> 는 <span style="color:#e74c3c;"><code>B</code></span>, <span style="color:#e74c3c;"><code>W</code></span>, <span style="color:#e74c3c;"><code>.</code></span>으로만 구성되어 있으며, <span style="color:#e74c3c;"><code>B</code></span>는 흑돌, <span style="color:#e74c3c;"><code>W</code></span>는 백돌, <span style="color:#e74c3c;"><code>.</code></span>은 빈칸을 의미한다. 흑돌과 백돌은 적어도 하나 이상 있음이 보장된다.</p>

### 출력 

 <p>첫 번째 줄에 선공이 이긴다면 <span style="color:#e74c3c;"><code>Win</code></span>, 선공이 진다면 <span style="color:#e74c3c;"><code>Lose</code></span>를 출력한다. 만약 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mn>100</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^{100}$</span></mjx-container> 턴이 지나도 승부가 결정되지 않으면 <span style="color:#e74c3c;"><code>Draw</code></span>를 출력한다.</p>

