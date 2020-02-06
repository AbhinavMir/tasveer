Please read more at <a href="https://tasveer.readthedocs.io">tasveer.readthedocs.io</a><br><hr>
Notice: This project is still under maintainence, I would love your support as I have to dedicate time to a few other projects as of now. The final project will be beautifully integrated into the Python ecosystem with perfect OOPs, Clean Code and the Zen of Python .☺
<br>
A Request for Pull Request: Please Run your Python code through a PEP8 formatter, but feel free to not do it incase you feel it decreases readability. Also, try to optimize performance whenever you can and include the *Zen of Python* in your code (or life!).
<br><hr>
# Tasveer
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

<h1>List of Functionalities for Tasveer 2.0</h1>

**Conversion between Image Formats**:

1. Interconversion between Raster Image Types

2. Vector types rendered to Raster Type

3. DICOM to Raster Types

4. Raster to HDF5 type Conversions

**Preprocessing Abilities**:

1. Blurring / Noise Removal
2. Sharpening
3. Contrast Adjustment
4. Saturation Adjustment
5. Brightness Adjustment

**Using ImageNets API for labelled download**

**Implement Multiprocessing**

- This will help us download and process at the same time. To be declared as a method of tasveer, with positional arguments of array of tasks to be performed.
<br><hr>

Kindly refer to <a href="https://github.com/AbhinavMir/tasveer/issues"><i>issues</i></a> to see list of other requested enhancements and easy tasks you could help the community with plus have your own OSS contribution!

If there is any problem you have, want quick answers or want to dicuss with core developers, kindly use the slack channel at <br> https://tasveer-group.slack.com/

If you're new to the Open Source community,programming or Python, please message me for any doubts! ^_^

Sincerely,
Abhinav
<br><hr>
**Contribution**<br>
<a href="https://github.com/steveyackey">Steve</a> for adding paramentric download function<br>
<a href="https://github.com/Mansi145">Mansi</a> for adding a function to download images and adjust width and height
<br>
<a href="https://github.com/ambika1101">Ambika</a> for readthedocs.io documentation<br><hr>
Next Release on February 7th 2020.
   
