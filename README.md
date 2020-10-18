# Squirrel Tracker

This project is to track all the known squirrels in Central Park. Users are allowed to report, update, and view squirrel data. 

## install requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.
```bash
$ pip install -r requirements.txt
```

## Usage
### to launch the project
```bash
$ python3 manage.py runserver
```

### import squirrel data
```bash
$ python3 manage.py import_squirrel_data /path/to/file.csv
```

### export squirrel data
```bash
$ python3 manage.py export_squirrel_data /path/to/file.csv
```

### Pages
`/sightings`: this is the homepage of the project. it lists all of the records with links, and users are able to report new spots, update records and view the map
`/map`: view the squirrels spot on the map
`/sightings/<unique-squirrel-id>`: individaul record
`/sightings/add`: report new observations
`/sightings/stats`: show some basic statistics of the data