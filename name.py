#2-4

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
 
 #f-strings
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!" 
print(message)

# Adding Whitespace to Strings with Tabs or Newlines
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace - rstrip(), lstrip()
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

# Removing Prefixes
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
print(nostarch_url)
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)