x = "global x"

def outer_function():
    x = "enclosing x"

    def inner_function():
        x = "local x"
        print("Inside inner_function:", x)

    inner_function()
    print("Inside outer_function:", x)

print("In global scope:", x)
outer_function()
