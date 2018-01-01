# AutomataPY
# Introduction
  - Searching in XML structure to satisfy input tregex 
	-	Input: Data XML , Term to search in data XML
	-	Output: file result show xml structure satisfy term 
# Algorism
- Create Automata machine by term input : 
  - Function: cre_auto(params: term input):
    - Create Alphabet
    - Create transitions, states and final state
- Check data xml input with automata machine was created above:
  - Function: check(params: automata, data)
    - Data is array tree structure.
    - array stack = []
    - Foreach item in data: 
      - IF (item has in automata['alphabet']){
          - check arity of item 
          - If (item['arity'] == 0) : 
            - Check transition of item 
              - If(true)->Push item into stack
              - Else return false
          - Else {
            - pop number of elements equal arity from stack array
            - Check transition of item with element arity
            - If(true) -> Push item into stack
            - Else return false
            
      - ELSE return false
        
- Algorism of function cre_auto:
  - Create Alphabet: function alpha(params: term input)
		- Tranform term input to 2 dimension array => depend on array above => determind arity of each letter in alphabet
   	-	Example: term input: f(g(a),a) => 2 dimension array is [[f,g,a],[g,a]] => output of function alphabet is [f:2,g:1,a:0]
   	-	Create 5 array symbols[], query[], check[], result[] and stack[]
		-	symbols[] = [f,g,a,a]
		-	query[]	=  [f,(,g,(,a,),a]
		-	stack[] = []
		-	result[] = []
		-	check[] = [] (this array is to get letter which has arity != 0)
		- Create 1 object alphabet {}
	-	while(length(query)>1){
		-	pop item from query
		-	If(item != "(" )
			-	push to stack
		-	Else {
			-	create array k[]
			-	push to k[] last element in query[] (Ex: item == "(" stack[] = [a,),a], last element of query is "g")
			-	while (last element of stack != ")")
				-	pop last element of stack
				-	push this to k[] 
				(finish while loop, k[] = [g,a])
			-	pop item ")"
			-	push k[] into result[]
			
		- Foreach item of result[]
			- push item[0] into check[] 
		
		- Foreach symbol in symbols[]
			-	If(has symbol in check[]): alphabet->symbol = length(check[index (has value == symbol)]) - 1 (Get arity of item)
			-	Else alphabet->symbol = 0;
			
		- return alphabet {}
# Using
  - Language : Python3
