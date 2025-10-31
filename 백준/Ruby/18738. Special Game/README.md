# [Ruby III] Special Game - 18738 

[문제 링크](https://www.acmicpc.net/problem/18738) 

### 성능 요약

메모리: 110984 KB, 시간: 128 ms

### 분류

애드 혹, 게임 이론

### 제출 일자

2025년 10월 31일 23:43:15

### 문제 설명

<p>Dmytryk and Petro are playing the following game. They have 2n cards with integer values 1 to 2n, all values are different. At the beginning of the game, each player has exactly n cards.</p>

<p>A total of n rounds occur, and Dmytryk makes the first turn in the first round. In each round, the player that makes the first turn takes out one of his cards. Then the other player (seeing the first player’s card) takes out one of his cards. The player that has the largest card value wins the round and takes the first turn in the next round. Both cards are then removed from the game.</p>

<p>There is an additional rule: in each round, if the player making the second turn has a card with bigger value than the other player’s card he sees, he is obliged to take out one of such cards.</p>

<p>The objective of each player is to maximize the number of rounds he wins. Find the maximum number of turns Dmytryk can win, if both players play optimally.</p>

### 입력 

 <p>The first line contains a single integer n (1 ≤ n ≤ 1000). The second line contains n integers — Dmytryk’s cards. The third line contains Petro’s cards.</p>

### 출력 

 <p>The answer to the problem.</p>

