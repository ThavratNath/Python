''' 
1. start
    2. s = 1, e =100, correct = random
    3. guess
    4. while True:
    if guess == correct:
        then Conglation!! You won.
        break
    else:
        if guess < correct:
            s = guess
            help = ciel ((s+100)/2)
        else:
            e = guess
            help = ciel((s + e)/2)   (ciel: number we increase. Ex: 3.4 > 4)
'''

'''
2. 

1. Start
2. input num
3. define reverse = 0, remain
4. while num > 0:   // num = 123
remain = num%10     // reverse = 321
reverse = reverse * 10 + remain 
num = num// 10


This algorithm reverses the digits of a given number. Let me break down the steps to make it easier to understand:

### Example: Reversing the Number 123

1. **Start**
   - The algorithm begins with an input number, which in this case is `123`.

2. **Input num**
   - The user provides the input number. Here, `num = 123`.

3. **Define reverse = 0, remain**
   - We initialize `reverse` to `0`. This will eventually hold the reversed number.
   - `remain` is used to store the last digit of the current number (`num`).

4. **While num > 0 (Keep repeating these steps as long as `num` is greater than 0):**
   - We perform the following steps to reverse the digits:

   **First Iteration** (`num = 123`):
   - `remain = num % 10`  
     - This step calculates the last digit of `123`, which is `3` (`123 % 10 = 3`).
   - `reverse = reverse * 10 + remain`  
     - We update `reverse`. Initially, `reverse = 0`, so now it becomes `0 * 10 + 3 = 3`.
   - `num = num // 10`  
     - This step removes the last digit from `123`, leaving us with `12` (`123 // 10 = 12`).

   **Second Iteration** (`num = 12`):
   - `remain = num % 10`  
     - The last digit of `12` is `2` (`12 % 10 = 2`).
   - `reverse = reverse * 10 + remain`  
     - Update `reverse` to `3 * 10 + 2 = 32`.
   - `num = num // 10`  
     - Remove the last digit from `12`, resulting in `1` (`12 // 10 = 1`).

   **Third Iteration** (`num = 1`):
   - `remain = num % 10`  
     - The last digit of `1` is `1` (`1 % 10 = 1`).
   - `reverse = reverse * 10 + remain`  
     - Update `reverse` to `32 * 10 + 1 = 321`.
   - `num = num // 10`  
     - Now `num` becomes `0` (`1 // 10 = 0`), and the loop ends.

5. **End**
   - The reversed number, stored in `reverse`, is `321`.

### Key Idea
The algorithm works by repeatedly extracting the last digit of the number and adding it to 
the reverse in a new position (by multiplying the reverse by 10). This shifts the digits and builds 
the reversed number step by step.

'''
'''2'''

# a = 0
# b = 1
# next = 0
# n = 3
# print(a, b, end =" ")
# for i in range (n):
#     next = a + b
#     print(next, end =" ")
#     a = b 
#     b = next


'''3

20 - 6

'''



'''
Start with two variables, a = 0 and b = 1.
Add them together to get the next number in the sequence.
Update a to the value of b and b to the newly calculated number.
Repeat the process for as many terms as needed.
In Python, this can be written as:

python
Copy code
a, b = 0, 1
for _ in range(10):  # Generate the first 10 terms
    print(a)
    a, b = b, a + b
    a
'''


'''Oct 26, 2024


Flowchart Symbol and Meaning: A Complete Guide: Used this flow chart in the Algorithsm. We create software after great a software. 

- Oval: refer to the start and the end. 

- retangle: denote the process
- arrow: indicate the flow between steps
- diamond: check the condition: signify a poit that requires Yes/No
- Pallenlogram: used for the output orinput operation

'''

'''Example: 
a, b

>> 
1. start 
2. input(a,b)
if a>b:
    output a
else:
    output b
3. stop'''

'''Ex 2. Sum 1--> n
1. Start
2. Input n 
3. Sum = 0
4. for i in range(1,n+1):
    Sum = Sum + i
5. output sum
6. stop

'''
