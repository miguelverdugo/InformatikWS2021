# Informatics_Exercise_WS2020
Exercises for the Astronomy-Informatics lecture in the winter semester of 2020

*Copied from WS2019*

**Please raise an issue to discuss particular stuff. 
You can of course also suggest changes directly using a pull request.** 

Please check the [course structure](Structure.md)

Ideas for questions are in [here](ideas.md)

----
Because of convenience I started to write the exercises in Markdown and 
I will put them in a private github repository. 

Slides (e.g. [Exercise_00](Exercise_00) are also done with Markdown and
rendered using [remark](https://github.com/gnab/remark). Converting to PDF
can be done using Chrome/Chromium. It doesn't work with Firefox. 

[Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

There are more than few ways to convert .md files to pdf. I will detail 
them here




## Using pandoc

    sudo apt-get install pandoc 
    sudo apt install texlive-xetex
    sudo apt install librsvg2-bin
    sudo apt install texlive-math-extra
    sudo apt-get install lmodern

    # etc
    # finally

    pandoc input.md -f gfm -o output.pdf
    
More details [here](https://learnbyexample.github.io/tutorial/ebook-generation/customizing-pandoc/)

A [script](run_pandoc.sh) is available for a better rendering 

    sh run_pandoc.sh input.md output.md

## Using `remark.js`

It is possible to set the an html file that can takes a markdown file and
use chromium to produce pdf or print the file. A example of such page 
is in the [Exercise_02](Exercise_02) directory. **It needs more work**

  * Among other things, it needs to setup a webserver. One can setup
    such a thing by using `python -m http.server` on the directory. 
    Useful for testing stuff! :-)
    
## Online

There are also online services that render markdown into pdf acceptably 
well e.g. [https://www.markdowntopdf.com/]
 
