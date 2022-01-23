# PKB
A low-tech command line tool for adding and querying a PKB - Personal Knowledge Base (uses key value pairs)

Install python dependencies for this project and install mongo (https://docs.mongodb.com/manual/installation/) 

## 1.
Run a local mongo server: $:`mongod --dbpath="./db/"`

## 2.
Now you can add to your PKB with:
$:`pkb --insert a` 

## 3.
And query it with
$:`pkb --query "WHATYOUWANTTOSEARCHHERE"`
