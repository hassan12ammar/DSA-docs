# Data Structures and Algorithms (DSA)
Data Structures and Algorithms (DSA) form the foundation of computer science and software development. DSA encompasses the study of organizing and manipulating data efficiently, along with designing and analyzing algorithms for problem-solving.

In DSA, **Data Structures** refer to the different ways of organizing and storing data to facilitate efficient operations such as insertion, deletion, and searching. Examples of common data structures include arrays, linked lists, stacks, queues, trees, graphs, and hash tables.

On the other hand, **Algorithms** are step-by-step procedures or instructions used to solve problems or perform computations. Algorithms utilize data structures and define the logic to process and transform data. They aim to optimize time and space complexity to achieve efficient and scalable solutions.

DSA not only improves your chances of success in **MAANG** (Meta, Amazon, Apple, Netflix, Google) interviews but also prepares you for a wide range of technical roles in the industry. It demonstrates your ability to solve complex problems, design efficient algorithms, and build scalable software systems – all of which are highly valued by MAANG companies and other top tech employers.nd scalable solutions.

# Practice makes perfect 
<i>"Practice makes perfect."</i> is a well-known adage that holds true for DSA, software development and problem-solving, especially in the context of technical interviews. **LeetCode**, an online platform, offers a wide range of coding problems and a supportive community for practicing and honing your skills. By regularly practicing on LeetCode, you can improve your problem-solving abilities, enhance your algorithmic thinking skills, gain exposure to interview-style questions, manage time efficiently, leverage the learning resources and community, track your progress, and effectively prepare for technical interviews. However, it is important to supplement LeetCode practice with a solid understanding of fundamental concepts and theory to develop a well-rounded skill set for real-world software development.

* before an interview, you should feel comfortable solving any **medium-level problem** in less then **30 minutes** with no help.
* at least **150** problem solved **recintly** (last 3 month)

# Asymptotic analysis
Asymptotic analysis is a method used to analyze the performance of algorithms as the input size approaches infinity. It provides a way to estimate how the runtime or space requirements of an algorithm grow with the input size. Notations such as O (Big-O), Ω (Big-Omega), and Θ (Big-Theta) are used to describe the upper, lower, and tight bounds of the algorithm's complexity.

## Notations
* O - “Big-O”     notation for **upper** bound of f(N) 
* Ω - “Big-Omega” notation for **lower** bound of f(N)
* Θ - “Big-Theta” notation for **tight** bound of f(N), use only if Ω = O

In the field of Data Structures and Algorithms (DSA) as well as software development, **Big O** notation is commonly used to analyze and describe the efficiency and scalability of algorithms. It provides a standardized way to express the worst-case performance of an algorithm in terms of its input size.

TC (Time Complexity): the amount of time taken by an algorithm to run, as a function of the length of the input
SC (Space Complexity): the total amount of memory space used by an algorithm/program, including the space of input values for execution

Can you do better (what is TC and SC of your solution and can you reduce that) is one of the most asked quesions in interviews 

## Order of Growth
* Constant     : **O(1)**
* Logarithmic  : **O(log N)**
* Linear       : **O(N)**
* Polynomial   : **O(Nx)**
* Linearithmic : **O(N log N)**
* Exponential  : **O(xN)**
* Factorial    : **O(N!)**

<center>
  <img alt="Big-O Complexity Chart" src="./Big-O_Complexity_Chart.jpg" width=650>
</center>

<details>
  <summary> <span style="font-size: 1.5em"> Examples </spen> </summary>
Here are some examples to illustrate the different orders of growth:

## Constant Complexity: O(1)
```pyton
def constant_example():
    a = 1
    b = 2
    c = a + b
    return c
```

## Logarithmic Complexity: O(log N)
```pyton
def logarithmic_example(n):
    i = 1
    while i < n:
        i = i * 2
    return i
```

## Linear Complexity: O(N)
```pyton
def linear_example(arr):
    for num in arr:
        print(num)
```

## Polynomial Complexity: O(N^x)
```pyton
def polynomial_example(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i] + arr[j])
```

## Linearithmic Complexity: O(N log N)
```pyton
def linearithmic_example(arr):
    arr.sort()
    for num in arr:
        print(num)
```

## Exponential Complexity: O(x^N)
```pyton
def exponential_example(n):
    if n <= 0:
        return
    else:
        exponential_example(n-1)
```

## Factorial Complexity: O(N!)
```pyton
def factorial_example(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_example(n-1)
```

These examples demonstrate the different orders of growth and how they relate to the input size. By understanding the time complexity of algorithms, we can analyze their efficiency and scalability.
</details>
<br>

# Coding
Naming Convention 
Abstraction (helper methods)
DRY (Do not Repeat Yourself)
YAFNI (You Arn't Going to Need It)
self-descriptive variables or methods
Document (if not **self-descriptive**)

# problem solving
ask clarifying questions
start by brute force than enhance or 
test the solution

# communication
talk (think loud) and why
if you are stuck, summarize then ask if it's clear (ask for hint indirectly, telling them what you have done, and what doesn't work)
use the laptop & whiteboard interchangeably for explain your thought

# Googliness and Leadership (GNL)
Behavioural type
how did you solveed a conflict
past experience and resume (everything about the project like did something good/bad)
feedback & positivity of your work

# DS

<details>
  <summary> Arrays, & Linked Lists </summary>
  
  ## Array
  1. Foo
  2. Bar
     * Baz
     * Qux

  ## Linked List
  1. Foo
  2. Bar
     * Baz
     * Qux


</details>
<br>

<details>
  <summary> Stack, & Queue </summary>
  
  ## Stack
  1. Foo
  2. Bar
     * Baz
     * Qux

  ## Queue
  1. Foo
  2. Bar
     * Baz
     * Qux

</details>
<br>

# A

<details>
  <summary> Sort </summary>
  
  ## Buble sort
  1. Foo
  2. Bar
     * Baz
     * Qux

  ## whatever
  1. Foo
  2. Bar
     * Baz
     * Qux


</details>
<br>

<details>
  <summary> Divide & conqer </summary>
  
  ## Lablaba
  1. Foo
  2. Bar
     * Baz
     * Qux

</details>
<br>

<details>
  <summary> Recursion </summary>
  
  ## Lablaba
  1. Foo
  2. Bar
     * Baz
     * Qux

</details>
<br>
