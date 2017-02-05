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

now = time.strftime("%c")

#########################################################

# add
def insert(inserted):
	while(True):
		title = input("Title: ")
		content = input("Content: ")
		collection.insert_one({"name": title, "contents": content, "date": now, "type": "word"})
		click.clear()

# query
def query(query):
    click.echo("Search: ")
    data = collection.find( { "$text": { "$search": query } } )
    for x in data:
        click.echo(x)

#########################################################

@click.command()

@click.option('--insert', nargs=1, help="Add")
@click.option('--query', nargs=1, help="Search")

def cli(insert, query):

    if insert:
    	print(insert)
    	insert()

    if query:
	query(query)

#########################################################

# future additions: all file imports, support more types
