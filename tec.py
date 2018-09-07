#!/usr/bin/python
suma=4+6

def resultado(suma):
	if suma == 10:
		print('''La suma es correcta es %s''') % str(suma)
	else:
		print('''La suma no es igual a %s''') % string(suma)

def test_suma():	
	assert resultado(10) != 10
	