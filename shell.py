import jani

while True:
	text = input('bolo jani kaya karna ha? > ')
	if text.strip() == "": continue
	result, error = jani.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
