#!/usr/bin/env python

from pymongo import MongoClient
from subprocess import Popen

import click
import time
import gridfs
import os

# Create db if not existing
where = os.getcwd()
if not os.path.isdir(where+"/db/"):
	os.mkdir("db")

#########################################################

# DB 
client = MongoClient("localhost")

db = client.local;
collection = db.entries

collection.createIndex({name: "text", contents: "text"});

now = time.strftime("%c")
#########################################################

# add
def add():
	title = input("Title: ")
	content = input("Content: ")
	collection.insert_one({"name": title, "contents": content, "date": now, "type": "word"})
	click.clear()

# query
def search(query):
    click.echo("Search: ")
    data = collection.find( { "$text": { "$search": query } } )
    for x in data:
        click.echo(x)

#########################################################

@click.command()

@click.option('--insert', nargs=1, help='Add')
@click.option('--query', nargs=1, help='Search')

def cli(insert, query):

    if insert:
    	add()

    if query:
	    search(query)

#########################################################

# future additions: all file imports, support more types

if __name__ == '__main__':
    cli()
