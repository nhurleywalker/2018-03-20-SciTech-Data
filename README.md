# 2018-03-20-SciTech-Data
A talk I gave to a class of gifted and talented students at SciTech, via jupyter notebook and plot.ly

If you're reading this, you're probably one of the audience. If so, well done! It probably took a fair bit of effort to get this far.

This website probably seems pretty weird and complicated. Well, it kinda is. Even I don't know how everything works here. But here are some introductory notes.

You're on github, which is where researchers and code monkeys and random people from all over the place upload and share code. Right now you're looking at one of my "repositories", which is a fancy word for a directory full of stuff.

If you want to get this directory full of stuff and play with it, you'll need to "clone" the repository, for which you need a program called "git" running on your computer.

If you're using a Mac, go here: https://git-scm.com/download/mac

If you're using Windows, go here: https://gitforwindows.org/

If you're using Linux, open a terminal and type:

sudo apt install git

Then in either the Git for Windows terminal, or a Mac or Linux terminal, you can type

git clone https://github.com/nhurleywalker/2018-03-20-SciTech-Data.git

Right, hopefully that worked. Now you have a directory full of stuff! What do you do with it??

Well, I made the talk using a cool program called Jupyter. It is an interface to a programming language called Python, which is huge in astronomy and in the wider world of computing. The easiest way to get started using Jupyter is to go here:

http://jupyter.org/install

and follow the instructions for your operating system.

Now in your terminal, go into the new directory "2018-03-20-SciTech-Data" via

cd 2018-03-20-SciTech-Data

And you can type

jupyter notebook NHW_SciTech_Data.ipynb

If everything is installed properly, it should "magically" open a browser window, with the raw talk code, which you can modify as you see fit.

If you want to run a slideshow instead, type:

jupyter nbconvert --to slides --post serve --reveal-prefix=reveal.js NHW_SciTech_Data.ipynb

or if you're on Linux, the built-in script
./display_slides.sh
should work.

Some of the plots might need you to sign in to http://plot.ly. Sorry about that; it's a nice way of making them look fancy. You can find out about simpler plotting code by googling the "matplotlib" module which would have come with python in your Anaconda install.

Python is way more powerful than just this talk is showing. It's a real programming language and it's what most of my code is written in. To see some examples you could have a look at some of my other repositories. But to get started I recommend Googling for some "how to get started with python" information, and go from there.

Hope you enjoyed the talk!

Natasha Hurley-Walker

nhw@icrar.org

20/03/2018
