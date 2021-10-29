# graph_rigidity_checker
A simple user-friendly Python program for checking if a graph is rigid and globally rigid.

To use, run the python script graph_build_interface.py. 
This will open up a terminal window and an interactable screen where you can draw your desired graph.
To do so, just follow the basic instructions in the terminal window.

To check whether your graph is rigid, the program generates a random realisation of your desired graph and then checks whether its rigidity matrix has the correct rank.
To check whether your graph is globally rigid, the program generates a random realisation of your desired graph,
finds a random stress of the realisation and then checks whether the realisation is both infinitesimally rigid and the stress has the correct rank.
