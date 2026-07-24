import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    hint_level = mo.ui.slider(
        value=0, start=0, stop=3, step=1,
        label="💡 Hint level",
        show_value=True,
    )
    mo.vstack([
        hint_level,
        mo.md("""
    **0** = no hints &nbsp;|&nbsp; **1** = conceptual nudge &nbsp;|&nbsp; **2** = detailed approach &nbsp;|&nbsp; **3** = full solution
        """),
    ])
    return (hint_level,)


@app.cell(hide_code=True)
def _(hint_level, mo):


    _level = hint_level.value

    def show_hints(hint1="", hint2="", solution=""):
        items = {}
        if _level >= 1 and hint1:
            items["💡 Hint 1"] = mo.md(hint1)
        if _level >= 2 and hint2:
            items["💡 Hint 2"] = mo.md(hint2)
        if _level >= 3 and solution:
            items["✅ Solution"] = mo.md(solution)
        if not items:
            return mo.md("")
        return mo.accordion(items)

    return (show_hints,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 1: Hello World

    Write a program that greets the user by printing "Hello, world!" on the screen. Then it prints a message asking the user to enter their name. The program greets the user by name by printing "Hello," followed by the user's name.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise1/)
    """)
    return


@app.function
# TODO: implement
def hello():
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use `print()` to display text and `input()` to get the user's name. Store it in a variable.",
        hint2="Concatenate 'Hello, ' with the user's name using `+` or an f-string. Make sure there's a space after the comma.",
        solution="""```python
    def hello():
        print("Hello,world!")
        print("What is your name?")
        name = input()
        print(f"Hello, {name}")
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import io as _io
    from contextlib import redirect_stdout as _redirect_stdout

    _buf = _io.StringIO()
    _saved_input = input
    globals()["input"] = lambda *a: "Simon"
    try:
        with _redirect_stdout(_buf):
            hello()
    finally:
        globals()["input"] = _saved_input
    _out = _buf.getvalue()

    _results = [
        "Hello,world!\n" in _out,
        "What is your name?\n" in _out,
        "Hello, Simon\n" in _out,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 2: Temperature Conversion

    Write a `convertToFahrenheit()` function with a `degreesCelsius` parameter that returns the temperature in degrees Fahrenheit. Then write a `convertToCelsius()` function with a `degreesFahrenheit` parameter that returns the temperature in degrees Celsius. Formulas: Fahrenheit = Celsius × (9/5) + 32, Celsius = (Fahrenheit - 32) × (5/9).


    [📖 Full description](https://inventwithpython.com/pythongently/exercise2/)
    """)
    return


@app.cell
def _():
    # TODO: implement
    def convertToCelsius(fahrenheit):
        pass

    def convertToFahrenheit(celsius):
        pass

    return convertToCelsius, convertToFahrenheit


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Translate the math formulas directly into Python. Replace × with `*` and use parentheses for grouping.",
        hint2="Each function is just one line: a `return` statement with the formula. `celsius = (fahrenheit - 32) * (5/9)`",
        solution="""```python
    def convertToCelsius(fahrenheit):
        return (fahrenheit - 32) * (5 / 9)

    def convertToFahrenheit(celsius):
        return celsius * (9 / 5) + 32
    ```"""
    )
    return


@app.cell
def _(convertToCelsius, convertToFahrenheit, mo):
    # 📋 Tests - run to check your solution
    _results = [
        convertToCelsius(0) == -17.77777777777778,
        convertToCelsius(180) == 82.22222222222223,
        convertToFahrenheit(0) == 32,
        convertToFahrenheit(100) == 212,
        convertToCelsius(convertToFahrenheit(15)) == 15,
        convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 3: Odd & Even

    Write two functions, `isOdd()` and `isEven()`, with a single numeric parameter named `number`. `isOdd()` returns `True` if `number` is odd and `False` if even. `isEven()` returns `True` if `number` is even and `False` if odd. Both return `False` for numbers with fractional parts. Zero is considered even.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise3/)
    """)
    return


@app.cell
def _():
    # TODO: implement
    def isOdd(num):
        pass

    def isEven(num):
        pass

    return isEven, isOdd


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use the `%` modulo operator. `number % 2` gives 0 for even numbers and 1 for odd.",
        hint2="Return a boolean comparison: `return number % 2 == 1` for isOdd. Think about what happens with negative numbers.",
        solution="""```python
    def isOdd(num):
        return num % 2 == 1

    def isEven(num):
        return num % 2 == 0
    ```"""
    )
    return


@app.cell
def _(isEven, isOdd, mo):
    # 📋 Tests - run to check your solution
    _results = [
        isOdd(1) is True,
        isOdd(3) is True,
        isOdd(2) is False,
        isOdd(0) is False,
        isOdd(-5) is True,
        isOdd(-4) is False,
        isEven(2) is True,
        isEven(0) is True,
        isEven(1) is False,
        isEven(-6) is True,
        isEven(-3) is False,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 4: Area & Volume

    Write four functions: `area()` and `perimeter()` with `length` and `width` parameters, and `volume()` and `surfaceArea()` with `length`, `width`, and `height` parameters. They return the area, perimeter, volume, and surface area respectively. Formulas: area = L × W, perimeter = L + W + L + W, volume = L × W × H, surface area = (L×W×2) + (L×H×2) + (W×H×2).


    [📖 Full description](https://inventwithpython.com/pythongently/exercise4/)
    """)
    return


@app.cell
def _():
    # TODO: implement
    def area(length, width):
        pass

    def perimeter(length, width):
        pass

    def volume(length, width, height):
        pass

    def surfaceArea(length, width, height):
        pass

    return area, perimeter, surfaceArea, volume


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Each function is a one-line `return` statement that translates the math formula into Python operators.",
        hint2="Surface area has three pairs of faces: `(L×W + L×H + W×H) × 2`. Don't forget to multiply by 2!",
        solution="""```python
    def area(length, width):
        return length * width

    def perimeter(length, width):
        return length * 2 + width * 2

    def volume(length, width, height):
        return length * width * height

    def surfaceArea(length, width, height):
        return ((length * width) + (length * height) + (width * height)) * 2
    ```"""
    )
    return


@app.cell
def _(area, mo, perimeter, surfaceArea, volume):
    # 📋 Tests - run to check your solution
    _results = [
        area(10, 10) == 100,
        area(0, 9999) == 0,
        area(5, 8) == 40,
        perimeter(10, 10) == 40,
        perimeter(0, 9999) == 19998,
        perimeter(5, 8) == 26,
        volume(10, 10, 10) == 1000,
        volume(9999, 0, 9999) == 0,
        volume(5, 8, 10) == 400,
        surfaceArea(10, 10, 10) == 600,
        surfaceArea(9999, 0, 9999) == 199960002,
        surfaceArea(5, 8, 10) == 340,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 5: Fizz Buzz

    Write a `fizzBuzz()` function with a single integer parameter named `upTo`. For numbers 1 up to and including `upTo`: print 'FizzBuzz' if divisible by 3 and 5, print 'Fizz' if only divisible by 3, print 'Buzz' if only divisible by 5, otherwise print the number. Print them without newlines separated by spaces.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise5/)
    """)
    return


@app.function
# TODO: implement
def fizzBuzz(upTo: int):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Check divisibility by both 3 AND 5 FIRST, before checking 3 or 5 individually. Use `number % 3 == 0 and number % 5 == 0`.",
        hint2="Use `print(..., end=' ')` to avoid newlines. Loop with `for number in range(1, upTo + 1)`.",
        solution="""```python
    def fizzBuzz(upTo):
        for number in range(1, upTo + 1):
            if number % 3 == 0 and number % 5 == 0:
                print('FizzBuzz', end=' ')
            elif number % 3 == 0:
                print('Fizz', end=' ')
            elif number % 5 == 0:
                print('Buzz', end=' ')
            else:
                print(number, end=' ')
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import io as _io
    from contextlib import redirect_stdout as _redirect_stdout

    def _capture(n):
        buf = _io.StringIO()
        with _redirect_stdout(buf):
            fizzBuzz(n)
        return buf.getvalue().strip()

    _results = [
        _capture(5) == "1 2 Fizz 4 Buzz",
        _capture(15) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz",
        _capture(3) == "1 2 Fizz",
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 6: Ordinal Suffix

    Write an `ordinalSuffix()` function with an integer parameter named `number` that returns a string of the number with its ordinal suffix. For example, `ordinalSuffix(42)` should return '42nd'.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise6/)
    """)
    return


@app.function
# TODO: implement
def ordinalSuffix(number: int):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use the `%` modulo operator. `number % 100` gives the last two digits, `number % 10` gives the last digit.",
        hint2="Check `number % 100 in (11, 12, 13)` first (these are all 'th'). Then check `number % 10`: 1→'st', 2→'nd', 3→'rd', everything else→'th'.",
        solution="""```python
    def ordinalSuffix(number):
        if number % 100 in (11, 12, 13):
            return str(number) + 'th'
        if number % 10 == 1:
            return str(number) + 'st'
        if number % 10 == 2:
            return str(number) + 'nd'
        if number % 10 == 3:
            return str(number) + 'rd'
        return str(number) + 'th' 
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        ordinalSuffix(0) == '0th',
        ordinalSuffix(1) == '1st',
        ordinalSuffix(2) == '2nd',
        ordinalSuffix(3) == '3rd',
        ordinalSuffix(4) == '4th',
        ordinalSuffix(10) == '10th',
        ordinalSuffix(11) == '11th',
        ordinalSuffix(12) == '12th',
        ordinalSuffix(13) == '13th',
        ordinalSuffix(14) == '14th',
        ordinalSuffix(101) == '101st',
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 7: ASCII Table

    Write a `printASCIITable()` function that displays the ASCII number and its corresponding text character, from 32 to 126 (the printable ASCII characters).


    [📖 Full description](https://inventwithpython.com/pythongently/exercise7/)
    """)
    return


@app.function
# TODO: implement
def printASCIITable():
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use a `for` loop over `range(32, 127)` and Python's `chr()` function to convert integers to characters.",
        hint2="Print each line as `f\"{i} {chr(i)}\"`. Remember range's upper bound is exclusive, so use 127 not 126.",
        solution="""```python
    def printASCIITable():
        for i in range(32, 127):
            print(i, chr(i))
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import io as _io
    from contextlib import redirect_stdout as _redirect_stdout

    _buf = _io.StringIO()
    with _redirect_stdout(_buf):
        printASCIITable()
    _out = _buf.getvalue()
    _lines = _out.strip().split("\n")
    _results = [
        "65 A" in _out,
        "97 a" in _out,
        "32  " in _out,
        "126 ~" in _out,
        len(_lines) == 95,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 8: Read Write File

    Write three functions: `writeToFile()` with parameters for filename and text to write, `appendToFile()` which is identical but opens in append mode, and `readFromFile()` with one parameter for the filename that returns the full text contents as a string.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise8/)
    """)
    return


