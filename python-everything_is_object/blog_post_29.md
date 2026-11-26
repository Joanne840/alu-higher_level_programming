# Python3: Mutable, Immutable... Everything Is an Object!

![Python](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

Everything in Python is an object, including numbers, strings, lists, tuples, functions, and classes. Knowing how objects and references work prevents bugs when assigning variables, creating aliases, or passing arguments to functions.

Every object has an identity (id()), a type (type()), and a value. id() returns a unique identifier (in CPython, its memory address), and type() returns its type.

```python
x = 89
print(type(x))
print(id(x))
```

Memory schema 1:
[x] ---> (int: 89)

Mutable objects can change in place without changing id(): list, dict, set, and bytearray.

```python
l = [1, 2, 3]
before = id(l)
l.append(4)
print(l, id(l) == before)
```

Memory schema 2:
[l] ---> (list: [1, 2, 3] -> [1, 2, 3, 4], same id)

Immutable objects cannot change in place after creation: int, float, complex, str, tuple, frozenset, and bytes. Changing values creates or points to a new object in memory rather than mutating the existing object.

This matters because mutating a shared mutable object affects all references to it, while rebinding an immutable reference does not. CPython pre-allocates 262 small integers at startup using NSMALLPOSINTS and NSMALLNEGINTS for the most used small integers; aliases share a reference to the same object; and tuple or frozenset are immutable containers that can still contain mutable objects.

Arguments are passed to functions by object reference assignment. Mutating a mutable object inside a function changes the caller object, whereas rebinding a local variable (such as n = v or n += 1) only changes the local reference.
