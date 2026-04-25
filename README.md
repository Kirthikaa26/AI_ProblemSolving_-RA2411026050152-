#  AI MINI PROJECT PORTFOLIO 

This repository contains two AI-based projects developed using Python and Streamlit:

1.  AI Chatbot System  
2.  Traveling Salesman Problem (TSP) Solver  

---

##  Live Project Links

 AI Chatbot System:  
https://ai-chatbot-logic-engine.streamlit.app/

 TSP Solver:  
https://tspplanner.streamlit.app/ 

## Sample Output

![Chatbot Output](output.png)
![TSP Output](output.png)


## Project 1: AI Chatbot System

### Problem Statement

Design and develop a simple AI chatbot that can interact with users and respond to basic queries using predefined rules. The system should simulate human-like conversation using pattern matching techniques.

---
##  Features
- Rule-based AI responses  
- Fast interaction  
- Beginner-friendly AI logic  
- Streamlit web interface


---
### Algorithm Used

* Rule-Based AI (Pattern Matching)
* Conditional Logic (if-else statements)
* Keyword Matching

---

### Execution Steps

1. User enters a message in the Streamlit interface.
2. The input is converted to lowercase.
3. System checks for matching keywords in predefined rules.
4. Appropriate response is selected using conditional logic.
5. The chatbot displays the response instantly.


---

### Sample Output

```
User: Hello
Bot: Hi! How can I help you today?

User: What is AI?
Bot: AI is a branch of computer science that enables machines to simulate human intelligence.
```

---

## Project 2: Traveling Salesman Problem (TSP) Solver

###  Problem Statement

Develop a system to find the shortest possible route that visits a set of cities exactly once and returns to the starting point. The solution should compute the optimal path based on distance.

---

##  Features
- User-defined city coordinates  
- Finds optimal shortest path  
- Calculates minimum distance  
- Interactive Streamlit UI 

###  Algorithm Used

* Brute Force Approach
* Permutations using itertools
* Distance Calculation (Euclidean Distance)

---

###  Execution Steps

1. User inputs city coordinates.
2. System generates all possible permutations of city paths.
3. Calculates total distance for each path.
4. Compares distances to find the shortest route.
5. Displays the optimal path and minimum distance.

---

###  Sample Output

```
Input Cities:
City 1 → (0,0)
City 2 → (2,3)
City 3 → (5,4)
City 4 → (1,1)

Best Route:
0 → 3 → 1 → 2

Minimum Distance:
8.76
```

---

##  Tech Stack

* Python
* Streamlit
* Rule-Based Logic
* Brute Force Optimization
* itertools



 
