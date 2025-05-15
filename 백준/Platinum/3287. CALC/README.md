# [Platinum V] CALC - 3287 

[문제 링크](https://www.acmicpc.net/problem/3287) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

문자열, 애드 혹, 해 구성하기, 파싱

### 제출 일자

2025년 5월 16일 00:47:59

### 문제 설명

<p>Hal has a symbolic calculator whose memory is organised as a list that can have at most 100 elements. Each element can contain an arithmetic expression. The calculator understands following commands:</p>

<ul>
	<li>HASH - If the first element of a list contains expression s and the second element contain expression t then this command removes those two elements from list and creates new first element containing expression (t#s).</li>
	<li>DOLLAR - If the first element of a list contains expression s and the second element contain expression t then this command removes those two elements from list and creates new first element containing expression (t$s).</li>
	<li>SWAP - Exchanges the first and the second element of a list.</li>
	<li>DROP - Removes the first element from a list.</li>
	<li>DUP - New first element is created and expression from the second element of list (which was the first before the creation of new element) is copied to it.</li>
	<li>ROT - Rotates the first four elements of list so that the first becomes the second, the second becomes the third, the third becomes the fourth and the fourth becomes the first.</li>
</ul>

<p>List with two elements is given. The first element contains A and the second element contains B. </p>

<p>Write a program which will for given expression e generate a sequence of commands for Hal’s calculator that will, starting with given list and executing all commands of the sequence without any error as a result leave a list whose first and only element contain expression e.</p>

<p>An error occurs if list gets too long (attempt to add 101st element) or if there are not enough elements needed to perform a command. Commands DUP and DROP require that the first element has an expression; commands HASH, DOLLAR and SWAP require that the first two elements have expressions; command ROT requires that the first four elements of a list have expressions.</p>

<p>Program should generate any sequence of commands that as result leaves given expression. Number of commands in a sequence should not exceed 10000.</p>

### 입력 

 <p>The first and only line of input file contains a given expression which is a sequence of characters A, B, #, $, (,) and nothing else (not even space characters).</p>

<p>Length of expression will always be 100 or less.</p>

<p>There will always be a solution to test data.</p>

### 출력 

 <p>The output file should contain a sequence of commands generating given expression. Each line should contain one command.</p>

<p>Note: a solution needs not to be unique.</p>

