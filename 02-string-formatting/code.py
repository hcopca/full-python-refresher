name = "Hugo"
greeting = (f"Hello, {name}")

# print(greeting)

name = "Hugo2"
greeting = (f"Hello, {name}")
# print(greeting)

#TemplateStrings

name = "Bob"

greeting = "Hola, {}"

with_name = greeting.format(name)
# print(with_name)

with_name2 = greeting.format("Rodolfo")
# print(with_name2)


# LongPhrase

longer_phrase =  "Hello {}, today is {}."

formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)