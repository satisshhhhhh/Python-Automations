#E-mail and phone number extractor
#---------------------------------

import pyperclip

import re

#Text containing email's and phone number to be pasted from clipboard
text = str(pyperclip.paste())
#Don't know how to navigate to clipboard?
"""
WINDOWS Users - To get to your clipboard history at any time, press Windows logo key + V. 
    You can also paste and pin frequently used items by choosing an individual item from your clipboard menu.
    To share your clipboard items across your Windows 10 devices, select Start > Settings > System > Clipboard.

MAC OS Users - You can find the Command key immediately left of your keyboard's space bar.
    When you select some text or an item on a Mac, pressing Command-C copies it to the clipboard, 
    where it will remain until you either copy it over with another item or selection or restart your Mac.

Linux Users - Incidentally, most of the time, if you want to Copy, Paste, and Cut, you use Ctrl-C, Ctrl-V, 
    and Ctrl-X respectively. If you're working in Bash at the command line, the shortcuts are 
    Shift-Ctrl-C, Shift-Ctrl-V, and Shift-Ctrl-X respectively.

"""
#Regular expression for phone numbers

phone_regex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?    # Non greedy approach for area code
	(\s|-|\.)?            # hypen or a dot (Phone number format) 
	(\d{3})               # first 3 digit
	(\s|-|\.)?            # seperator
	(\d{4})               # Last 4 digit
	)''', re.VERBOSE)

email_regex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+      # Username
	@                      # symbol
	[a-zA-Z0-9.-]+         # domain name
	(\.[a-z{2,4}])         # dot-something
	)''', re.VERBOSE)

match =[] # list for storing all the matched found

for groups in phone_regex.findall(text):
	phone_number = '-'.join([groups[1],groups[3],groups[5]])
	match.append(phone_number)

for groups in email_regex.findall(text):
	match.append(groups[0])

# Copy results to clipboard

if len(match)>0:
	pyperclip.copy('\n'.join(match))
	print ('Copied to clipboard')
	print ('\n'.join(match))
else:
	print ('Nothing found')