@app.cell
def _():
    # TODO: implement
    def writeToFile(filename, text):
        pass

    def appendToFile(filename, text):
        pass

    def readFromFile(filename):
        pass

    return appendToFile, readFromFile, writeToFile


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use `open(filename, mode)` with the `with` statement. Modes are `'w'` for write, `'a'` for append, `'r'` for read.",
        hint2="Write mode overwrites the file, append mode adds to the end. `fileObj.read()` returns the entire file contents as a string.",
        solution="""```python
    def writeToFile(filename, text):
        with open(filename, "w") as f:
            f.write(text)

    def appendToFile(filename, text):
        with open(filename, "a") as f:
            f.write(text)

    def readFromFile(filename):
        with open(filename, "r") as f:
            return f.read()
    ```"""
    )
    return


@app.cell
def _(appendToFile, mo, readFromFile, writeToFile):
    # 📋 Tests - run to check your solution
    import tempfile, os
    _tmp = tempfile.mktemp(suffix=".txt")
    writeToFile(_tmp, 'Hello!\n')
    appendToFile(_tmp, 'Goodbye!\n')
    _content = readFromFile(_tmp)
    os.remove(_tmp)
    _results = [_content == 'Hello!\nGoodbye!\n']
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 9: Chess Square Colour

    Write a `getChessSquareColor()` function with parameters `column` and `row`. The function returns 'black' or 'white' depending on the color at the specified position. Chess boards are 8×8 (columns and rows 1 to 8). If column or row is outside 1-8, return a blank string. White is always in the top-left corner.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise9/)
    """)
    return


@app.function
# TODO: implement
def getChessSquareColor(column: int, row: int):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="If the even/oddness of column and row match, the square is white. First check bounds (1-8).",
        hint2="Use `column % 2 == row % 2` — if they match, return 'white', otherwise 'black'. Return '' for out-of-bounds (outside 1-8).",
        solution="""```python
    def getChessSquareColor(column, row):
        if column < 1 or column > 8 or row < 1 or row > 8:
            return ''
        if column % 2 == row % 2:
            return 'white'
        else:
            return 'black' 
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        getChessSquareColor(1, 1) == 'white',
        getChessSquareColor(2, 1) == 'black',
        getChessSquareColor(1, 2) == 'black',
        getChessSquareColor(8, 8) == 'white',
        getChessSquareColor(0, 8) == '',
        getChessSquareColor(2, 9) == '',
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 10: Find & Replace

    Write a `findAndReplace()` function with three parameters: `text`, `oldText`, and `newText`. The function is case-sensitive: if replacing 'dog' with 'fox', 'DOG' in 'MY DOG' won't be replaced.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise10/)
    """)
    return


@app.function
# TODO: implement
def findAndReplace(text: str, oldText: str, newText: str):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use a `while` loop with an index `i`. Compare a slice `text[i:i+len(oldText)]` to `oldText` at each position.",
        hint2="If the slice matches, append `newText` and advance `i` by `len(oldText)`. Otherwise append `text[i]` and advance by 1.",
        solution="""```python
    def findAndReplace(text, oldText, newText):
        replacedText = ""
        i = 0
        while i < len(text):
            if text[i:i + len(oldText)] == oldText:
                replacedText += newText
                i += len(oldText)
            else:
                replacedText += text[i]
                i += 1
        return replacedText
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        findAndReplace('The fox', 'fox', 'dog') == 'The dog',
        findAndReplace('fox', 'fox', 'dog') == 'dog',
        findAndReplace('Firefox', 'fox', 'dog') == 'Firedog',
        findAndReplace('foxfox', 'fox', 'dog') == 'dogdog',
        findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.',
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 11: Hours, Minutes, Seconds

    Write a `getHoursMinutesSeconds()` function with a `totalSeconds` parameter.
    The argument is the number of seconds to translate into hours, minutes, and seconds.
    If the amount for hours, minutes, or seconds is zero, don't show it (return '10m'
    rather than '0h 10m 0s'). The only exception is that `getHoursMinutesSeconds(0)`
    should return '0s'.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise11/)
    """)
    return


@app.function
# TODO: implement
def getHoursMinutesSeconds(totalSeconds):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use integer division `//` by 3600 for hours and `//` by 60 for minutes. Use `%` to get remainders.",
        hint2="Build a list of strings like '2h', '5m', '30s' — only add if the value is > 0. Then `' '.join()` them. Special case: if totalSeconds is 0, return '0s'.",
        solution="""```python
    def getHoursMinutesSeconds(totalSeconds):
        if totalSeconds == 0:
            return '0s'
        hours = totalSeconds // 3600
        minutes = (totalSeconds % 3600) // 60
        seconds = totalSeconds % 60
        hms = []
        if hours > 0:
            hms.append(str(hours) + 'h')
        if minutes > 0:
            hms.append(str(minutes) + 'm')
        if seconds > 0:
            hms.append(str(seconds) + 's')
        return ' '.join(hms)
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _cases = [
        (0, "0s"),
        (59, "59s"),
        (60, "1m"),
        (61, "1m 1s"),
        (3599, "59m 59s"),
        (3600, "1h"),
        (3661, "1h 1m 1s"),
        (7322, "2h 2m 2s"),
        (86400, "24h"),
        (86522, "24h 2m 2s"),
    ]
    _results = [getHoursMinutesSeconds(s) == expected for s, expected in _cases]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 12: Smallest & Biggest

    Write a `getSmallest()` function with a `numbers` parameter (a list of integer
    and floating-point values). The function returns the smallest value in the list.
    If the list is empty, return `None`. Don't use Python's built-in `min()` function.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise12/)
    """)
    return


@app.function
# TODO: implement
def getSmallest(numbers):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Start with the first number as the smallest, then loop through comparing each number.",
        hint2="Handle empty list first (return None). Set `smallest = numbers[0]`, then `for num in numbers: if num < smallest: smallest = num`.",
        solution="""```python
    def getSmallest(numbers):
        if len(numbers) == 0:
            return None
        smallest = numbers[0]
        for number in numbers:
            if number < smallest:
                smallest = number
        return smallest
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        getSmallest([1, 2, 3]) == 1,
        getSmallest([3, 2, 1]) == 1,
        getSmallest([28, 25, 42, 2, 28]) == 2,
        getSmallest([1]) == 1,
        getSmallest([]) is None,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 13: Sum & Product

    Write two functions: `calculateSum()` and `calculateProduct()`, both with a
    `numbers` parameter (a list of integers or floats). `calculateSum()` returns the
    sum, `calculateProduct()` returns the product. Empty list returns 0 for sum and
    1 for product. Don't use Python's built-in `sum()` function.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise13/)
    """)
    return


@app.cell
def _():
    # TODO: implement
    def calculateSum(numbers):
        pass

    def calculateProduct(numbers):
        pass

    return calculateProduct, calculateSum


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="For sum, start a `total` at 0 and add each number. For product, start at 1 and multiply each number.",
        hint2="Product starts at 1 (not 0!) because anything × 0 = 0. Use `+=` for sum and `*=` for product.",
        solution="""```python
    def calculateSum(numbers):
        result = 0
        for number in numbers:
            result += number
        return result

    def calculateProduct(numbers):
        result = 1
        for number in numbers:
            result *= number
        return result
    ```"""
    )
    return


@app.cell
def _(calculateProduct, calculateSum, mo):
    # 📋 Tests - run to check your solution
    _results = [
        calculateSum([]) == 0,
        calculateSum([2, 4, 6, 8, 10]) == 30,
        calculateProduct([]) == 1,
        calculateProduct([2, 4, 6, 8, 10]) == 3840,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 14: Average

    Write an `average()` function with a `numbers` parameter. Returns the statistical
    average of the list of numbers. Passing an empty list should return `None`.
    Don't use Python's built-in `sum()` function.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise14/)
    """)
    return


