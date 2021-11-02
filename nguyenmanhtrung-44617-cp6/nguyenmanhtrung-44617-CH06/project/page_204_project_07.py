"""
Author: nguyen manh trung
Date: 24/10/2021
Problem:
    Lee has discovered what he thinks is a clever recursive strategy for printing the
    elements in a sequence (string, tuple, or list). He reasons that he can get at the
    first element in a sequence using the 0 index, and he can obtain a sequence of
    the rest of the elements by slicing from index 1. This strategy is realized in a
    function that expects just the sequence as an argument. If the sequence is not
    empty, the first element in the sequence is printed and then a recursive call is
    executed. On each recursive call, the sequence argument is sliced using the
    range 1:. Here is Lee’s function definition:
Solution:

    ....
"""
import os
import os.path


def displayFiles(path):
 """visits all of the files and directories in path and displays the files' contents."""
 if os.path.isfile(path):
     print("File name:"+path)
     f = open(path,'r')
     print(f.read())
 else:
     print("Directory name:"+path)
     lyst = os.listdir(path)
     for element in lyst:
         recursive_element = os.path.join(path,element)
         print("element:",element)
         print("recursive_element",recursive_element)
         displayFiles(recursive_element)
if __name__ == '__main__':
    print(f"Directory:{os.getcwd()}")
    displayFiles(os.getcwd())
