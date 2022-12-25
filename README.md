# Roll - Dice roller for your command line
Have you ever asked yourself why your terminal can't roll a set of dice?

Sometimes you want to play a tabletop game and haven't dice at your fingertips?

Sometimes you want to play but do not have enough space to set up a table for it?

What? Never? Sure? You make a point.

**BUT**

If you have answered yes to at least one of these questions, "roll" is a tool that can help you!

## The idea
The idea at the base of "roll" is to remove the dice component from your games and move it to your computer. For now, works in your terminal, but planning to make a web page and, maybe, an app so you can use it also on your phone, tablet, smartwatch, or whatever.

Now you are thinking: *"why to use this and not any other dice roller on the web?"* the answer is simple... You are already here, and the install instructions are just a few lines down. Why lose other time searching for another dice roller?

  

## Instructions

### Dependencies
  1.  Colorama 

### How to install
  1.  Clone the repository
  2.  Make the file "roll.py" available by adding it to your path or creating an alias
  3.  Enjoy
### How to use
The command to use is:

    roll [n]d[max][mod]

This tool, to roll a dice, parses a list of strings that following this syntax:
*n*d*max***mod**
> Use **roll** without any argoument will use *1d6+0* as default dice string

Where:
-   **n** is for the number of rolls, is an integer, default 1, *so d[max] is still a **valid** input*
-   **max** is the number of faces of the dice (so the max number you can get from a roll)
-   **mod** is for the modifiers

and return the sum of the rolls + the modifiers

Available modifiers:

-   **+m**, to add m to the total
-   **-m**, to subtract m from the total

#### Examples:
Input: 

    > roll
Output: 

    ================================
    Number of Dices: 1
    Range: 6
    Roll #1: 2
    
    Total: 2 = 2
    ================================



Input:

    ❯ roll d6 3d12-3 2d20+6
Ouput:

    ================================
    Number of Dices: 1
    Range: 6
    Roll #1: 4
    
    Total: 4 = 4
    ================================
    ================================
    Number of Dices: 3
    Range: 12
    Bonus or Malus: -3
    Roll #1: 2
    Roll #2: 5
    Roll #3: 7
    
    Total: 2+5+7-3 = 11
    ================================
    ================================
    Number of Dices: 2
    Range: 20
    Bonus or Malus: +6
    Roll #1: 15
    Roll #2: 19
    
    Total: 15+19+6 = 40
    ================================
