---------------------------------------------------------------

       d8888   888b    888    .d8888b.    888      
      d88888   8888b   888   d88P  Y88b   888      
     d88P888   88888b  888   888    888   888      
    d88P 888   888Y88b 888   888          888      
   d88P  888   888 Y88b888   888  88888   888      
  d88P   888   888  Y88888   888    888   888      
 d8888888888   888   Y8888   Y88b  d88P   888      
d88P     888   888    Y888    "Y8888P88   88888888

Abrupt Numerical Graph Language

By Aries Powvalla
---------------------------------------------------------------

ANGLing Laws:
1. Every ANGL program operates on a 16x16 grid.
  a. From (1,1) at top left to (16,16) at bottom right.
2. Space values can span -128 to 128.
3. At the beginning of the program, the (1,1) tile is selected.
4. Commands can be used to manipulate the grid.

------------- Practical Usage Pros/Cons -------------

Pros:
Extremely low file size
Extremely minimal compiler
Moderately fast at industry standard

Cons:
Very complex syntax
Not expandable
Few use cases

----------------

BEST USAGES:
Mathematical Computation/Evaluation
Physics Computation
Fluid Dynamics

OK USAGES:
Non-classical Mathematics (Sub-Euclidian, Relativity Plot)
Root programming
ASCII Construction

BAD USAGES:
Games
Simulations
Graphics Host

TERRIBLE/IMPOSSIBLE USAGES:
Large-Scale implementation
Threaded Applications (Unless using Py or JS as mediator)
GPU Utilization


------------- Program Init -------------

Fully initializing your program is not required. Not initializing your program will simply set the following values:

projectname: AngledScript
projectauthor: Unknown
projectversion: v0.1
process_clock: 20
error_skipping: 0
parse_timeout: 100
builtin_visualizer: 0
alternate_complier: 0
max_cache: 6

In order to modify these options in your project, add the line as shown above to the beginning of the .angl file.

NOTE: ONLY LETTERS, NUMBERS, _, AND - CAN BE USED

After modifying settings if desired, a line should be left empty. The line following should contain a single start character, "!" (More below), and then the code can begin.

------------- Init Functions -------------

PROCESS CLOCK -- Milliseconds per tick. ANGL attempts to run at 10 operations per tick, but upon failing will fallback to the next multiple of ticks. Setting to 0 is not recommended as it disables the purpose of the space operation.

ERROR SKIPPING -- Whether errors stop the program and raise a callback or ignore the operation. 1 = SKIP, 0 = FLAG

PARSE TIMEOUT -- Milliseconds an operation is allowed to take to execute fully. Values above 120 are not recommended because if a function takes this long, something is probably broken.

BUILT-IN VISUALIZER -- Versions 1.3 and onward of ANGL will include a togglable visualizer of the 16x16 grid. Not yet implemented (CURRENTLY USEABLE THROUGH "~")

ALTERNATE COMPILER -- Whether an alternate compiler is used. Can be useful on unstable platforms, or if main compiler is broken for some reason. 0 = MAIN COMPILER, 1 = ALTERNATE COMPILER, -1 = ATTEMPT BOTH AND OUTPUT LEAST ERRORED BLOCK

MAX CACHE -- Maximum amount of operations allowed to be cached at a certain point in time. Decrease to free up resources but slow down large programs. 6 is sufficient for most devices (4GB RAM) and programs (<2k OPERATIONS).

------------- Operations -------------

Important notes: Some operations can handle multiple inputs/outputs, and some have a separate function for such cases. When the guide refers to a "selected" space, that is where the selector is currently placed. When the guide refers to a "saved" space, that is the position(s) previously saved using the (@) operation.

File Operations

! : Script start/end (Comments can be added only after the final "!" character.)


Movers

* : Move selector to (1,1).
v : Move selector down one space.
^ : Move selector up one space.
> : Move selector right one space.
< : Move selector left one space.


Selection

@ : Save to selector (STM).
_ : Deselect/Unsave (STM).


Selector Modifiers

Q : Expand selector by one space both down and right.
o : Shrink selector by one space both up and left.
q : Reset selector to 1x1.


Incrementors

+ : Adds one to the space(s) selected.
- : Subtracts one from the space(s) selected.
x : Resets space(s) selected to 0.
" : Doubles space(s) selected.
' : Halves space(s) selected.

a : Adds the saved spaces' value to the space(s) selected.
   > If saved and selected space amount match, they add correspondingly.
   > If amount of saved spaces are more than or less than amount of selected spaces, saved spaces are added together and the resulting value is added to each selected space.

s : Subtracts the saved spaces' value from the space(s) selected.
   > If saved and selected space amount match, they subtract correspondingly.
   > If amount of saved spaces are more than or less than amount of selected spaces, saved spaces are added together and the resulting value is subtracted from each selected space.

m : Multiplies the saved spaces' value and the spaces' value(s). Same rules apply.

d : Divides the saved spaces' value from the spaces' value(s). Same rules apply.

% : Performs the modulo of the selected space over the saved space. Same rules apply.

Self Incrementors

{ : Saves the value of all selected spaces' values added together.

} : Saves the value of all selected spaces' values subtracted, in order.

* : Saves the value of all selected spaces' values multiplied together.


Standard Outputters

p : Output raw data of spaces selected (Number/Array).
P : Output ASCII table conversion of SPACE (1) selected (ABSOLUTE VALUE).
m : Perform addition operation on selected SPACES (>1) and output number.
f : Perform subtraction operation on selected SPACES (>1) and output number (NEGATIVES ALLOWED).
M : Perform addition operation on selected SPACES (>1) and output ASCII.
F : Perform subtraction operation on selected SPACES (>1) and output ASCII (ABSOLUTE VALUE).


Other Ouputters/Savers

r : Output selected row.
c : Output selected column.
R : Save selected row.
C : Save selected column.


Functions

[_CODE_]# : Loop _CODE_ for # times.

d : Get numerical user input and insert as selected space(s) value.
D : Get 1 character user input, convert via ASCII, and insert as selected space(s) value.
u : Get numerical user input and save it.
U : Get 1 character user input, convert via ASCII, and save.

( : Move selector to the first instance of the saved number (Left-Right, Top-Bottom).
) : Move selector to the last instance of the saved number (Bottom-Top, Right-Left).

\ : Sets selected space to 1 if value of selected space is greater than value of saved space.
= : Sets current space to 1 if current space(s) matches saved value(s), otherwise set to 0. Same amount of tiles must be selected.


Miscellaneous

[space] : Halt for 10 ticks (200 ms by default).
[newline] : Deselect, Move to (1,1).
[double_newline] : Deselect, Move to (1,1), Reset all tiles to 0.
. : Lock space (Cannot be modified).
, : Unlock space (Can be modified).
# : Filler character
? : Move cursor in a random direction