# [Bronze I] Brownies vs. Candies vs. Cookies - 25934 

[문제 링크](https://www.acmicpc.net/problem/25934) 

### 성능 요약

메모리: 112520 KB, 시간: 128 ms

### 분류

사칙연산, 구현, 수학, 시뮬레이션

### 제출 일자

2024년 11월 19일 17:08:52

### 문제 설명

<p>Everyone is welcome to the UCF Programming Team practices, and many students take advantage of this opportunity. The main benefit is that these students improve their problem solving and programming skills. Another benefit is that the students enjoy the refreshments Dr. Orooji brings every week! Dr. O usually brings candies but sometimes he brings cookies or brownies. Brownies are very popular and don’t usually last long, so Dr. O has to come up with some clever trick to make the brownies last longer (so that the students stay for the entire practice!). Well, the easiest solution is to cut the brownies in half; that will double the number of brownies.</p>

<p>Given the original number of brownies and the students wanting brownies, you are to keep track of the brownie count as Dr. O cuts them in half.</p>

### 입력 

 <p>The first input line contains a positive integer, n, indicating the number of programming team practices. This is followed by the data for these practices. The first input line for each practice contains two integers (separated by a space): the number of students (between 1 and 30 inclusive) in the practice and the number of brownies (between 60 and 600 inclusive) Dr. O has brought that day. The next input line for the practice contains a positive integer, m, indicating how many groups of students approach the refreshment table to take brownies. This is followed by the number of students in each group, one number per line. Assume that the input values are valid, e.g., the number of students in a group will be at least 1 and it will not be greater than the number of students in the practice.</p>

<p>If a group of students is approaching the refreshment table and Dr. O notices that the number of remaining brownies is less than or equal to the number of students in the group, Dr. O cuts the brownies in half to be sure they won’t be all gone after each student in the group grabs one brownie. Note that, if needed, Dr. O will cut the brownies more than once (as many times as needed). For example, if there are 3 brownies left and 24 students are approaching the table, Dr. O has to cut the brownies four times (3 → 6 → 12 → 24 → 48) to be sure the brownies won’t be all gone after each student in the group grabs one.</p>

### 출력 

 <p>At the beginning of each practice, output “Practice #p: s b” where p is the practice number (starting with 1), s is the number of students in this practice, and b is the number of brownies. Then, on each of the following output lines, print the number of students in a group approaching the refreshment table and the number of brownies left after each of these students has grabbed one brownie (note that cutting in halves may occur before grabbing). Leave a blank line after the output for each practice.</p>

