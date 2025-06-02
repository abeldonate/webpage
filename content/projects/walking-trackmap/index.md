+++
title = "Walking trackmap"
date = 2025-05-16

[taxonomies]
categories = ["software"]
tags = ["programming"]
+++

# How it started

I, with my dear friend [Pau](https://ploliver.github.io), used to meet once in a while in [Elda and Petrer](https://www.google.es/maps/@38.4787493,-0.7896861,15.24z?entry=ttu&g_ep=EgoyMDI1MDUxNS4wIKXMDSoASAFQAw%3D%3D), our native cities respectively. If my memory serves me right (which happens quite often), one day we had the following conversation:
- **Abel**: Have you noticed that we always make the same route?
- **Pau**: Yeah, we always meet at the same place, head in the same direction and unconsciously go through the same streets.
- **Abel**: Maybe we should try changing the route. Have you ever walked through *all* the streets?
- **Pau**: Do you mean *all* of them? Like every single one google maps marks as a street?
- **Abel**: Yep, I mean exhaustively *all* of them.
- **Pau**: I don't think so...
- **Abel**: Maybe we can try to do it.

(Normal people would have stopped here, and would have tried to have more variety on their walks. But, turns out to be, we don't exactly fit that profile.)

- **Pau**: If we do it we have to do it properly.
- **Abel**: I'm thinking about tracking our routes on Strava, for instance. That way, we'd have a record.
- **Pau**: Yep, and then we could write a python script that merges the tracks.

And what started as a joke is still going on...

# How it's going

<iframe src="resultingmap.html" width="100%" height="500" style="border:1px solid #ccc;">
    Your browser does not support iframes.
</iframe>


# Implementation

The implementation can be explored in github [abeldonate/walking-trackmap](https://github.com/abeldonate/walking-trackmap.git).

The code is written in python, and we make use of the following libraries:
- folium: management of maps
- gpxpy: management of track files (in .gpx format) 
- yaml: just for having the config parameters on a different file

The heavylifting is just a for loop that reads the .gpx tracks within the folder `tracks` and adds it to the map previously created by folium. Finally, the map is stored in the file `resultingmap.html`.