![Solar Logo](https://github.com/Solar-language/Solar/blob/master/media/solar-logo.png?raw=true)

# Solar Docs - Reserved Names

The official solar documentation designed so the team knows what is going on and so that you can learn the language.

## Table of Contents

- [About Solar](#about-solar)
- [Reserved Names](#reserved-names)
	- [Keywords](#keywords)
	- [Reserved Function Names](#reserved-function-names)
## About Solar

Solar is a Lisp-Style language that uses built-in functions to run everything, making the syntax easy to pick up and not take up too much space.

## Reserved Names

In the topic of reserved names, we will split it up into two parts: Keywords and Reserved Function Names, we will start with the smaller Keywords.

### Keywords
These reserved names below are neither functions nor variables; rather they are keywords built in to the language:

| Name   | Usage                   | Implemented? |
|:------:|:-----------------------:|:------------:|
|true|True boolean value|Yes|
|false|False boolean value|Yes|
|null|Null value|Yes|


### Reserved Function Names

| Name   | Usage                   | Implemented? |
|:------:|:-----------------------:|:------------:|
|        |**Operators**            |    |
|+       |Add                      | Yes|
|-       |Subtract                 | Yes|
|*       |Multiply                 | Yes|
|/       |Divide                   | Yes|
|%       |Modulo                   | Yes|
|=       |Equal                    | Yes|
|!=      |Not equal                | Yes|
|>       |Greater Than             | Yes|
|<       |Less Than                | Yes|
|>=      |Greater Than or Equal To | Yes |
|<=      |Less Than or Equal To    | Yes|
|        |**Variables**         |    |    
|def     |Declare a variable       | Yes |
|set     |Reassign a variable      | Yes |
|append  |Append to a list.        | Yes |
|index   |Get the *n*th value in a list| Yes |
|        |**Control flow**         |    |
|if      |If expression.           | Yes |
|elif    |May follow an if expression| Yes |
|else    |May follow an if or elif expression|Yes|
|while   |While expression         |Yes  |
|        |**Converters**           |    |
|lambda  |Creates a lambda object  |Yes  |
|list    |Return all parameters as a list| Yes |
|int     |Convert to Integer       | Yes|
|str     |Convert to String        | Yes|
|float   |Convert to Float         | Yes|
|bool    |Convert to Bool          | Yes|
|lower   |Convert to Lowercase     | Yes|
|upper   |Convert to Uppercase     | Yes|
|encode  |Convert Text to Unicode  | Yes|
|decode  |Convert Unicode to Text  | Yes|
|        |**I/O**                  |    |
|put     |Print output without new line            | Yes|
|print    |Print output             | Yes|
|get     |Read a line of input from stdin| Yes |
|open     |Open a file| Yes |
|read     |Read from an open file.| Yes |
|readline     |Read a line from an open file.| Yes |
|readlines     |Returns a list with all the lines in a file| Yes |
|argv     |Returns a list with all the command-line arguments| Yes |
|        |**Other**               |    |
|raise   |Raise a SolarError   | Yes |
|datetime   |Returns the date and/or time   | Yes |
|random   |Returns a pseudo-random number   | Yes |


More coming soon...

- The Solar Team