@app.function
# TODO: implement
def average(numbers):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Sum all numbers and divide by how many there are. Use `len()` for the count.",
        hint2="Handle empty list first (return None). Then: `total / len(numbers)`.",
        solution="""```python
    def average(numbers):
        if len(numbers) == 0:
            return None
        total = 0
        for number in numbers:
            total += number
        return total / len(numbers)
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        average([1, 2, 3]) == 2,
        average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2,
        average([12, 20, 37]) == 23,
        average([0, 0, 0, 0, 0]) == 0,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 15: Median

    Write a `median()` function with a `numbers` parameter. Returns the statistical
    median. For odd-length lists, it's the middlemost number when sorted. For even-length
    lists, it's the average of the two middlemost numbers. Empty list returns `None`.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise15/)
    """)
    return


@app.function
# TODO: implement
def median(numbers):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Sort the list first, then find the middle index with `len(numbers) // 2`.",
        hint2="If even length: average the two middle values `(numbers[mid] + numbers[mid-1]) / 2`. If odd: just `numbers[mid]`.",
        solution="""```python
    def median(numbers):
        if len(numbers) == 0:
            return None
        numbers.sort()
        middleIndex = len(numbers) // 2
        if len(numbers) % 2 == 0:
            return (numbers[middleIndex] + numbers[middleIndex - 1]) / 2
        else:
            return numbers[middleIndex]
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        median([]) is None,
        median([1, 2, 3]) == 2,
        median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5,
        median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 16: Mode

    Write a `mode()` function with a `numbers` parameter. Returns the mode (most
    frequently appearing number) of the list. Empty list returns `None`.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise16/)
    """)
    return


