+++
title = "Chords and lyrics webapp"
date = 2024-07-15

[taxonomies]
categories = ["software"]
tags = ["music", "software"]
+++

# Motivation

I have always been pretty unhappy with the options that the internet offers me on chords and lyrics applications. For those who are not much in the music world, a "chords and lyrics" application is a database of a bunch of songs that contains the lyrics as well as the chords for playing it on an instrument (classically guitar/ukulele, but can be extended to any instrument). Don't get me wrong, there are great options on the internet, and I still use some of them. However, I haven't found a web/app that meets the following requirements (at least in a free version):

- I have all the songs I want (and in the case they aren't, they can be added)
- Transportation is allowed
- No registration needed
- Free of ads

For these reasons I decided to code my own webapp that does this. This post is the result of this little adventure.


# User's view

### Creation of songs

All the songs are stored in the folder songs-md. If you want to add/remove/change one song, a format should be followed, that consists on:
- A header containing
    - Name: \<the name of the song\> 
    - Artist: \<the artist of the song\>
    - Tune: \<an integer with the relative tune of the chords\>
- A line with "+++" that acts as a separator between the header and the content
- The lyrics with the chords above. Chords must be between <> keys.

An example of a correct format is shown below.

    Name: Stick Season
    Artist: Noah Kahan
    Tune: 0
    
    +++
           <A>
    As you promised me that I was more than all the miles combined
                  <E>
    You must have had yourself a change of heart like halfway through the drive
                     <F#m>
    'Cause your voice trailed off exactly as you passed my exit sign
    <D>
    Kept on driving straight and left our future to the right

Once you have some songs in the folder, it's time to navigate through the webapp.

### Navigation

If you are running this in localhost, the app should be running at http://127.0.0.1:5000/chords. Here a list with of songs and artists is shown. Clicking on an artist, the list with all the songs of that artist appears. Clicking on a song, the lyrics and chords of the song appear.

Inside every song page, three key pieces of information are displayed: the name, the artist and the tune of the song. Additionally, there is a little tab at the right part to display the rest of the information on the header. Above this tab two buttons are placed (-1 and +1). These are responsible for transporting the chords of the song. Finally, the third button is for returning to the original list of songs.


# Programmer's view

The webapp uses flask for the web building and bulma for the style management. All is managed via a python environment and a Makefile.

### Code

We start with the `html` documents in the folder `src/templates/`. These are html templates for each page.
- `index.html` handles the list of songs
- `artist.html` handles the list of artists
- `song.html` displays each song
- `about.html` displays the info of the page

There are two other python scripts on `src/`

`main.py` handles the routing of the pages, and all the things that are specific to flask. We distinguish four different routes:
- `/chords` the initial page, where the list of songs is displayed. It uses the template `index.html`
- `/chords/<artist>` the page of artist, where the list of songs of a given artist `<artist>` is shown.
- `/chords/<song>/<newtune>` the page each song. It displays the song `<song>` in the tune `<tune>`
- `/chords/about` to display the `about.html` page

`parser.py` contains all the required functions. For instance, a class `Song` is created, that contains all the information of a song. Some functions are, for example
- `get_songs_list()` gets the list of all the songs in the `songs-md` folder
- `transport_chord()` transports a given chord
- `md_to_html()` parses the md file into an html text with some custom features (mainly it replaces <> by \<strong\>\</strong\>)

### Configuration

There is also a configuration file `config.yaml` that stores the possible configurations of the application. Some of the variables are
- `MD_PATH` the path of the songs files
- `CHORD_OPEN/CLOSE` these four variables control the format of the keys. By default `<>` are used for the chords in the .md files, and this results in `<strong><\strong>` in the resulting html
- `SEPARATOR` the format of the separator of the header and the content in the .md files
- `KEYS` a list with the keys of a 12 edo scale


# Installation

For taking a look just visit [chords](https://abeldonate.com/chords/). I have stored here my songs. For making your own songs, follow the installation guide on the repo [abeldonate/chords](https://github.com/abeldonate/chords) to run the app in localhost.

