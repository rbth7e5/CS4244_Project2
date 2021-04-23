# CS4244_Project2

Usage: `python3 main.py <model> <evidence>`\
`model` should have file extension `.uai`\
`evidence` should have file extension `.uai.evid`

Output:
1. CNF formula in DIMACS format
2. Weight file with the relevant mappings

Assumptions:
1. Domain of variables will always be 2

Note:
1. Please make sure the input model file is of type MARKOV even if it is BAYES

## Encoding

Number of Indicator Variables = Number of nodes in the graph\
Number of Parameter Variables = Total number of rows of all CPT / 2

Referring to the example given in class, here are the encodings:
* I<sub>R</sub> &#10231; Q<sub>R</sub>
* I<sub>S</sub> &#10231; Q<sub>S</sub>
* (I<sub>R</sub> &#8743; I<sub>S</sub> &#8743; I<sub>G</sub>) &#10231; Q<sub>RSG</sub>)
* (I<sub>R</sub> &#8743; I<sub>S</sub> &#8743; &#172;I<sub>G</sub>) &#10231; &#172;Q<sub>RSG</sub>)
* (I<sub>R</sub> &#8743; &#172;I<sub>S</sub> &#8743; I<sub>G</sub>) &#10231; Q<sub>RS&#773;G</sub>)
* (I<sub>R</sub> &#8743; &#172;I<sub>S</sub> &#8743; &#172;I<sub>G</sub>) &#10231; &#172;Q<sub>RS&#773;G</sub>)
* (&#172;I<sub>R</sub> &#8743; I<sub>S</sub> &#8743; I<sub>G</sub>) &#10231; Q<sub>R&#773;SG</sub>)
* (&#172;I<sub>R</sub> &#8743; I<sub>S</sub> &#8743; &#172;I<sub>G</sub>) &#10231; &#172;Q<sub>R&#773;SG</sub>)
* (&#172;I<sub>R</sub> &#8743; &#172;I<sub>S</sub> &#8743; <sub>G</sub>) &#10231; Q<sub>R&#773;S&#773;G</sub>)
* (&#172;I<sub>R</sub> &#8743; &#172;I<sub>S</sub> &#8743; &#172;I<sub>G</sub>) &#10231; &#172;Q<sub>R&#773;S&#773;G</sub>)

The weights are:
* W(I<sub>R</sub>) = W(I<sub>S</sub>) = W(I<sub>G</sub>)= 1
* W(&#172;I<sub>R</sub>) = W(&#172;I<sub>S</sub>) = W(&#172;I<sub>G</sub>)= 0
* W(Q<sub>R</sub>) = 0.2, W(&#172;Q<sub>R</sub>) = 1 - 0.2 = 0.8
* W(Q<sub>S</sub>) = 0.6, W(&#172;Q<sub>S</sub>) = 1 - 0.6 = 0.4
* W(Q<sub>RSG</sub>) = 0.9, W(&#172;Q<sub>RSG</sub>) = 1 - 0.9 = 0.1
* W(Q<sub>RS&#773;G</sub>) = 0.8, W(&#172;Q<sub>RS&#773;G</sub>) = 1 - 0.8 = 0.2
* W(Q<sub>R&#773;SG</sub>) = 0.7, W(&#172;Q<sub>R&#773;SG</sub>) = 1 - 0.7 = 0.3
* W(Q<sub>R&#773;S&#773;G</sub>) = 0.4, W(&#172;Q<sub>R&#773;S&#773;G</sub>) = 1 - 0.4 = 0.6
