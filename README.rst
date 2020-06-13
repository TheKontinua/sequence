The Hillegass Sequence
======================

In the future, a significant piece of the workforce will need to be
able to solve problems using the ideas of math, physics, and computer
science. These ideas are deep and difficult to master. It is my
opinion that the topics would be most efficiently taught as an
integrated toolbox. This will be a collection of educational materials
to support that approach.

These materials assume that the student can type with reasonable speed
and can solve problems using algebra. At the end the student will have
a working knowledge of:

* Math through linear algebra and vector calculus
* Python programming
* Physics that an engineer would know at the end of the first year of university
* Probability and statistics
* Basic data science and machine learning techniques

There will be 36 workbooks for this sequence. The workbooks are to be
printed out and given to the student. The student is expected to write
in the books with a pencil: there is no substitute for pencil and
paper when you are learning to solve deep problems.

There will be a collection of lecture videos to accompany the
workbooks. The videos will be freely available on the internet.

I hope that each student has a mentor who will answer their questions
and evaluate their progress. It is my hope that the comprehensive
nature of the materials I am supplying will make the job of this mentor
pretty easy.

To this end, there will be a system that generates a test and its
answer key for each workbook. Mentors will need to join the mentor
network to access this system.

Learning these ideas is a journey, and everyone will travel at
different speeds. Not everyone will make it to through to the
end. This sequence is designed to accommodate that reality. That said,
we have tried to design the workbooks so that each one will take about
40 hours of work for the average student to consume.

Where I live, schools are open about 180 days per year. Thus, if
students work for two hours per day, they will consume 9 workbooks per
year.  Working for four years, the average student should be able to complete all 36
workbooks.

The first version of the workbooks, videos, and tests will be in
American English, as that is the language that I speak. I hope that in
time I will have translations into every major language on the planet.

Teaching to the Tests
-----------------------

In order to prove the validity of this approach, we will make a point
of preparing the student to pass several nationally and
internationally normed tests. In particular, if you have
worked through all the workbooks, you should be able to pass the
following tests:

* AP Calculus BC
* AP Physics C: Mechanics
* AP Physics C: Electricity and Magnetism
* AP Statistics
* The TensorFlow Developer Certificate

Politically, it is hoped that this will also make the sequence easier to
adopt in schools.

Programming Language and Software
---------------------------------

This sequence uses Python, and there are compromises there.  If we were
teaching to the current AP Computer Science A test, we would use
Java. However, given the exploratory nature of the programming the
student will be doing, Python and its extensive libraries are the
obvious choice.

Julia, which is a more elegant and efficient language, would also be a
natural choice, but at this time Python is a more desireable skill in
industry. We will use Python.

The student will use only open source software during this
sequence. This lowers the cost of software to zero, and empowers the
student by inviting them to explore the foundational code they rely
upon.

Markup
------

As Python is the language of choice, and Python documentation uses
reStructuredText for markup, documents designed to be read on the web,
such as this one, will be created in
`ReStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_,
not Markdown.

The workbooks themselves will be written in
`LaTeX <https://www.latex-project.org>`_. The workbooks are designed to printed onto paper. In commiting to
LaTeX instead of something like reStructuredText, we giving up nice
web rendering in return for a lot of control over page layout. I am
comfortable with this compromise.

Installation
------------

You will need to install LaTeX.

In ``Build/build.cfg`` you can specify where ``pdftex`` is installed
on your system.  You can also specify your default paper size (``A4``
or ``Letter``)..

In the ``Build`` directory, there is are three python scripts called
``build_book.py``, ``build_link_list.py`` and ``clean.py``.

To build a PDF of Workbook 5 for your default paper size::

  python build_book.py 5

Intermediate files will be created in directory
``Build/Intermediate``. You can ignore them.  The final pdf will
appear in as ``Build/Workbook_05.pdf``

To build all the books::

  python build_book.py all

To build an html page that has all the links (including all the video links) for Workbook 5::

  python build_link_list 5

A file called ``Build/link_list_05.html`` will appear.

To delete all the intermediate files, pdfs, and html files in ``Build``::

  python clean.py
