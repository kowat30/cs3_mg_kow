# INSTRUCTIONS

| Activity 2: Code Quality Assessment  Instructions: This activity will be done in pairs.  Find your partner or work with your seatmate The activity could be found in Annex C: Code Quality Assessment Form Create a copy of the Code Quality Assessment Form in your Github portfolio and name it as code\_review\_section\_ln[.md](http://codereviewSectionLN.md)             Here are the short guides on how to use Markdown:              [https://www.markdowntutorial.com/](https://www.markdowntutorial.com/)             [https://daringfireball.net/projects/markdown/basics](https://daringfireball.net/projects/markdown/basics)             [https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/)             [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/) Both of you will create the .md file, but identify in the .md file who is your partner. Given two algorithms, use this worksheet to select the better solution to the problem of Searching for a Number in a Sorted List by answering the questions from 1 to 5\.  Note: Divide the assessment between your partner and then agree on the final answer on which of the two algorithms is the best. A checklist for each number is given to guide you in answering each question.   Create a [README.md](http://README.md) file (to be also uploaded in your GitHub) to have the link to your file and submit the live server link  and the .git repository link in the submission bin found in KhuB. |
| :---- |

**NOTE:** 

1. If, due to time constraints, you are unable to create and finish your Markdown file, please make a copy of this document, enter your answers, and submit it to the Activity \#2 submission bins in Khub.

2. However, I would appreciate it if you would submit a Markdown file uploaded to your GitHub repository.

# Annex C

### 

### **Annex C**

**Code Quality Assessment Worksheet**

**Section: Magnesium						Score:\_\_\_\_\_\_\_\_\_\_\_\_**  
**C\# / Name: Ashley Paclibar & Andrea Kow		Date: 8/26/26**

**Instructions:**

**The problem: Search for a Number in a Sorted List**

**For example: Both algorithms could search:**   
numbers \= \[5, 12, 18, 23, 31, 47, 56, 68, 74, 90\]  
target \= 47

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| def linear\_search(numbers, target):    *for* i *in* range(len(numbers)):        *if* numbers\[i\] \== target:            *return* i    *return* \-1   | def binary\_search(numbers, target):    low \= 0    high \= len(numbers) \- 1     *while* low \<= high:        middle \= (low \+ high) // 2         *if* numbers\[middle\] \== target:            *return* middle        *elif* numbers\[middle\] \< target:            low \= middle \+ 1        *else*:            high \= middle \- 1     *return* \-1   |

## 

## 

## 

## 

## **Questions with Checklists**

### **1\. Efficiency**

Which algorithm is faster when the list of numbers is very large? Why?

In a long list, Implementation 2 would be faster. Since it is binary search, it continuously halves the list making operations faster. However, for linear search, it goes through each element one by one making it less efficient and not as fast.


**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? | How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? |

**2\. Readability**

Which algorithm is easier to understand at first glance? What makes it clearer?

Implementation 1 uses simpler logic and a singular for loop that checks every item from left to right. The execution is straightforward and concise.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? | How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? |

### 

### **3\. Maintainability**

If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?

Implementation 1 would be easier to update. Since it’s direct and concise, there is a lower risk of bugs and fewer moving parts and it relies on a single variable (i). Compared to implementation 2, which has risks of errors due to boundary logic.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? | Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? |

### 

### **4\. Testability**

Which algorithm is easier to test with different inputs? Why?

Implementation 1 is easier to test because it runs predictably on small lists of any order, uses only one simple condition, and follows a clear, step-by-step path. In contrast, implementation 2 requires pre-sorted data and complex multi-branch pointer logic.


**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? | Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? |

### **5\. Reliability and Input Validation**

What should the algorithm check to avoid errors when receiving input from a user?

To avoid errors, the algorithm should check if the list is empty, ensure input has the correct data type, and verify the list is sorted. It must also handle unusual or missing targets gracefully to prevent crashes.


**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Linear Search? | Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Binary Search? |

### 

### **6\. Final Answer**

Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.

For this problem, implementation 1 is the better choice for this problem because of its simplicity, ease of testing, and ability to handle unsorted lists directly. It is less likely to have errors during modification due to its preciseness. However, implementation 2 becomes more suitable when working with very large datasets that are already sorted, where its superior search speed outweighs the added complexity.
