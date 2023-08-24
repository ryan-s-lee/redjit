# Redjit - Reddit clone in Django

After several weeks of learning python and Django, I figured it would be better 
if I actually did something with that knowledge. Reddit is pretty popular, and
has a fairly clear-cut features, so it serves as a good project to work on.

I aim to emulate Reddit fairly closely (but not exactly), without following any 
tutorials (a quick search suggests there aren't any anyway). I also don't intend
to host this publicly.

## All Pages
- Should display a list of posts on them

## User Pages
- Should display user's name, birthday, a paginated list of communities they're
in, and a paginated list of posts that they've made (if infinite scrolling is 
possible using pagination, do that instead).

## Thread Pages
- Should display main post title at the top.
- A subtitle should display the main post user and post date
- A Comments header should delineate the start of the comments section
- Comments should include commenting user's name, post date, and content.
- Comments should have a line to their left indicating which comment they are 
  responding to
- Below each comment should be the option to reply to it

## Community Pages
- Should contain Community name
- Should contain all posts related to the community
    - in order of post date
    - paginated or infinite scrolling
    - post titles should be clickable, allowing users to enter a thread page for
      that post

## Feed Pages
- Should contain all posts ever made
    - in order of post date
    - paginated or infinite scrolling
    - post titles should be clickable, allowing users to enter a thread page for
      that post