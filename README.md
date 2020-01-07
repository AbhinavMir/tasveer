Notice: This project is still under maintainence, I would love your support as I have to dedicate time to a few other projects as of now. The final project will be beautifully integrated into the Python ecosystem with perfect OOPs, Clean Code and the Zen of Python .☺

# tasveer
A Python Package to help you quickly download a few images for testing/validation purposes.

**Welcome to Tasveer**

Tasveer is a module to help you download tons of images!

**Usage**

```
pip install tasveer
```
```python
import tasveer as tsv

# Simple usage. Prompts the user for a query and number of images:
tsv.download()

# Using query and count parameters:
tsv.download(query="<SEARCH_STRING>", count="<NUM_IMAGES_AS_INT>")

# Example using parameters: downloads 4 images of books:
tsv.download(query="books", count="4")
```
>**Note:** If you only include one parameter, it will fall back to prompting for the missing parameter. 


**Future Work**

Feel free to pull. Here's what I plan to work on-

1. Include a lightweight cleaning and processing function

2. Change from prompt to argument

Kindly refer to <a href="https://github.com/AbhinavMir/tasveer/issues"><i>issues</i></a> to see list of requested enhancements and easy tasks you could help the community with plus have your own OSS contribution!

If there is any problem you have, want quick answers or want to dicuss with core developers, kindly use the slack channel at <br> https://tasveer-group.slack.com/

If you're new to the Open Source community,programming or Python, please message me for any doubts! ^_^

Sincerely,
Abhinav
   
