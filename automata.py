import xml.etree.ElementTree as ET
import re 
#input_string = "country(rank,year,gdppc,dm(minh,tri),neighbor,neighbor)||country(rank,year,gdppc,neighbor,neighbor) "
#input_string = "check(check1(check2),check3(check4,check5))"
#input_string = input_string.split('||')

#string = "country.rank > 50"
#query =query.partition("(")
"""file = open('data.xml','r')
tree = ET.ElementTree()
tree.parse(file)
p =tree.findall('')
#(p)"""

def alpha(query):
	final = []
	s =[]
	alphabet= {}
	check = []
	final_states = []
	symbols = re.findall(r"[A-Za-z0-9]+", query)
	query = re.findall(r"[A-Za-z0-9]+|\(|\)", query)
	while (len(query)>0):
		symbol = query.pop()
		#print (symbol)
		if (symbol != '('):
			s.append(symbol)
		if (symbol == '('):
			k = []
			#print (query[-1])
			k.append(query[-1])
			while (s[-1] !=')'):
				k.append(s.pop())
			s.pop()
			final.append(k)
	for i in range(0,len(final)):
		check.append(final[i][0])

	for symbol in symbols:
			if (symbol in check):			
				alphabet[symbol]=len(final[check.index(symbol)])-1
			else :
				alphabet[symbol]=0
	###print(alphabet)
	return(alphabet)

def cre_auto(query):
	alphabet = alpha(query)
	symbols = re.findall(r"[A-Za-z0-9]+", query)
	s = []
	a = list(alphabet.values())
	auto = {}
	###print (alphabet)
	auto['alphabet'] = alphabet
	final_states = []
	trans = [[]for i in range(0,max(a)+1)]
	while (len(symbols)>1):
		symbol = symbols.pop()
		k = symbol
		if (alphabet[symbol] == 0):
			k = k,symbol+"0000"
			s.append(symbol+"0000")
			trans[0].append(k)			
		else :
			arity = alphabet[symbol]
			pre_s = (s.pop(),)
			for i in range(1,arity):
				pre_s = pre_s+(s.pop(),)
			k = pre_s+(k,)
			d_state = ''.join(k)
			k = k+(d_state,)
			s.append(d_state)	
			trans[arity].append(k)
	symbol = symbols.pop()
	k = symbol
	if (alphabet[symbol] == 0):
		k = k,symbol+"0000"
		s.append(symbol+"0000")
		trans[0].append(k)			
	else :
		arity = alphabet[symbol]
		pre_s = (s.pop(),)
		for i in range(1,arity):
			pre_s = pre_s+(s.pop(),)
		# (pre_s)
		k = pre_s+(k,)
		#(k)
		d_state = ''.join(k)
		k = k+(d_state,)
		final_states.append(d_state)	
		trans[arity].append(k)
	for t in trans:	
		t = sorted(t)
		t = [t[i] for i in range(len(t)) if i == 0 or t[i] != t[i-1]]
	auto['trans'] = trans
	auto['final_states'] = final_states
	
	return auto
def trans(t,symbol,pre_states):
  pre_states.append(symbol)
  # ("pre_states:",pre_states)
  states = [k[-1] for k in t if pre_states==list(k)[:-1]]
  return states
def check(auto,term):
	try:
	    symbols = term
	    #auto = cre_auto(query)
	    ###print (auto)
	    transitions = auto['trans']
	    alpha = auto['alphabet']
	    ##print (alpha)
	    final_states = auto['final_states']
	    s_states = [[]]
	    while len(symbols)> 0:
	      minh_states = []
	      symbol = symbols.pop()
	      ###print (symbol)
	      t =[]
	      s = []
	      #lay prevstates ra
	      for i in range(0,len(s_states)):
	        minh_states.append(s_states[i])
	      #(minh_states)
	      for s_state in s_states:
	        minh_states[minh_states.index(s_state)] = s_state
	        if alpha[symbol] == 0:
	          t=trans(transitions[alpha[symbol]],symbol,[])
	          # (t)
	        else :
	          p_states = []
	          ##print (s_state)
	          for i in range(0,alpha[symbol]):
	            p_states.append(s_state.pop())
	          t=trans(transitions[alpha[symbol]],symbol,p_states) 
	        # (t)
	        if len(t) == 0 :
	            minh_states.remove(s_state)
	            #("sida")
	        elif len(t) == 1 :
	          s_state.append(t[0])

	        else :
	          s=[s_state[i] for i in range(len(s_state))]
	          s_state.append(t[0])
	          for k in range(1,len(t)):
	            k = s + [t[k]]
	            minh_states.insert(0,k)
	      #("s:" , s)
	      s_states = minh_states
	      s_states = sorted(s_states)
	      s_states = [s_states[i] for i in range(len(s_states)) if i == 0 or s_states[i] != s_states[i-1]]    
	      #("s_states : ",s_states)
	      #("-----------"+"-------------")

	        
	    for l in s_states:
	      for k in final_states:
	        if l == [k] :
	          return True
	    return False
	except:
		#print('opps')
		return False

#input_string = input_string.split('||')
def run():
	input_string = "country(rank,year,gdppc,ten(minh,tri),neighbor,neighbor)"

	input_string = input_string.split('||')
	output = open('output.xml','w')
	output.write('<result>')
	##print(input_string)
	for s in input_string:
		symbols = re.findall(r"[A-Za-z0-9]+", s)
		auto = cre_auto(s)
		#print(auto)
		#print (auto)
		file = open('data1.xml','r')
		#except :
			# ("Oops!")
		#	return False
		tree = ET.parse(file)
		##print(symbols[0])
		p =tree.getroot().findall('.//'+symbols[0])
		#print(symbols[0])
		#print(p)
		
		for k in p: 
			heheh = k.iter()
			#print ("-------------------")
			alpha = {}
			for c in heheh:
				alpha[c.tag] = len(list(c))
			#print(alpha)
			try:
				for key in alpha:
					if auto['alphabet'][key] != alpha[key]:
						
						continue
			except:
				continue
			t = [elem.tag for elem in k.iter()]
			#print (t)
			if (check(auto,t)):
				output.write(ET.tostring(k))
	output.write('</result>')
	output.close()
		
run()
#result.write('output.xml')
###print(p)
		