@app.function
# TODO: implement
def mode(numbers):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use a dictionary to count how often each number appears. The key with the highest count is the mode.",
        hint2="Loop through numbers, incrementing `numberCount[number]`. Track `mostFreqNumber` and `mostFreqNumberCount` as you go.",
        solution="""```python
    def mode(numbers):
        if len(numbers) == 0:
            return None
        numberCount = {}
        mostFreqNumber = None
        mostFreqNumberCount = 0
        for number in numbers:
            if number not in numberCount:
                numberCount[number] = 0
            numberCount[number] += 1
            if numberCount[number] > mostFreqNumberCount:
                mostFreqNumber = number
                mostFreqNumberCount = numberCount[number]
        return mostFreqNumber
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import random as _rng16
    _rng16.seed(42)
    _td16 = [1, 2, 3, 4, 4]
    _results = [
        mode([]) is None,
        mode([1, 2, 3, 4, 4]) == 4,
        mode([1, 1, 2, 3, 4]) == 1,
    ]
    for _i in range(1000):
        _rng16.shuffle(_td16)
        _results.append(mode(_td16) == 4)
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 17: Dice Roll

    Write a `rollDice()` function with a `numberOfDice` parameter representing the
    number of six-sided dice to roll. Returns the sum of all dice rolls. Use
    `random.randint()` for each die.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise17/)
    """)
    return


@app.function
# TODO: implement

def rollDice(numberOfDice):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use a `for` loop and `random.randint(1, 6)` for each die. Sum the results.",
        hint2="Start `total = 0`, loop `numberOfDice` times with `for i in range(numberOfDice)`, add `random.randint(1, 6)` each time.",
        solution="""```python
    import random

    def rollDice(numberOfDice):
        total = 0
        for i in range(numberOfDice):
            total += random.randint(1, 6)
        return total
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [rollDice(0) == 0]
    for _i in range(1000):
        _results.append(1 <= rollDice(1) <= 6)
        _results.append(2 <= rollDice(2) <= 12)
        _results.append(3 <= rollDice(3) <= 18)
        _results.append(100 <= rollDice(100) <= 600)
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 18: Buy 8 Get 1 Free

    Write a `getCostOfCoffee()` function with parameters `numberOfCoffees` and
    `pricePerCoffee`. Returns the total cost considering that every 9th coffee is
    free (buy 8, get 1 free).


    [📖 Full description](https://inventwithpython.com/pythongently/exercise18/)
    """)
    return


@app.function
# TODO: implement
def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="For every 9 coffees, one is free. Calculate how many free coffees: `numberOfCoffees // 9`.",
        hint2="Paid coffees = `numberOfCoffees - numberOfFreeCoffees`. Return `numberOfPaidCoffees * pricePerCoffee`.",
        solution="""```python
    def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
        numberOfFreeCoffees = numberOfCoffees // 9
        numberOfPaidCoffees = numberOfCoffees - numberOfFreeCoffees
        return numberOfPaidCoffees * pricePerCoffee
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        getCostOfCoffee(7, 2.50) == 17.50,
        getCostOfCoffee(8, 2.50) == 20,
        getCostOfCoffee(9, 2.50) == 20,
        getCostOfCoffee(10, 2.50) == 22.50,
    ]
    for _i in range(1, 4):
        _results.extend([
            getCostOfCoffee(0, _i) == 0,
            getCostOfCoffee(8, _i) == 8 * _i,
            getCostOfCoffee(9, _i) == 8 * _i,
            getCostOfCoffee(18, _i) == 16 * _i,
            getCostOfCoffee(19, _i) == 17 * _i,
            getCostOfCoffee(30, _i) == 27 * _i,
        ])
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 19: Password Generator

    Write a `generatePassword()` function with a `length` parameter. If length < 12,
    force it to 12. The returned password must have at least one lowercase letter, one
    uppercase letter, one number, and one special character (~!@#$%^&*()_+).


    [📖 Full description](https://inventwithpython.com/pythongently/exercise19/)
    """)
    return


@app.cell
def _():
    LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUMBERS = '1234567890'
    SPECIAL = '~!@#$%^&*()_+'

    # TODO: implement
    def generatePassword(length):
        pass

    return LOWER_LETTERS, NUMBERS, SPECIAL, UPPER_LETTERS, generatePassword


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Start by guaranteeing one character from each category (lower, upper, digit, special). Then fill the rest randomly from all characters.",
        hint2="Build a list of characters, add one from each category first, then fill remaining with `random.randint()` indexing into a combined string. Shuffle at the end with `random.shuffle()`.",
        solution="""```python
    import random

    LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUMBERS = '1234567890'
    SPECIAL = '~!@#$%^&*()_+'
    ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL

    def generatePassword(length):
        if length < 12:
            length = 12
        password = []
        password.append(LOWER_LETTERS[random.randint(0, 25)])
        password.append(UPPER_LETTERS[random.randint(0, 25)])
        password.append(NUMBERS[random.randint(0, 9)])
        password.append(SPECIAL[random.randint(0, 12)])
        while len(password) < length:
            password.append(ALL_CHARS[random.randint(0, 74)])
        random.shuffle(password)
        return ''.join(password)
    ```"""
    )
    return


