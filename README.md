# Python Modules
- Python Library and Built in Functions
- What is pip and how do we use it 
    - pip is a package manager, we use it to install / use packages in python such as requests
    - syntax: pip install name_of_package
- APIs with python
    - https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/


- Built in functions help us accelerate our development of software
- Example: creating a customised function. 
    ```python
    import sys # import module
    def system_path():
        print(sys.path) # you can use the om    

## Requests

- Local host makes an API call to a www server
  - To find out if the web is live
  - To handle the user as per the response from the web
  - Meeting the user's expectation
  - ![](https://media.discordapp.net/attachments/767793850529087489/775332176240574494/unknown.png)
## Task
- get user input of a float number
- check if the number is lower than .50 then round the figure to lower end
- check if the number is greater than .51 then round the figure to higher end

example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end

### Syntax
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