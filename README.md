# text-gen-Markov     

## Description 

A simple simple that uses text files to build a markov chain k-gram to then generate some text.  

## Purpose

The purpose was to learn about markov chains and some of their applications. 

## Setup

`git clone https://github.com/Hweinstock/text-gen-Markov.git`    
  
Now try testing to out with the help menu:  
  
`python3 generate.py -h`  

## Usage

Here is the help menu for arguments.   
```
usage: generate.py [-h] -f  [-k] [-l]

optional arguments:
  -h, --help          show this help message and exit
  -f , --learn_file   Path to a .txt file to build the markov chain model to
                      emulate text.
  -k , --k_gram       argument describing what length to group the text into
                      for the markov model. Smaller values means the model
                      looks at looks at less characters to predict the next
                      one, whereas higher numbers look cause the model to look
                      at more characters to predict the next one.
  -l , --length       how many characters the program should generate.
```
An example call could look like this,  
`python generate.py -f data/shakespeare.txt -k 8`  

## Data

There is a large amount of example data files in the `/data` directory but feel free to have the program build its markov model  
based on any text, even your own writing. Be aware, the more text you give it, the more accurate and interesting it will be.  
