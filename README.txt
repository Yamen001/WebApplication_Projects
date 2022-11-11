to link html with css in html files write the following:
--------------------------------------------------------


I) on top of the html file write:
{% load static %}

II) to actually link the css styling:

<link rel="stylesheet" href = {% static 'css/main.css' %}

And your done!

----------------

Note: linking js files and images is the same as well

example for images:

<img src = {% static 'img/images.jpg' %}

Note: you must include {% load static %} here as well
