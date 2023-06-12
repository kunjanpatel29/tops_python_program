"""
The nonlocal keyword is used to work with variables inside nested functions,
where the variable should not belong to the inner function.
"""

# Without Nonlocal Keyword
def fun1():
    x = "Kunjan"

    def fun2():
        x = "Python"
    fun2()
    return x

print(fun1())

# With Nonlocal Keyword
def fun1():
    x = "Kunjan"

    def fun2():
        nonlocal x
        x = "Python"
    fun2()
    return x

print(fun1())
