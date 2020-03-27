from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title


"""First test, then proceed. Like a goat
who steps only one leg each time,
which can climb on top of pracarious tree,
always listen to the voice of 
innter goat bleating "test first, test first!"
"""