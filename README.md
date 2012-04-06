django-impositions
==================

Initialize Black Triangle
-------------------------

1. make virtualenv and pip install the requirements
1. syncdb and migrate
1. runserver, go to admin, add something for each model
1. note the pk of the composition you want to test
1. ./manage.py shell
1. output composition:

        > from impositions import utils
        > utils.output_composition(<pk>)

*[Black Triangle Wha??](http://rampantgames.com/blog/2004/10/black-triangle.html)*



