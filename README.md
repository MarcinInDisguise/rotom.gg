# rotom.gg [![Build Status](https://travis-ci.com/RirisuV/rotom.gg.svg?branch=master)](https://travis-ci.com/RirisuV/rotom.gg) [![codecov](https://codecov.io/gh/RirisuV/rotom.gg/branch/master/graph/badge.svg)](https://codecov.io/gh/RirisuV/rotom.gg) ![stability-wip](https://img.shields.io/badge/stability-work_in_progress-lightgrey.svg)
<img align="left" width="100" height="100" src="https://i.imgur.com/qxnOpVb.jpg">Use the rotom.gg to explore pokémon by type, weakness, ability, and more! Rotom.gg is a Discord bot  designed to support competitive players with metagame informations. Check out the list of commands below!


## Adding rotom.gg 
To add rotom.gg to your discord server just follow this link:
```
https://discord.com/api/oauth2/authorize?client_id=733002946752807084&permissions=84992&scope=bot
```

## Commands

| Command                                              | Description                                   | Example            |
| ----------------------------------------------------:|:---------------------------------------------:| ------------------:|
| !poke [_pokemon_ or _id_]                            | Detailed info about a Pokemon                 | !poke magikarp     |
| !ability [ability or _id_]                           | Detailed info about an ability                | !ability blaze     |
| !item [item or _id_]                                 | Detailed info about an item                   | !item leftovers    |
| !move [item or _id_]                                 | Detailed info about a move                    | !move thunderbolt  |
| !weak [_pokemon_ or _id_]                            | Detailed info about a Pokemon's weaknesses    | !weak magikarp     |
| !speed [_pokemon_  or _id_] [_level_ or _nothing_]   | Shows pokemon's speed stat in specified level | !speed magikarp    |


## Screenshots
<img src="https://i.imgur.com/DtacKME.png">

# Development 

## Requirements
* python>=3.6
* python3-pip

## CI/CD
* travis
* heroku

## Installation
#### For development
Start with cloning repository
```
git clone https://github.com/RirisuV/rotom.gg.git
```

I highly recommend to create virtual environment (but still, you can skip that)
On macOS and Linux:
```
python3 -m venv env
```
On Windows:
```
py -m venv env
```
Don't forget to activate it with command below
```
.\env\Scripts\activate
```
You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.

On macOS and Linux:
```
which python
.../env/bin/python
```
On Windows:
```
where python
.../env/bin/python.exe
```

Configuration is loaded from .env file located in root directory. Create it and paste your discord token of your bot.
```
DISCORD_TOKEN={your token goes here}
```

Install all dependencies
```
pip3 install -r requirements.txt
```

Once dependencies are installed, you can run application typing:
```
python3 bot.py
```
