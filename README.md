
### Introduction

This repository is an implementation of Exercise 7.1.4 of Christian Hill's
[Scientific
Python](https://scipython.com/book/chapter-7-matplotlib/problems/p71/atmospheric-carbon-dioxide-concentrations/).
In this exercise the student obtains a CSV file of the atmospheric carbon
dioxide concentrations since 1958 from the US National Oceanic and Atmospheric
Administration (NOAA) and plots it using [Matplotlib](https://matplotlib.org/).

I've extended what is basically an exercise in learning the Matplotlib API into
an exercise in Django. Rather than do the usual thing of simply reading the CSV
file in a simple python script I have created a simple model, loaded it into
Django and generated the plots with a couple of management commands.

Of course once the data is in a database, you can do all sorts of things with
it. You can create interactive front ends, you can run more interesting queries,
you can generate statistics (and store them too) without every having to load
the data from CSV again.

Django's Object Relational Mapper allows one to get the Data into a database for
querying very easily. In fact a REST interface (not done here) is not that far
away either using the Django REST Framework. In both cases one avoids the
(mostly) boilerplate code one usually writes when interacting with a relational
database.

And of course Django is based on python and most scientists and engineers are
already using python or on their way to learning it.

### Results

![Recent monthly mean CO_2 at Mauna Loa
Observatory](./backend/ccgg/static/ccgg/co2_mm_mlo_recent.png)

![Atmospheric CO_2 at Mauna Loa
Observatory](./backend/ccgg/static/ccgg/co2_mm_mlo_full_record.png)
