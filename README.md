# Python Modules
- Python Library and Built in Functions
- What is pip and how do we use it 
- APIs with python

- Built in functions help us accelerate our development of software

## Task
- get user input of a float number
- check if the number is lower than .50 then round the figure to lower end
- check if the number is greater than .51 then round the figure to higher end

example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end

## Syntax
First we must `import` the necessary modules from python, in this case `math`

```python
import math
```
You can use the built in method `round(float, decimal_to_round_to)`, which already has this control flow.
```python
# Take user's input
number = input('What number would you like to round?')
# check that the user gave us a float
if float(number) % 1 == 0 
    number = (input('You must enter a float, please try again.'))
# the built in round function already has this control flow
else:
    print(round(float(number),0))
```
If you were hell-bent on doing the flow yourself, perhaps you want different cut off points for rounding up / down, you can use the following syntax:

```python
...
else:
    if number % 1 < 0.5:
        print(math.floor(number))
    else:
        print(math.ceil(number))
```