@app.cell
def _(LOWER_LETTERS, NUMBERS, SPECIAL, UPPER_LETTERS, generatePassword, mo):
    # 📋 Tests - run to check your solution
    _results = [len(generatePassword(8)) == 12]
    _pw = generatePassword(14)
    _results.append(len(_pw) == 14)
    _hasLower = _hasUpper = _hasNum = _hasSpecial = False
    for _ch in _pw:
        if _ch in LOWER_LETTERS:
            _hasLower = True
        if _ch in UPPER_LETTERS:
            _hasUpper = True
        if _ch in NUMBERS:
            _hasNum = True
        if _ch in SPECIAL:
            _hasSpecial = True
    _results.append(_hasLower and _hasUpper and _hasNum and _hasSpecial)
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 20: Leap Year

    Write an `isLeapYear()` function with an integer `year` parameter. Returns `True`
    if it's a leap year. Rules: divisible by 400 → leap year; divisible by 100 → not
    leap year; divisible by 4 → leap year; otherwise → not leap year.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise20/)
    """)
    return


@app.function
# TODO: implement
def isLeapYear(year):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Check divisibility in this order: 400, then 100, then 4. Each is an exception to the previous rule.",
        hint2="Use `if year % 400 == 0: return True`, `elif year % 100 == 0: return False`, `elif year % 4 == 0: return True`, `else: return False`.",
        solution="""```python
    def isLeapYear(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        isLeapYear(1999) == False,
        isLeapYear(2000) == True,
        isLeapYear(2001) == False,
        isLeapYear(2004) == True,
        isLeapYear(2100) == False,
        isLeapYear(2400) == True,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 21: Validate Date

    Write an `isValidDate()` function with parameters `year`, `month`, and `day`.
    Returns `True` if the integers represent a valid date, `False` otherwise.
    Months 1-12, days depend on month (28/29/30/31). February has 29 days on leap years.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise21/)
    """)
    return


@app.function
# TODO: implement
def isValidDate(year, month, day):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Check month is 1-12 first. Then check the day range depends on the month (30 vs 31 vs 28/29 for Feb).",
        hint2="Check leap year for Feb 29. September, April, June, November have 30 days. Use `if/elif` chain for each month group.",
        solution="```python\ndef isValidDate(year, month, day):\n    if not (1 <= month <= 12):\n        return False\n    if month in (1, 3, 5, 7, 8, 10, 12):\n        return 1 <= day <= 31\n    elif month in (4, 6, 9, 11):\n        return 1 <= day <= 30\n    else:  # February\n        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):\n            return 1 <= day <= 29\n        return 1 <= day <= 28\n```"
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        isValidDate(1999, 12, 31) == True,
        isValidDate(2000, 2, 29) == True,
        isValidDate(2001, 2, 29) == False,
        isValidDate(2029, 13, 1) == False,
        isValidDate(1000000, 1, 1) == True,
        isValidDate(2015, 4, 31) == False,
        isValidDate(1970, 5, 99) == False,
        isValidDate(1981, 0, 3) == False,
        isValidDate(1666, 4, 0) == False,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 22: Rock, Paper, Scissors

    Write a `rpsWinner()` function with parameters `player1` and `player2`
    (strings 'rock', 'paper', or 'scissors'). Returns 'player one' if player 1 wins,
    'player two' if player 2 wins, or 'tie'.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise22/)
    """)
    return


@app.function
# TODO: implement
def rpsWinner(player1, player2):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Check if both moves are the same first (tie). Then check the 3 winning conditions for player 1.",
        hint2="Player 1 wins if: rock vs scissors, paper vs rock, scissors vs paper. Everything else is player 2 winning.",
        solution="```python\ndef rpsWinner(move1, move2):\n    if move1 == 'rock' and move2 == 'paper':\n        return 'player two'\n    elif move1 == 'rock' and move2 == 'scissors':\n        return 'player one'\n    elif move1 == 'paper' and move2 == 'scissors':\n        return 'player two'\n    elif move1 == 'paper' and move2 == 'rock':\n        return 'player one'\n    elif move1 == 'scissors' and move2 == 'rock':\n        return 'player two'\n    elif move1 == 'scissors' and move2 == 'paper':\n        return 'player one'\n    else:\n        return 'tie'\n```"
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        rpsWinner('rock', 'paper') == 'player two',
        rpsWinner('rock', 'scissors') == 'player one',
        rpsWinner('paper', 'scissors') == 'player two',
        rpsWinner('paper', 'rock') == 'player one',
        rpsWinner('scissors', 'rock') == 'player two',
        rpsWinner('scissors', 'paper') == 'player one',
        rpsWinner('rock', 'rock') == 'tie',
        rpsWinner('paper', 'paper') == 'tie',
        rpsWinner('scissors', 'scissors') == 'tie',
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 23: 99 Bottles of Beer

    Write a program that displays the complete lyrics to "99 Bottles of Beer on the Wall."
    Each stanza counts down from 99, with the last line being "No more bottles of beer on the wall!"
    Use singular "bottle" when appropriate.

    *Visual output exercise — inspect output to verify.*


    [📖 Full description](https://inventwithpython.com/pythongently/exercise23/)
    """)
    return


@app.function
# TODO: implement
def bottlesOfBeer():
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use a `for` loop with `range(99, 1, -1)` to count down. Handle the singular 'bottle' case when count reaches 1.",
        hint2="The last stanza (1 bottle) needs special handling with 'No more bottles' as the final line.",
        solution="```python\ndef bottlesOfBeer():\n    for n in range(99, 1, -1):\n        print(f'{n} bottles of beer on the wall,')\n        print(f'{n} bottles of beer,')\n        print('Take one down,')\n        print('Pass it around,')\n        if n - 1 == 1:\n            print('1 bottle of beer on the wall,')\n        else:\n            print(f'{n-1} bottles of beer on the wall,')\n        print()\n    print('1 bottle of beer on the wall,')\n    print('1 bottle of beer,')\n    print('Take one down,')\n    print('Pass it around,')\n    print('No more bottles of beer on the wall!')\n```"
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import io as _io
    from contextlib import redirect_stdout as _redirect_stdout
    _buf = _io.StringIO()
    with _redirect_stdout(_buf):
        bottlesOfBeer()
    _out = _buf.getvalue()
    _results = [
        "99 bottles of beer on the wall," in _out,
        "1 bottle of beer on the wall," in _out,
        "No more bottles of beer on the wall!" in _out,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 24: Every 15 Minutes

    Write a program that displays the time for every 15 minute interval from 12:00 am to 11:45 pm
    (96 lines total). Use nested for loops over am/pm, hours (12, 1-11), and minutes (00, 15, 30, 45).

    *Visual output exercise — inspect output to verify.*


    [📖 Full description](https://inventwithpython.com/pythongently/exercise24/)
    """)
    return


@app.function
# TODO: implement
def every15Minutes():
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use three nested for loops: outer for am/pm, middle for hours (12, 1-11), inner for minutes (00, 15, 30, 45).",
        hint2="Hours list is ['12', '1', '2', ..., '11']. Minutes list is ['00', '15', '30', '45']. Concatenate with ':'.",
        solution="```python\ndef every15Minutes():\n    for meridiem in ['am', 'pm']:\n        for hour in ['12','1','2','3','4','5','6','7','8','9','10','11']:\n            for minutes in ['00', '15', '30', '45']:\n                print(hour + ':' + minutes + ' ' + meridiem)\n```"
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import io as _io
    from contextlib import redirect_stdout as _redirect_stdout
    _buf = _io.StringIO()
    with _redirect_stdout(_buf):
        every15Minutes()
    _out = _buf.getvalue()
    _lines = _out.strip().split(chr(10))
    _results = [
        len(_lines) == 96,
        "12:00 am" in _out,
        "11:45 pm" in _out,
        "1:15 am" in _out,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 25: Multiplication Table

    Write a program that displays a 10×10 multiplication table with properly aligned columns,
    number labels along the top and left sides, and separator lines made of dashes and pipes.

    *Visual output exercise — inspect output to verify.*


    [📖 Full description](https://inventwithpython.com/pythongently/exercise25/)
    """)
    return


@app.function
# TODO: implement
def multiplicationTable():
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use nested for loops (1-10 for both row and column). Use `str.rjust()` to right-justify numbers for alignment.",
        hint2="Print header row and separator line first. Then for each row, print the row label, a pipe, then each product right-justified to 2 chars.",
        solution="```python\ndef multiplicationTable():\n    print('  | 1  2  3  4  5  6  7  8  9 10')\n    print('--+------------------------------')\n    for row in range(1, 11):\n        print(str(row).rjust(2) + '|', end='')\n        for col in range(1, 11):\n            print(str(row * col).rjust(2) + ' ', end='')\n        print()\n```"
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import io as _io
    from contextlib import redirect_stdout as _redirect_stdout
    _buf = _io.StringIO()
    with _redirect_stdout(_buf):
        multiplicationTable()
    _out = _buf.getvalue()
    _results = [
        "| 1" in _out,
        "10|10" in _out or "10| 10" in _out,
        "100" in _out,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 26: Handshakes

    Write a `printHandshakes()` function with a `people` parameter (list of name strings).
    Prints all possible handshake pairs (no duplicates) and returns the count of handshakes.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise26/)
    """)
    return


@app.function
# TODO: implement
def printHandshakes(people):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use nested for loops where the inner loop starts after the outer loop's index to avoid duplicates.",
        hint2="`for i in range(0, len(people)-1)` and `for j in range(i+1, len(people))`. Count each pair.",
        solution="```python\ndef printHandshakes(people):\n    numberOfHandshakes = 0\n    for i in range(0, len(people) - 1):\n        for j in range(i + 1, len(people)):\n            print(people[i], 'shakes hands with', people[j])\n            numberOfHandshakes += 1\n    return numberOfHandshakes\n```"
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        printHandshakes(['Alice', 'Bob']) == 1,
        printHandshakes(['Alice', 'Bob', 'Carol']) == 3,
        printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 27: Rectangle Drawing

    Write a `drawRectangle()` function with `width` and `height` parameters.
    Prints a solid rectangle of # characters. If either dimension is 0 or negative, print nothing.

    *Visual output exercise — inspect output to verify.*


    [📖 Full description](https://inventwithpython.com/pythongently/exercise27/)
    """)
    return


