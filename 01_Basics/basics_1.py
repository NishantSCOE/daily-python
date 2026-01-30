# How python program executes

"""

1.python program
  program.py
which is called as 'Source Code'

compiled using python compiler

2.python compiled file
  program.pyc
which is called as 'Byte Code'

run using python virtual machine (PVM)

3.Machine Code

Compiled file is then converted to machine code in 0s and 1s so machine can understand it and then processor does the action

we can see the output on the computer screen


we cannot see .pyc file in folder as it all internally completed and only result is shown on screen

to create separate .pyc file

python -m py_compile program.py

above command can be used to make a compiled file of our program


to see byte code we can use the following command
python -m dis program.py
-m for module 
dis for 'disassembler' which converts byte code to human readable format

"""

a = int(input('Dont enter anything: '))
b = int(input('Dont enter anything: '))
print(a+b)