# Algorithms & Visualizations

* Implementing algorithms from Princeton Algorithms 1 with Python
* Trying to go the extra mile to visualize algorithm operation and/or results whenever possible
* Trying to concurrently learn PyTest by writing tests for the implementations

## Table of Contents

* [Algorithms & Visualizations](#algorithms--visualizations)
    * [Union Find](#union-find)
	    * [Execution Instructions](#execution-instructions)
		* [Algorithm Functionality](#algorithm-functionality)

## Union Find
Implementation based on [Assignment 1 - Percolation](http://coursera.cs.princeton.edu/algs4/assignments/percolation.html)
#### Execution Instructions
1. Install required tree visualization package
> pip install pydotplus
2. Install the GraphViz backend using the installer found in the install_files folder. If the installation directory is not 'C:/Program Files (x86)/Graphviz2.38/bin/', then modify the GRAPHVIZ_BIN_PATH variable in config.py
#### Algorithm Functionality
1. **union_find.py** - implemented using the [*Weighted Quick Union optimization*](https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/WeightedQuickUnionUF.html)
* **union**: connects two objects from a set of n objects
* **connected**: determines whether two objects are connected
2. **union_find_percolation.py** - identifies whether a given input percolates
* **read_input**: reads in the size of the grid and the coordinates of the activated (i.e. on) objects
* **link_top_bottom**: helper function that links top nodes to a single node and bottom nodes to a single node
* **connect_surrounding**: connect activated nodes to adjacent activated nodes
* **ParseResult**: extracts trees from array representation of node relationships
* **DrawTree**: visualizes the parsed trees using pydot and saves the output in /output_files/percolation/
(see example trees from Monte Carlo Percolation simulations in the example_output folder)

3. **union_find_percolation_monte_carlo.py** - uses Monte Carlo simulations to estimate the theoretical [*percolation threshold*](http://mathworld.wolfram.com/PercolationThreshold.html)
* **simulate_percolation**: generates a random sequence of objects to activate, checks for percolation at each object activation, and returns the percolation threshold once percolation is detected
* **visualize_activated**: visualizes the grid of activated and non-activated objects