@app.function
# TODO: implement
def drawRectangle(width, height):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use nested for loops or string replication (`'#' * width`) for each row. Print `height` rows.",
        hint2="Check if width or height < 1 first (return early). Then `for row in range(height): print('#' * width)`.",
        solution="```python\ndef drawRectangle(width, height):\n    if width < 1 or height < 1:\n        return\n    for row in range(height):\n        print('#' * width)\n```"
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import io as _io
    from contextlib import redirect_stdout as _redirect_stdout
    _buf = _io.StringIO()
    with _redirect_stdout(_buf):
        drawRectangle(10, 4)
    _out = _buf.getvalue()
    _lines = _out.strip().split(chr(10))
    _results = [
        len(_lines) == 4,
        all(line == "##########" for line in _lines),
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 28: Border Drawing

    Write a `drawBorder()` function with `width` and `height` parameters.
    Draws the border of a rectangle using + for corners, - for horizontal lines,
    and | for vertical lines. Interior is spaces. Minimum size is 2×2.

    *Visual output exercise — inspect output to verify.*


    [📖 Full description](https://inventwithpython.com/pythongently/exercise28/)
    """)
    return


@app.function
# TODO: implement
def drawBorder(width, height):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Print top line (`+` + dashes + `+`), then middle lines (`|` + spaces + `|`), then bottom line same as top.",
        hint2="Dashes and spaces are `width - 2` characters wide. Middle rows repeat `height - 2` times.",
        solution="```python\ndef drawBorder(width, height):\n    if width < 2 or height < 2:\n        return\n    print('+' + ('-' * (width - 2)) + '+')\n    for i in range(height - 2):\n        print('|' + (' ' * (width - 2)) + '|')\n    print('+' + ('-' * (width - 2)) + '+')\n```"
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import io as _io
    from contextlib import redirect_stdout as _redirect_stdout
    _buf = _io.StringIO()
    with _redirect_stdout(_buf):
        drawBorder(16, 4)
    _out = _buf.getvalue()
    _lines = _out.strip().split(chr(10))
    _results = [
        len(_lines) == 4,
        _lines[0] == "+--------------+",
        _lines[-1] == "+--------------+",
        _lines[1] == "|              |",
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 29: Pyramid Drawing

    Write a `drawPyramid()` function with a `height` parameter.
    The top row has 1 centered # character, each subsequent row has 2 more.
    Left-pad with spaces for centering.

    *Visual output exercise — inspect output to verify.*


    [📖 Full description](https://inventwithpython.com/pythongently/exercise29/)
    """)
    return


@app.function
# TODO: implement
def drawPyramid(height):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Each row has `rowNumber * 2 + 1` hashtags. Left-pad with `height - rowNumber - 1` spaces.",
        hint2="Loop `for rowNumber in range(height)`. Spaces = `' ' * (height - rowNumber - 1)`, hashtags = `'#' * (rowNumber * 2 + 1)`.",
        solution="```python\ndef drawPyramid(height):\n    for rowNumber in range(height):\n        spaces = ' ' * (height - (rowNumber + 1))\n        hashes = '#' * (rowNumber * 2 + 1)\n        print(spaces + hashes)\n```"
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import io as _io
    from contextlib import redirect_stdout as _redirect_stdout
    _buf = _io.StringIO()
    with _redirect_stdout(_buf):
        drawPyramid(5)
    _out = _buf.getvalue()
    _lines = _out.strip().split(chr(10))
    _results = [
        len(_lines) == 5,
        _lines[0].strip() == "#",
        _lines[-1].strip() == "#########",
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 30: 3D Box Drawing

    Write a `drawBox()` function with a `size` parameter.
    Draws a 3D box using - for horizontal, | for vertical, / for diagonal lines,
    and + for corners. If size < 1, print nothing.

    *Visual output exercise — inspect output to verify.*


    [📖 Full description](https://inventwithpython.com/pythongently/exercise30/)
    """)
    return


@app.function
# TODO: implement
def drawBox(size):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="The box has 3 surfaces. Horizontal lines use `size * 2` dashes. Vertical and diagonal lines use `size` characters each.",
        hint2="Draw 9 lines total: back top edge, top surface diagonals, front top edge, front surface sides, front bottom edge. Track indentation carefully.",
        solution="```python\ndef drawBox(size):\n    if size < 1:\n        return\n    print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')\n    for i in range(size):\n        print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')\n    print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')\n    for i in range(size - 1, -1, -1):\n        print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')\n    print('+' + '-' * (size * 2) + '+')\n```"
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import io as _io
    from contextlib import redirect_stdout as _redirect_stdout
    _buf = _io.StringIO()
    with _redirect_stdout(_buf):
        drawBox(2)
    _out = _buf.getvalue()
    _results = [
        "+----+" in _out,
        "/" in _out,
        "|" in _out,
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 31: Convert Integers To Strings

    Write a `convertIntToStr()` function with an `integerNum` parameter.
    Returns a string form of the integer (like `str()` does).
    Must work for negative integers. Don't use `str()` in your code.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise31/)
    """)
    return


@app.function
# TODO: implement
def convertIntToStr(integerNum):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use `% 10` to get the last digit and `// 10` to remove it. Build the string from right to left.",
        hint2="Map digits 0-9 to strings with a dictionary. Handle 0 and negatives as special cases.",
        solution="""```python
    def convertIntToStr(integerNum):
        if integerNum == 0:
            return '0'
        DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
            5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        if integerNum < 0:
            isNegative = True
            integerNum = -integerNum
        else:
            isNegative = False
        stringNum = ''
        while integerNum > 0:
            onesPlaceDigit = integerNum % 10
            stringNum = DIGITS_INT_TO_STR[onesPlaceDigit] + stringNum
            integerNum //= 10
        if isNegative:
            return '-' + stringNum
        else:
            return stringNum
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = []
    for _i in range(-10000, 10000):
        _results.append(convertIntToStr(_i) == str(_i))
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 32: Convert Strings To Integers

    Write a `convertStrToInt()` function with a `stringNum` parameter.
    Returns an integer form of the string (like `int()` does).
    Must work for negative numbers. Don't use `int()` in your code.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise32/)
    """)
    return


@app.function
# TODO: implement
def convertStrToInt(stringNum):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use a dictionary mapping '0'-'9' to 0-9. Process characters left to right.",
        hint2="Multiply running total by 10, then add the current digit. Handle negative sign at start.",
        solution="""```python
    def convertStrToInt(stringNum):
        DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        if stringNum[0] == '-':
            isNegative = True
            stringNum = stringNum[1:]
        else:
            isNegative = False
        integerNum = 0
        for i in range(len(stringNum)):
            digit = DIGITS_STR_TO_INT[stringNum[i]]
            integerNum = (integerNum * 10) + digit
        if isNegative:
            return -integerNum
        else:
            return integerNum
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = []
    for _i in range(-10000, 10000):
        _results.append(convertStrToInt(str(_i)) == _i)
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 33: Comma-Formatted Numbers

    Write a `commaFormat()` function with a `number` parameter (integer or float).
    Returns a string with proper US/UK comma formatting
    (comma after every third digit in the whole number part only).


    [📖 Full description](https://inventwithpython.com/pythongently/exercise33/)
    """)
    return


