# Google Books API ⟶ BibTeX

Simple Python script for querying Google Books API for searching books, then printing its info formatted as BibTeX.

Example usage:

```shell
        [1] Title =
        [2] Author =
        [3] ISBN =
        [4] Query

>> Input: 1
>> Title = science of programming

        [1] Title = science of programming
        [2] Author =
        [3] ISBN =
        [4] Query

>> Input: 4
Searching Google Books with this info:
Title = science of programming
Author =
ISBN =

100%|██████████████████████████| 10/10 

[1] David Gries - The Science of Programming
[2] David Gries - The Science of Programming Answer Book
[3]  - SCIENCE OF PROGRAMMING
[4] Mark Priestley - A Science of Operations
[5] Walter J. Savitch - Pascal, an Introduction to the Art and Science of Programming
[6] Walter J. Savitch, Charles G. Petersen - Ada
[7] Walter J. Savitch - Turbo Pascal
[8] Walter J. Savitch - An Introduction to the Art and Science of Programming
[9] P. A. Collier, University of Tasmania. Department of Information Science, C. A. Lakos - A Rigorous Logic Basis for the Science of Programming
[10] Walter J. Savitch - Turbo Pascal 4.0/5.0
[X] Quit
Which book do I format?
>> Input: 1

@book{testname,
author={David Gries},
title={The Science of Programming},
publisher={Springer Science & Business Media},
year={2012},
url={https://play.google.com/store/books/details?id=QFrlBwAAQBAJ}
}
```
