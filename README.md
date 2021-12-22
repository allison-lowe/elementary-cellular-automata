elementary cellular automata is the most rudimentary class of one-dimensional automata. they have two possible values for each cell (0 or 1). the state of a cell is calculated by the state of its closest neighboring cells. simply put, an elementary cellular automata can be described as a table which the next generation of a cell is based on the values of the left neighbor, right neighbor, and the cell itself.

each of these three cells is interpreted as a single bit. with two possible values for each bit (0 or 1), there are 8 possible binary states for the three observed cells and 256 possible rules.

the binary state of the three observed cells operates as an indexing mechanism for the rule.

as an example, let's calculate rule 100. first, we find the binary expression of 100. this value is 01100100. next, let's observe a set of cells. here we go: a set of three cells. left-most bit 1, center bit 1, right-most bit 0. we can interpret this set as a binary state. reading left to right, this would be 110. now, converting to decimal, we get 6. this means that the new cell will receive it's value from the 6th index of the 8 bit rule we have previously defined. 01100100 -> 0(1)100100. the 6th bit of our rule is 1, so consequently the child cell will also be a 1.

this calculation is completed for each cell of the grid. once the calculation for a rule is complete, the program increments to the next rule and repeats.