@app.function
# TODO: implement
def commaFormat(number):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Work with the string form. Process digits from right to left, inserting commas every 3 digits.",
        hint2="Handle the fractional part separately (no commas there). Build triplets from right, join with commas.",
        solution="""```python
    def commaFormat(number):
        number = str(number)
        if '.' in number:
            fractionalPart = number[number.index('.'):]
            number = number[:number.index('.')]
        else:
            fractionalPart = ''
        triplet = ''
        commaNumber = ''
        for i in range(len(number) - 1, -1, -1):
            triplet = number[i] + triplet
            if len(triplet) == 3:
                commaNumber = triplet + ',' + commaNumber
                triplet = ''
        if triplet != '':
            commaNumber = triplet + ',' + commaNumber
        return commaNumber[:-1] + fractionalPart
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        commaFormat(1) == '1',
        commaFormat(10) == '10',
        commaFormat(100) == '100',
        commaFormat(1000) == '1,000',
        commaFormat(10000) == '10,000',
        commaFormat(100000) == '100,000',
        commaFormat(1000000) == '1,000,000',
        commaFormat(1234567890) == '1,234,567,890',
        commaFormat(1000.123456) == '1,000.123456',
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 34: Uppercase Letters

    Write a `getUppercase()` function with a `text` parameter.
    Returns a string with all lowercase letters converted to uppercase.
    Non-letter characters remain unchanged. Don't use Python's `upper()` method.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise34/)
    """)
    return


@app.function
# TODO: implement
def getUppercase(text):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Create a dictionary mapping lowercase to uppercase letters. Loop over each character.",
        hint2="If character is in the dictionary, use the uppercase version. Otherwise keep it as-is.",
        solution="""```python
    LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
    'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K',
    'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q',
    'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W',
    'x': 'X', 'y': 'Y', 'z': 'Z'}

    def getUppercase(text):
        uppercaseText = ''
        for character in text:
            if character in LOWER_TO_UPPER:
                uppercaseText += LOWER_TO_UPPER[character]
            else:
                uppercaseText += character
        return uppercaseText
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        getUppercase('Hello') == 'HELLO',
        getUppercase('hello') == 'HELLO',
        getUppercase('HELLO') == 'HELLO',
        getUppercase('Hello, world!') == 'HELLO, WORLD!',
        getUppercase('goodbye 123!') == 'GOODBYE 123!',
        getUppercase('12345') == '12345',
        getUppercase('') == '',
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 35: Title Case

    Write a `getTitleCase()` function with a `text` parameter.
    Returns the title case form: every word begins with uppercase, remaining letters
    are lowercase. Non-letter characters separate words.
    Don't use Python's `title()` or `split()` methods.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise35/)
    """)
    return


@app.function
# TODO: implement
def getTitleCase(text):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="A character is the start of a word if it's at index 0 OR the previous character is not a letter.",
        hint2="Use `text[i-1].isalpha()` to check previous char. Uppercase the first letter of each word, lowercase everything else.",
        solution="""```python
    def getTitleCase(text):
        titledText = ''
        for i in range(len(text)):
            if i == 0:
                titledText += text[i].upper()
            elif text[i].isalpha() and not text[i - 1].isalpha():
                titledText += text[i].upper()
            else:
                titledText += text[i].lower()
        return titledText
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        getTitleCase('Hello, world!') == 'Hello, World!',
        getTitleCase('HELLO') == 'Hello',
        getTitleCase('hello') == 'Hello',
        getTitleCase('hElLo') == 'Hello',
        getTitleCase('') == '',
        getTitleCase('abc123xyz') == 'Abc123Xyz',
        getTitleCase('cat dog RAT') == 'Cat Dog Rat',
        getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat',
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 36: Reverse String

    Write a `reverseString()` function with a `text` parameter.
    Returns a string with all characters in reverse order.
    Empty string returns empty string.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise36/)
    """)
    return


@app.function
# TODO: implement
def reverseString(text):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Convert string to list, swap characters from outside in (first with last, second with second-to-last).",
        hint2="Loop over first half of indexes. Mirror index is `len(text) - 1 - i`. Swap `text[i]` and `text[mirrorIndex]`.",
        solution="""```python
    def reverseString(text):
        text = list(text)
        for i in range(len(text) // 2):
            mirrorIndex = len(text) - 1 - i
            text[i], text[mirrorIndex] = text[mirrorIndex], text[i]
        return ''.join(text)
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        reverseString('Hello') == 'olleH',
        reverseString('') == '',
        reverseString('aaazzz') == 'zzzaaa',
        reverseString('xxxx') == 'xxxx',
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 37: Change Maker

    Write a `makeChange()` function with an `amount` parameter (integer cents).
    Returns a dictionary with keys 'quarters', 'dimes', 'nickels', 'pennies'
    showing the minimal number of coins. Keys with 0 coins should not be present.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise37/)
    """)
    return


