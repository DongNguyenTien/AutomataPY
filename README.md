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

        
- Algorism of function cre_auto:
	-	Create Alphabet: function alpha(params: term input)
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
		
	-	Create transitions, states and final state: 
		-	Example: term input: f(g(a),a)
		-	symbols[] = [f,g,a,a]
		- alphabet: {f:2,g:1,a:0}
		- stack_state[] = []
		-	trans[] = array of arrays transitions
		-	final_state = ""
		- automata[] = [] (This is result return automata machine)
		-	While (length(symbols) > 1)
			-	pop item from symbols[]
			-	If (alphabet->item == 0) (Ex : alphabet->a == 0)
				-	push into stack_state[]: item+"0000"
				-	push into trans[0]: (item, item+"0000") (Ex: transition: item -> item"0000" , a -> a0000) 
			-	Else
				- arity = alphabet->item
				-	pre_state = (stack_state.pop,) (Ex, pre_state = a0000)
				-	for (i=1;i<arity;i++)
					-	pre_state = pre_State + stack.pop
				-	create k = pre_state + item (Ex: a0000,g)
				-	create d_state = join(k) (Ex: a0000g)
				-	push into stack_state[]: d_state
				-	push into trans[arity]: k + d_state (Ex: trans[arity] = (a0000,g,a0000g), this is transition: g(a0000)->a0000g)
				
				
		-	Pop last symbol of symbols[]
		-	If (alphabet->last_symbol == 0) (Ex : alphabet->a == 0)
				-	push into stack_state[]: item+"0000"
				-	push into trans[0]: (item, item+"0000") (Ex: transition: item -> item"0000" , a -> a0000) 
			-	Else
				- arity = alphabet->item
				-	pre_state = (stack_state.pop,) (Ex, pre_state = a0000)
				-	for (i=1;i<arity;i++)
					-	pre_state = pre_State + stack.pop
				-	create k = pre_state + item (Ex: a0000,g)
				-	create d_state = join(k) (Ex: a0000g)
				-	push into stack_state[]: d_state
				-	push into trans[arity]: k + d_state (Ex: trans[arity] = (a0000,g,a0000g), this is transition: g(a0000)->a0000g)
				- final_state = d_state
		
		
		-	automata[transition] = trans[]
		-	automata[fnal_state] = final_state
		
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
# Using
  - Language : Python3
  -	Put file automata.py, data1.xml in same directory
	- open terminal, 
		-	run command: cd to directory which has file automata.py
		-	run cmd: $ python automata.py
	- check result in output.xml
	- Just can adjust term input only in automata.py (input_string)
