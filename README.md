# graph-rigidity-checker
(Requires pygame, scipy, numpy and lnumber packages.)

A simple user-friendly Python program for checking if a graph is rigid or globally rigid.
It can also check the adjacency and Laplacian matrix eigenvalues.

To use, run the python script graph_build_interface.py. 
This will open up a terminal window and an interactable screen where you can draw your desired graph.
To do so, just follow the basic instructions in the terminal window.

To check whether your graph is rigid, the program generates a random realisation of your desired graph and then checks whether its rigidity matrix has the correct rank.
To check whether your graph is globally rigid, the program generates a random realisation of your desired graph,
finds a random stress of the realisation and then checks whether the realisation is both infinitesimally rigid and the stress has the correct rank.

The graph will be described as a dictionary object in the terminal window every time an edge is added to the graph.
This can then be directly copied into other Python scripts easily.

FEATURE UPDATE 22/3/2023:
Program can now compute the drawn graph's number representation as described in
'The number of realizations of all Laman graphs with at most 12 vertices' 
by Jose Capco, Matteo Gallet, Georg Grasegger, Christoph Koutschan, Niels Lubbes and Josef Schicho (DOI: 10.5281/zenodo.1245517).

FEATURE UPDATE 12/3/2024:
Program can now compute the drawn graph's planar and spherical realisation numbers using the lnumber package:
'Toolkit for Computing the Laman Number' 
by Jose Capco (DOI: 10.5281/zenodo.8301012).
The GitHub repository for this package is found at https://github.com/jcapco/lnumber
