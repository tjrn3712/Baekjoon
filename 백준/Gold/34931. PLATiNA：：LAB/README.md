# [Gold II] PLATiNA::LAB - 34931 

[문제 링크](https://www.acmicpc.net/problem/34931) 

### 성능 요약

메모리: 206700 KB, 시간: 260 ms

### 분류

구현, 애드 혹, 시뮬레이션, 홀짝성

### 제출 일자

2025년 12월 25일 04:34:21

### 문제 설명

<p>플래티넘은 은하 대학교의 교수로 자신의 이름을 딴 연구소인 플래티나 랩(PLATiNA::LAB)에서 미생물 연구를 하고 있다.</p>

<p>플래티넘은 최근에 미생물 <span style="color:#e74c3c;"><code>A</code></span>와 <span style="color:#e74c3c;"><code>B</code></span>에 대해서 연구를 하고 있는데, 두 종류의 미생물을 일렬로 배치하고 관찰하면 한 시간마다 미생물에 재미있는 변화가 일어난다는 사실을 알게 되었다.</p>

<ul>
<li>만약 <span style="color:#e74c3c;"><code>A</code></span>의 양 옆에 <span style="color:#e74c3c;"><code>B</code></span>가 두 마리 있었다면 한 시간 뒤 <span style="color:#e74c3c;"><code>B</code></span>로 변하게 된다.</li>
<li>만약 <span style="color:#e74c3c;"><code>B</code></span>의 양 옆에 <span style="color:#e74c3c;"><code>A</code></span>가 두 마리 있었다면 한 시간 뒤 <span style="color:#e74c3c;"><code>A</code></span>로 변하게 된다.</li>
</ul>

<p>예를 들어 플래티넘이 처음에 미생물을 <code><span style="color:#e74c3c;">ABABAAA</span></code> 순서대로 놓았다면 1시간 뒤에는 <span style="color:#e74c3c;"><code>AABAAAA</code></span>가 되고, 2시간 뒤에는 <span style="color:#e74c3c;"><code>AAAAAAA</code></span>가 된다.</p>

<p>대학원생 브론즈는 플래티넘의 지시에 따라 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 미생물을 일렬로 배치한 후에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>시간이 지나고 나서 변화한 상태를 기록해야 했지만, 잠에 드는 바람에 결과를 기록하지 못했다. 브론즈를 위해 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>시간이 지난 후의 미생물의 상태를 대신 기록해 주자.</p>

### 입력 

 <p>첫째 줄에 미생물의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>과 시간 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>가 공백으로 구분되어 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-script></mjx-msup><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>T</mi><mo>≤</mo><mi>N</mi><mo>≤</mo><msup><mn>10</mn><mn>6</mn></msup><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1\leq T\leq N\leq 10^6)$</span> </mjx-container></p>

<p>둘째 줄에 미생물의 배치를 의미하는 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 문자열이 주어진다. 이 문자열은 <code><span style="color:#e74c3c;">A</span></code>와 <code><span style="color:#e74c3c;">B</span></code>로만 이루어져 있다.</p>

### 출력 

 <p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>시간 뒤의 미생물의 상태를 출력한다.</p>

