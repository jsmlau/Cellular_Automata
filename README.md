## Welcome 👋
> Display one-dimensional 8-bit or 32-bit rule Automaton</br>

## Elementary Cellular Automaton
![ElementaryCA30Rules_750](https://mathworld.wolfram.com/images/eps-gif/ElementaryCA30Rules_750.gif)</br>
 Elementary cellular automata have two possible values for each cell (0 or 1), and rules that depend only on nearest neighbor values. As a result, the evolution of an elementary cellular automaton can completely be described by a table specifying the state a given cell will have in the next generation based on the value of the cell to its left, the value the cell itself, and the value of the cell to its right. Since there are 2×2×2=2^3=8 possible binary states for the three cells neighboring a given cell, there are a total of 2^8=256 elementary cellular automata, each of which can be indexed with an 8-bit binary number (Wolfram 1983, 2002). For example, the table giving the evolution of rule 30 (30=00011110_2) is illustrated above. In this diagram, the possible values of the three neighboring cells are shown in the top row of each panel, and the resulting value the central cell takes in the next generation is shown below in the center. n generations of elementary cellular automaton rule r are implemented as CellularAutomaton[r, {{1}, 0}, n].


## Usage
```sh
python3 cellular_automata.py
```
## Output
![automata_output](https://user-images.githubusercontent.com/37385743/88640488-e1b7f500-d072-11ea-82e3-2a2014b07e48.png)

## Author

👤 **Jas Lau**

* Twitter: [@jsmlau](https://twitter.com/jsmlau)
* Github: [@jsmlau](https://github.com/jsmlau)

## Show your support

Give a ⭐️ if this project helped you!

## References
[Cellular Automaton](https://mathworld.wolfram.com/CellularAutomaton.html)</br>
[Elementary Cellular Automaton](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html)

***
