# PKB
A low-tech command line tool for adding and querying a PKB - Personal Knowledge Base (uses key value pairs)

https://medium.com/@nchackerian/wa-peek-into-personal-knowledge-management-systems-851a59413fcb#.go96348dl

Install python dependencies for this project and install mongo (https://docs.mongodb.com/manual/installation/) 

Run pkb to create the db folder for your KB

Run a local mongo server: $:`mongod --dbpath="./db/"`

Now you can add to your PKB with:
$:`pkb --insert a` (this does not insert 'a', it merely begins the process for adding key value pairs)

And query it with
$:`pkb --query "WHATYOUWANTTOSEARCHHERE"`
