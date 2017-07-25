# RPSProject
A project to create a multiplayer online rock paper scissors game with more intricate rules

## Rules
* Win rock, get 3 points
* Win scissors, get 2 points
* Win paper, get 1 point
* Win with same item multiple times, get +1 point for each consecutive win
 * Ex: win with paper twice, have 3 pts (1+2), win with paper thrice, have 6 pts (1+2+3)
* First to 10 pts wins

## Resources
* Django channels for aasynchonous web sockets (https://github.com/django/channels)
* This amazing tutorial: https://codyparker.com/django-channels-with-react/

## Requirements
* Django >= 1.9
* [Django Channels](https://github.com/django/channels)
* [Django Rest Framework](http://www.django-rest-framework.org/)
* [Django Webpack Loader](https://github.com/owais/django-webpack-loader)
* Node & Node Package Manager
