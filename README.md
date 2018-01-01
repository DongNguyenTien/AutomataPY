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
- Check data xml input with automate machine was created above:
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
    
# Using
  - Language : Python3
