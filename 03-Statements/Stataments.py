{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "\n",
    "<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>\n",
    "___\n",
    "<center><em>Content Copyright by Pierian Data</em></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Introduction to Python Statements\n",
    "\n",
    "In this lecture we will be doing a quick overview of Python Statements. This lecture will emphasize differences between Python and other languages such as C++. \n",
    "\n",
    "There are two reasons we take this approach for learning the context of Python Statements:\n",
    "\n",
    "    1.) If you are coming from a different language this will rapidly accelerate your understanding of Python.\n",
    "    2.) Learning about statements will allow you to be able to read other languages more easily in the future."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Python vs Other Languages\n",
    "\n",
    "Let's create a simple statement that says:\n",
    "\"If a is greater than b, assign 2 to a and 4 to b\"\n",
    "\n",
    "Take a look at these two if statements (we will learn about building out if statements soon).\n",
    "\n",
    "**Version 1 (Other Languages)**\n",
    "\n",
    "    if (a>b){\n",
    "        a = 2;\n",
    "        b = 4;\n",
    "    }\n",
    "                        \n",
    "**Version 2 (Python)**   \n",
    "\n",
    "    if a>b:\n",
    "        a = 2\n",
    "        b = 4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You'll notice that Python is less cluttered and much more readable than the first version. How does Python manage this?\n",
    "\n",
    "Let's walk through the main differences:\n",
    "\n",
    "Python gets rid of () and {} by incorporating two main factors: a *colon* and *whitespace*. The statement is ended with a colon, and whitespace is used (indentation) to describe what takes place in case of the statement.\n",
    "\n",
    "Another major difference is the lack of semicolons in Python. Semicolons are used to denote statement endings in many other languages, but in Python, the end of a line is the same as the end of a statement.\n",
    "\n",
    "Lastly, to end this brief overview of differences, let's take a closer look at indentation syntax in Python vs other languages:\n",
    "\n",
    "## Indentation\n",
    "\n",
    "Here is some pseudo-code to indicate the use of whitespace and indentation in Python:\n",
    "\n",
    "**Other Languages**\n",
    "\n",
    "    if (x)\n",
    "        if(y)\n",
    "            code-statement;\n",
    "    else\n",
    "        another-code-statement;\n",
    "        \n",
    "**Python**\n",
    "    \n",
    "    if x:\n",
    "        if y:\n",
    "            code-statement\n",
    "    else:\n",
    "        another-code-statement"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note how Python is so heavily driven by code indentation and whitespace. This means that code readability is a core part of the design of the Python language.\n",
    "\n",
    "Now let's start diving deeper by coding these sort of statements in Python!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Time to code!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "\n",
    "<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>\n",
    "___\n",
    "<center><em>Content Copyright by Pierian Data</em></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# if, elif, else Statements\n",
    "\n",
    "<code>if</code> Statements in Python allows us to tell the computer to perform alternative actions based on a certain set of results.\n",
    "\n",
    "Verbally, we can imagine we are telling the computer:\n",
    "\n",
    "\"Hey if this case happens, perform some action\"\n",
    "\n",
    "We can then expand the idea further with <code>elif</code> and <code>else</code> statements, which allow us to tell the computer:\n",
    "\n",
    "\"Hey if this case happens, perform some action. Else, if another case happens, perform some other action. Else, if *none* of the above cases happened, perform this action.\"\n",
    "\n",
    "Let's go ahead and look at the syntax format for <code>if</code> statements to get a better idea of this:\n",
    "\n",
    "    if case1:\n",
    "        perform action1\n",
    "    elif case2:\n",
    "        perform action2\n",
    "    else: \n",
    "        perform action3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## First Example\n",
    "\n",
    "Let's see a quick example of this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It was true!\n"
     ]
    }
   ],
   "source": [
    "if True:\n",
    "    print('It was true!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's add in some else logic:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I will be printed in any case where x is not true\n"
     ]
    }
   ],
   "source": [
    "x = False\n",
    "\n",
    "if x:\n",
    "    print('x was True!')\n",
    "else:\n",
    "    print('I will be printed in any case where x is not true')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Multiple Branches\n",
    "\n",
    "Let's get a fuller picture of how far <code>if</code>, <code>elif</code>, and <code>else</code> can take us!\n",
    "\n",
    "We write this out in a nested structure. Take note of how the <code>if</code>, <code>elif</code>, and <code>else</code> line up in the code. This can help you see what <code>if</code> is related to what <code>elif</code> or <code>else</code> statements.\n",
    "\n",
    "We'll reintroduce a comparison syntax for Python."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the bank!\n"
     ]
    }
   ],
   "source": [
    "loc = 'Bank'\n",
    "\n",
    "if loc == 'Auto Shop':\n",
    "    print('Welcome to the Auto Shop!')\n",
    "elif loc == 'Bank':\n",
    "    print('Welcome to the bank!')\n",
    "else:\n",
    "    print('Where are you?')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note how the nested <code>if</code> statements are each checked until a True boolean causes the nested code below it to run. You should also note that you can put in as many <code>elif</code> statements as you want before you close off with an <code>else</code>.\n",
    "\n",
    "Let's create two more simple examples for the <code>if</code>, <code>elif</code>, and <code>else</code> statements:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome Sammy!\n"
     ]
    }
   ],
   "source": [
    "person = 'Sammy'\n",
    "\n",
    "if person == 'Sammy':\n",
    "    print('Welcome Sammy!')\n",
    "else:\n",
    "    print(\"Welcome, what's your name?\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome George!\n"
     ]
    }
   ],
   "source": [
    "person = 'George'\n",
    "\n",
    "if person == 'Sammy':\n",
    "    print('Welcome Sammy!')\n",
    "elif person =='George':\n",
    "    print('Welcome George!')\n",
    "else:\n",
    "    print(\"Welcome, what's your name?\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Indentation\n",
    "\n",
    "It is important to keep a good understanding of how indentation works in Python to maintain the structure and order of your code. We will touch on this topic again when we start building out functions!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "\n",
    "<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>\n",
    "___\n",
    "<center><em>Content Copyright by Pierian Data</em></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# for Loops\n",
    "\n",
    "A <code>for</code> loop acts as an iterator in Python; it goes through items that are in a *sequence* or any other iterable item. Objects that we've learned about that we can iterate over include strings, lists, tuples, and even built-in iterables for dictionaries, such as keys or values.\n",
    "\n",
    "We've already seen the <code>for</code> statement a little bit in past lectures but now let's formalize our understanding.\n",
    "\n",
    "Here's the general format for a <code>for</code> loop in Python:\n",
    "\n",
    "    for item in object:\n",
    "        statements to do stuff\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The variable name used for the item is completely up to the coder, so use your best judgment for choosing a name that makes sense and you will be able to understand when revisiting your code. This item name can then be referenced inside your loop, for example if you wanted to use <code>if</code> statements to perform checks.\n",
    "\n",
    "Let's go ahead and work through several example of <code>for</code> loops using a variety of data object types. We'll start simple and build more complexity later on.\n",
    "\n",
    "## Example 1\n",
    "Iterating through a list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# We'll learn how to automate this sort of list in the next lecture\n",
    "list1 = [1,2,3,4,5,6,7,8,9,10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for num in list1:\n",
    "    print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Hopefully this makes sense. Now let's add an <code>if</code> statement to check for even numbers. We'll first introduce a new concept here--the modulo.\n",
    "### Modulo\n",
    "The modulo allows us to get the remainder in a division and uses the % symbol. For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "17 % 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This makes sense since 17 divided by 5 is 3 remainder 2. Let's see a few more quick examples:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 3 Remainder 1\n",
    "10 % 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 2 Remainder 4\n",
    "18 % 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 2 no remainder\n",
    "4 % 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that if a number is fully divisible with no remainder, the result of the modulo call is 0. We can use this to test for even numbers, since if a number modulo 2 is equal to 0, that means it is an even number!\n",
    "\n",
    "Back to the <code>for</code> loops!\n",
    "\n",
    "## Example 2\n",
    "Let's print only the even numbers from that list!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for num in list1:\n",
    "    if num % 2 == 0:\n",
    "        print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We could have also put an <code>else</code> statement in there:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Odd number\n",
      "2\n",
      "Odd number\n",
      "4\n",
      "Odd number\n",
      "6\n",
      "Odd number\n",
      "8\n",
      "Odd number\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for num in list1:\n",
    "    if num % 2 == 0:\n",
    "        print(num)\n",
    "    else:\n",
    "        print('Odd number')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Example 3\n",
    "Another common idea during a <code>for</code> loop is keeping some sort of running tally during multiple loops. For example, let's create a <code>for</code> loop that sums up the list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n"
     ]
    }
   ],
   "source": [
    "# Start sum at zero\n",
    "list_sum = 0 \n",
    "\n",
    "for num in list1:\n",
    "    list_sum = list_sum + num\n",
    "\n",
    "print(list_sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Read over the above cell and make sure you understand fully what is going on. Also we could have implemented a <code>+=</code> to perform the addition towards the sum. For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n"
     ]
    }
   ],
   "source": [
    "# Start sum at zero\n",
    "list_sum = 0 \n",
    "\n",
    "for num in list1:\n",
    "    list_sum += num\n",
    "\n",
    "print(list_sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Example 4\n",
    "We've used <code>for</code> loops with lists, how about with strings? Remember strings are a sequence so when we iterate through them we will be accessing each item in that string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "T\n",
      "h\n",
      "i\n",
      "s\n",
      " \n",
      "i\n",
      "s\n",
      " \n",
      "a\n",
      " \n",
      "s\n",
      "t\n",
      "r\n",
      "i\n",
      "n\n",
      "g\n",
      ".\n"
     ]
    }
   ],
   "source": [
    "for letter in 'This is a string.':\n",
    "    print(letter)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Example 5\n",
    "Let's now look at how a <code>for</code> loop can be used with a tuple:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "tup = (1,2,3,4,5)\n",
    "\n",
    "for t in tup:\n",
    "    print(t)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Example 6\n",
    "Tuples have a special quality when it comes to <code>for</code> loops. If you are iterating through a sequence that contains tuples, the item can actually be the tuple itself, this is an example of *tuple unpacking*. During the <code>for</code> loop we will be unpacking the tuple inside of a sequence and we can access the individual items inside that tuple!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "list2 = [(2,4),(6,8),(10,12)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 4)\n",
      "(6, 8)\n",
      "(10, 12)\n"
     ]
    }
   ],
   "source": [
    "for tup in list2:\n",
    "    print(tup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "6\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "# Now with unpacking!\n",
    "for (t1,t2) in list2:\n",
    "    print(t1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Cool! With tuples in a sequence we can access the items inside of them through unpacking! The reason this is important is because many objects will deliver their iterables through tuples. Let's start exploring iterating through Dictionaries to explore this further!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Example 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "d = {'k1':1,'k2':2,'k3':3}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "k1\n",
      "k2\n",
      "k3\n"
     ]
    }
   ],
   "source": [
    "for item in d:\n",
    "    print(item)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice how this produces only the keys. So how can we get the values? Or both the keys and the values? \n",
    "\n",
    "We're going to introduce three new Dictionary methods: **.keys()**, **.values()** and **.items()**\n",
    "\n",
    "In Python each of these methods return a *dictionary view object*. It supports operations like membership test and iteration, but its contents are not independent of the original dictionary – it is only a view. Let's see it in action:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([('k1', 1), ('k2', 2), ('k3', 3)])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a dictionary view object\n",
    "d.items()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Since the .items() method supports iteration, we can perform *dictionary unpacking* to separate keys and values just as we did in the previous examples."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "k1\n",
      "1\n",
      "k2\n",
      "2\n",
      "k3\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "# Dictionary unpacking\n",
    "for k,v in d.items():\n",
    "    print(k)\n",
    "    print(v) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you want to obtain a true list of keys, values, or key/value tuples, you can *cast* the view as a list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['k1', 'k2', 'k3']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(d.keys())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(d.values())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Conclusion\n",
    "\n",
    "We've learned how to use for loops to iterate through tuples, lists, strings, and dictionaries. It will be an important tool for us, so make sure you know it well and understood the above examples.\n",
    "\n",
    "[More resources](http://www.tutorialspoint.com/python/python_for_loop.htm)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "\n",
    "<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>\n",
    "___\n",
    "<center><em>Content Copyright by Pierian Data</em></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# while Loops\n",
    "\n",
    "The <code>while</code> statement in Python is one of most general ways to perform iteration. A <code>while</code> statement will repeatedly execute a single statement or group of statements as long as the condition is true. The reason it is called a 'loop' is because the code statements are looped through over and over again until the condition is no longer met.\n",
    "\n",
    "The general format of a while loop is:\n",
    "\n",
    "    while test:\n",
    "        code statements\n",
    "    else:\n",
    "        final code statements\n",
    "\n",
    "Let’s look at a few simple <code>while</code> loops in action. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x is currently:  0\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  1\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  2\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  3\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  4\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  5\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  6\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  7\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  8\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  9\n",
      " x is still less than 10, adding 1 to x\n"
     ]
    }
   ],
   "source": [
    "x = 0\n",
    "\n",
    "while x < 10:\n",
    "    print('x is currently: ',x)\n",
    "    print(' x is still less than 10, adding 1 to x')\n",
    "    x+=1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice how many times the print statements occurred and how the <code>while</code> loop kept going until the True condition was met, which occurred once x==10. It's important to note that once this occurred the code stopped. Let's see how we could add an <code>else</code> statement:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x is currently:  0\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  1\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  2\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  3\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  4\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  5\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  6\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  7\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  8\n",
      " x is still less than 10, adding 1 to x\n",
      "x is currently:  9\n",
      " x is still less than 10, adding 1 to x\n",
      "All Done!\n"
     ]
    }
   ],
   "source": [
    "x = 0\n",
    "\n",
    "while x < 10:\n",
    "    print('x is currently: ',x)\n",
    "    print(' x is still less than 10, adding 1 to x')\n",
    "    x+=1\n",
    "    \n",
    "else:\n",
    "    print('All Done!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# break, continue, pass\n",
    "\n",
    "We can use <code>break</code>, <code>continue</code>, and <code>pass</code> statements in our loops to add additional functionality for various cases. The three statements are defined by:\n",
    "\n",
    "    break: Breaks out of the current closest enclosing loop.\n",
    "    continue: Goes to the top of the closest enclosing loop.\n",
    "    pass: Does nothing at all.\n",
    "    \n",
    "    \n",
    "Thinking about <code>break</code> and <code>continue</code> statements, the general format of the <code>while</code> loop looks like this:\n",
    "\n",
    "    while test: \n",
    "        code statement\n",
    "        if test: \n",
    "            break\n",
    "        if test: \n",
    "            continue \n",
    "    else:\n",
    "\n",
    "<code>break</code> and <code>continue</code> statements can appear anywhere inside the loop’s body, but we will usually put them further nested in conjunction with an <code>if</code> statement to perform an action based on some condition.\n",
    "\n",
    "Let's go ahead and look at some examples!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x is currently:  0\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n",
      "x is currently:  1\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n",
      "x is currently:  2\n",
      " x is still less than 10, adding 1 to x\n",
      "x==3\n",
      "x is currently:  3\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n",
      "x is currently:  4\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n",
      "x is currently:  5\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n",
      "x is currently:  6\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n",
      "x is currently:  7\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n",
      "x is currently:  8\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n",
      "x is currently:  9\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n"
     ]
    }
   ],
   "source": [
    "x = 0\n",
    "\n",
    "while x < 10:\n",
    "    print('x is currently: ',x)\n",
    "    print(' x is still less than 10, adding 1 to x')\n",
    "    x+=1\n",
    "    if x==3:\n",
    "        print('x==3')\n",
    "    else:\n",
    "        print('continuing...')\n",
    "        continue"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note how we have a printed statement when x==3, and a continue being printed out as we continue through the outer while loop. Let's put in a break once x ==3 and see if the result makes sense:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x is currently:  0\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n",
      "x is currently:  1\n",
      " x is still less than 10, adding 1 to x\n",
      "continuing...\n",
      "x is currently:  2\n",
      " x is still less than 10, adding 1 to x\n",
      "Breaking because x==3\n"
     ]
    }
   ],
   "source": [
    "x = 0\n",
    "\n",
    "while x < 10:\n",
    "    print('x is currently: ',x)\n",
    "    print(' x is still less than 10, adding 1 to x')\n",
    "    x+=1\n",
    "    if x==3:\n",
    "        print('Breaking because x==3')\n",
    "        break\n",
    "    else:\n",
    "        print('continuing...')\n",
    "        continue"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note how the other <code>else</code> statement wasn't reached and continuing was never printed!\n",
    "\n",
    "After these brief but simple examples, you should feel comfortable using <code>while</code> statements in your code.\n",
    "\n",
    "**A word of caution however! It is possible to create an infinitely running loop with <code>while</code> statements. For example:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# DO NOT RUN THIS CODE!!!! \n",
    "while True:\n",
    "    print(\"I'm stuck in an infinite loop!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "A quick note: If you *did* run the above cell, click on the Kernel menu above to restart the kernel!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "\n",
    "<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>\n",
    "___\n",
    "<center><em>Content Copyright by Pierian Data</em></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Useful Operators\n",
    "\n",
    "There are a few built-in functions and \"operators\" in Python that don't fit well into any category, so we will go over them in this lecture, let's begin!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## range\n",
    "\n",
    "The range function allows you to quickly *generate* a list of integers, this comes in handy a lot, so take note of how to use it! There are 3 parameters you can pass, a start, a stop, and a step size. Let's see some examples:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(0, 11)"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(0,11)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that this is a **generator** function, so to actually get a list out of it, we need to cast it to a list with **list()**. What is a generator? Its a special type of function that will generate information and not need to save it to memory. We haven't talked about functions or generators yet, so just keep this in your notes for now, we will discuss this in much more detail in later on in your training!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Notice how 11 is not included, up to but not including 11, just like slice notation!\n",
    "list(range(0,11))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(0,12))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 2, 4, 6, 8, 10]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Third parameter is step size!\n",
    "# step size just means how big of a jump/leap/step you \n",
    "# take from the starting number to get to the next number.\n",
    "\n",
    "list(range(0,11,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(0,101,10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## enumerate\n",
    "\n",
    "enumerate is a very useful function to use with for loops. Let's imagine the following situation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "At index 0 the letter is a\n",
      "At index 1 the letter is b\n",
      "At index 2 the letter is c\n",
      "At index 3 the letter is d\n",
      "At index 4 the letter is e\n"
     ]
    }
   ],
   "source": [
    "index_count = 0\n",
    "\n",
    "for letter in 'abcde':\n",
    "    print(\"At index {} the letter is {}\".format(index_count,letter))\n",
    "    index_count += 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Keeping track of how many loops you've gone through is so common, that enumerate was created so you don't need to worry about creating and updating this index_count or loop_count variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "At index 0 the letter is a\n",
      "At index 1 the letter is b\n",
      "At index 2 the letter is c\n",
      "At index 3 the letter is d\n",
      "At index 4 the letter is e\n"
     ]
    }
   ],
   "source": [
    "# Notice the tuple unpacking!\n",
    "\n",
    "for i,letter in enumerate('abcde'):\n",
    "    print(\"At index {} the letter is {}\".format(i,letter))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## zip\n",
    "\n",
    "Notice the format enumerate actually returns, let's take a look by transforming it to a list()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(enumerate('abcde'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It was a list of tuples, meaning we could use tuple unpacking during our for loop. This data structure is actually very common in Python , especially when working with outside libraries. You can use the **zip()** function to quickly create a list of tuples by \"zipping\" up together two lists."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "mylist1 = [1,2,3,4,5]\n",
    "mylist2 = ['a','b','c','d','e']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<zip at 0x1d205086f08>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# This one is also a generator! We will explain this later, but for now let's transform it to a list\n",
    "zip(mylist1,mylist2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(zip(mylist1,mylist2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To use the generator, we could just use a for loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "For this tuple, first item was 1 and second item was a\n",
      "For this tuple, first item was 2 and second item was b\n",
      "For this tuple, first item was 3 and second item was c\n",
      "For this tuple, first item was 4 and second item was d\n",
      "For this tuple, first item was 5 and second item was e\n"
     ]
    }
   ],
   "source": [
    "for item1, item2 in zip(mylist1,mylist2):\n",
    "    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## in operator\n",
    "\n",
    "We've already seen the **in** keyword during the for loop, but we can also use it to quickly check if an object is in a list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'x' in ['x','y','z']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'x' in [1,2,3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## not in\n",
    "\n",
    "We can combine **in** with a **not** operator, to check if some object or variable is not present in a list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'x' not in ['x','y','z']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'x' not in [1,2,3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## min and max\n",
    "\n",
    "Quickly check the minimum or maximum of a list with these functions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "mylist = [10,20,30,40,100]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min(mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max(mylist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## random\n",
    "\n",
    "Python comes with a built in random library. There are a lot of functions included in this random library, so we will only show you two useful functions for now."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from random import shuffle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# This shuffles the list \"in-place\" meaning it won't return\n",
    "# anything, instead it will effect the list passed\n",
    "shuffle(mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[40, 10, 100, 30, 20]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mylist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from random import randint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Return random integer in range [a, b], including both end points.\n",
    "randint(0,100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "91"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Return random integer in range [a, b], including both end points.\n",
    "randint(0,100)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## input"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Something into this box: great job!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'great job!'"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "input('Enter Something into this box: ')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "\n",
    "<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>\n",
    "___\n",
    "<center><em>Content Copyright by Pierian Data</em></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# List Comprehensions\n",
    "\n",
    "In addition to sequence operations and list methods, Python includes a more advanced operation called a list comprehension.\n",
    "\n",
    "List comprehensions allow us to build out lists using a different notation. You can think of it as essentially a one line <code>for</code> loop built inside of brackets. For a simple example:\n",
    "## Example 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Grab every letter in string\n",
    "lst = [x for x in 'word']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['w', 'o', 'r', 'd']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check\n",
    "lst"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is the basic idea of a list comprehension. If you're familiar with mathematical notation this format should feel familiar for example: x^2 : x in { 0,1,2...10 } \n",
    "\n",
    "Let's see a few more examples of list comprehensions in Python:\n",
    "## Example 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Square numbers in range and turn into list\n",
    "lst = [x**2 for x in range(0,11)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Example 3\n",
    "Let's see how to add in <code>if</code> statements:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Check for even numbers in a range\n",
    "lst = [x for x in range(11) if x % 2 == 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 2, 4, 6, 8, 10]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Example 4\n",
    "Can also do more complicated arithmetic:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[32.0, 50.0, 68.18, 94.1]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert Celsius to Fahrenheit\n",
    "celsius = [0,10,20.1,34.5]\n",
    "\n",
    "fahrenheit = [((9/5)*temp + 32) for temp in celsius ]\n",
    "\n",
    "fahrenheit"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Example 5\n",
    "We can also perform nested list comprehensions, for example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst = [ x**2 for x in [x**2 for x in range(11)]]\n",
    "lst"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Later on in the course we will learn about generator comprehensions. After this lecture you should feel comfortable reading and writing basic list comprehensions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "\n",
    "<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>\n",
    "___\n",
    "<center><em>Content Copyright by Pierian Data</em></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# Statements Assessment Test\n",
    "Let's test your knowledge!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_____\n",
    "**Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "st = 'Print only the words that start with s in this sentence'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Code here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "______\n",
    "**Use range() to print all the even numbers from 0 to 10.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Code Here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "**Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Code in this cell\n",
    "[]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_____\n",
    "**Go through the string below and if the length of a word is even print \"even!\"**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "st = 'Print every word in this sentence that has an even number of letters'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Code in this cell"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "____\n",
    "**Write a program that prints the integers from 1 to 100. But for multiples of three print \"Fizz\" instead of the number, and for the multiples of five print \"Buzz\". For numbers which are multiples of both three and five print \"FizzBuzz\".**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Code in this cell"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "____\n",
    "**Use List Comprehension to create a list of the first letters of every word in the string below:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "st = 'Create a list of the first letters of every word in this string'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Code in this cell"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Great Job!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "\n",
    "<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>\n",
    "___\n",
    "<center><em>Content Copyright by Pierian Data</em></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# Statements Assessment Solutions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_____\n",
    "**Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "st = 'Print only the words that start with s in this sentence'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "start\n",
      "s\n",
      "sentence\n"
     ]
    }
   ],
   "source": [
    "for word in st.split():\n",
    "    if word[0] == 's':\n",
    "        print(word)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "______\n",
    "**Use range() to print all the even numbers from 0 to 10.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 2, 4, 6, 8, 10]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(0,11,2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "**Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x for x in range(1,51) if x%3 == 0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_____\n",
    "**Go through the string below and if the length of a word is even print \"even!\"**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "st = 'Print every word in this sentence that has an even number of letters'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "word <-- has an even length!\n",
      "in <-- has an even length!\n",
      "this <-- has an even length!\n",
      "sentence <-- has an even length!\n",
      "that <-- has an even length!\n",
      "an <-- has an even length!\n",
      "even <-- has an even length!\n",
      "number <-- has an even length!\n",
      "of <-- has an even length!\n"
     ]
    }
   ],
   "source": [
    "for word in st.split():\n",
    "    if len(word)%2 == 0:\n",
    "        print(word+\" <-- has an even length!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "____\n",
    "**Write a program that prints the integers from 1 to 100. But for multiples of three print \"Fizz\" instead of the number, and for the multiples of five print \"Buzz\". For numbers which are multiples of both three and five print \"FizzBuzz\".**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "for num in range(1,101):\n",
    "    if num % 3 == 0 and num % 5 == 0:\n",
    "        print(\"FizzBuzz\")\n",
    "    elif num % 3 == 0:\n",
    "        print(\"Fizz\")\n",
    "    elif num % 5 == 0:\n",
    "        print(\"Buzz\")\n",
    "    else:\n",
    "        print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "____\n",
    "**Use a List Comprehension to create a list of the first letters of every word in the string below:**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "st = 'Create a list of the first letters of every word in this string'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[word[0] for word in st.split()]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Great Job!"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