@app.function
# TODO: implement
def makeChange(amount):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Start with the largest coin (quarters = 25¢) and work down. Use `//` for count and `%` for remainder.",
        hint2="For each denomination: if amount >= value, add `amount // value` coins, then `amount = amount % value`. Skip zeros.",
        solution="""```python
    def makeChange(amount):
        change = {}
        if amount >= 25:
            change['quarters'] = amount // 25
            amount = amount % 25
        if amount >= 10:
            change['dimes'] = amount // 10
            amount = amount % 10
        if amount >= 5:
            change['nickels'] = amount // 5
            amount = amount % 5
        if amount >= 1:
            change['pennies'] = amount
        return change
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        makeChange(30) == {'quarters': 1, 'nickels': 1},
        makeChange(10) == {'dimes': 1},
        makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2},
        makeChange(100) == {'quarters': 4},
        makeChange(125) == {'quarters': 5},
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 38: Random Shuffle

    Write a `shuffle()` function with a `values` parameter (a list).
    Shuffles the list in-place by swapping each value with a randomly selected index.
    The function doesn't return anything. Don't use `random.shuffle()`.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise38/)
    """)
    return


@app.function
# TODO: implement
def shuffle(values):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Loop over each index and swap with a randomly chosen index using `random.randint(0, len(values)-1)`.",
        hint2="`for i in range(len(values)): swapIndex = random.randint(0, len(values)-1)` then swap `values[i], values[swapIndex]`.",
        solution="""```python
    import random

    def shuffle(values):
        for i in range(len(values)):
            swapIndex = random.randint(0, len(values) - 1)
            values[i], values[swapIndex] = values[swapIndex], values[i]
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    import random as _rng38
    _rng38.seed(42)
    _results = []
    for _i in range(10):
        _td = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shuffle(_td)
        _results.append(len(_td) == 10)
        _results.append(_td != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        _results.append(sorted(_td) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    _td2 = []
    shuffle(_td2)
    _results.append(_td2 == [])
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 39: Collatz Sequence

    Write a `collatz()` function with a `startingNumber` parameter.
    Returns a list of the Collatz sequence: if n is even, next is n/2;
    if odd, next is 3n+1. Sequence ends at 1. If startingNumber < 1, return empty list.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise39/)
    """)
    return


@app.function
# TODO: implement
def collatz(startingNumber):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="If even: n//2. If odd: 3*n+1. Keep going until n==1. Collect each value in a list.",
        hint2="Start with `[startingNumber]`, use a while loop until `num != 1`. Use `% 2` to check even/odd.",
        solution="""```python
    def collatz(startingNumber):
        if startingNumber < 1:
            return []
        sequence = [startingNumber]
        num = startingNumber
        while num != 1:
            if num % 2 == 1:
                num = 3 * num + 1
            else:
                num = num // 2
            sequence.append(num)
        return sequence
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        collatz(0) == [],
        collatz(10) == [10, 5, 16, 8, 4, 2, 1],
        collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
        collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1],
        len(collatz(256)) == 9,
        len(collatz(257)) == 123,
    ]
    import random as _rng39
    _rng39.seed(42)
    for _i in range(1000):
        _sn = _rng39.randint(1, 10000)
        _seq = collatz(_sn)
        _results.append(_seq[0] == _sn)
        _results.append(_seq[-1] == 1)
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 40: Merging Two Sorted Lists

    Write a `mergeTwoLists()` function with parameters `list1` and `list2` (both pre-sorted).
    Returns a single sorted list of all numbers from both lists.
    Don't use `sorted()` or `sort()`.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise40/)
    """)
    return


@app.function
# TODO: implement
def mergeTwoLists(list1, list2):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use two index pointers (i1, i2). Compare values at each pointer, append the smaller one.",
        hint2="While both pointers are in bounds, compare and advance the smaller. Then append whatever remains from the other list.",
        solution="""```python
    def mergeTwoLists(list1, list2):
        result = []
        i1 = 0
        i2 = 0
        while i1 < len(list1) and i2 < len(list2):
            if list1[i1] < list2[i2]:
                result.append(list1[i1])
                i1 += 1
            else:
                result.append(list2[i2])
                i2 += 1
        if i1 < len(list1):
            for j in range(i1, len(list1)):
                result.append(list1[j])
        if i2 < len(list2):
            for j in range(i2, len(list2)):
                result.append(list2[j])
        return result
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9],
        mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5],
        mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5],
        mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2],
        mergeTwoLists([1, 2, 3], []) == [1, 2, 3],
        mergeTwoLists([], [1, 2, 3]) == [1, 2, 3],
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 41: ROT 13 Encryption

    Write a `rot13()` function with a `text` parameter.
    Returns the ROT 13 encrypted version: each letter is replaced by the letter
    13 positions later in the alphabet (wrapping around).
    Non-letter characters are unchanged. Encrypting twice returns the original text.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise41/)
    """)
    return


@app.function
# TODO: implement
def rot13(text):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Add 13 to each letter's ord() value. If it goes past 'z' (122) or 'Z' (90), subtract 26.",
        hint2="Check `char.isalpha()` first. Use `ord()+13`, then check if past the end of alphabet for that case. Use `chr()` to convert back.",
        solution="""```python
    def rot13(text):
        encryptedText = ''
        for character in text:
            if not character.isalpha():
                encryptedText += character
            else:
                rotatedLetterOrdinal = ord(character) + 13
                if character.islower() and rotatedLetterOrdinal > 122:
                    rotatedLetterOrdinal -= 26
                if character.isupper() and rotatedLetterOrdinal > 90:
                    rotatedLetterOrdinal -= 26
                encryptedText += chr(rotatedLetterOrdinal)
        return encryptedText
    ```""",
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        rot13('Hello, world!') == 'Uryyb, jbeyq!',
        rot13('Uryyb, jbeyq!') == 'Hello, world!',
        rot13(rot13('Hello, world!')) == 'Hello, world!',
        rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm',
        rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM',
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 42: Bubble Sort

    Write a `bubbleSort()` function with a `numbers` parameter (a list).
    Sorts the list in-place using the bubble sort algorithm and returns the sorted list.
    Don't use `sort()` or `sorted()`.


    [📖 Full description](https://inventwithpython.com/pythongently/exercise42/)
    """)
    return


@app.function
# TODO: implement
def bubbleSort(numbers):
    pass


@app.cell(hide_code=True)
def _(show_hints):
    show_hints(
        hint1="Use nested loops. Compare every pair of indexes and swap if the left value is greater than the right.",
        hint2="Outer: `range(len(numbers)-1)`. Inner: `range(i+1, len(numbers))`. Swap if `numbers[i] > numbers[j]`.",
        solution="""```python
    def bubbleSort(numbers):
        for i in range(len(numbers) - 1):
            for j in range(i, len(numbers)):
                if numbers[i] > numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers
    ```"""
    )
    return


@app.cell
def _(mo):
    # 📋 Tests - run to check your solution
    _results = [
        bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4],
        bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2],
    ]
    mo.md(f"**📋 Tests:** {'✅ all passed' if all(_results) else '❌ some failed'}")
    return


if __name__ == "__main__":
    app.run()
