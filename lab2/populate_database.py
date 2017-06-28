import pymysql
from rollback_Movie import *
from rollback_genre import *
from rollback_Dvd import *
from rollback_director import *
from rollback_studio import *
from rollback_Genre_Junction_Table import *
from rollback_Director_Junction_Table import *
from rollback_Studio_Junction_Table import *

from import_Movie import *
from import_genre import *
from import_Dvd import *
from import_director import *
from import_studio import *
from import_Genre_Junction_Table import *
from import_Director_Junction_Table import *
from import_Studio_Junction_Table import *

# rollback Genre_Junction_Table

is_success = rollback_Genre_Junction_Table()

if is_success is True:
    print "rollback_Genre_Junction_Table : successful"
else:
    print "rollback_Genre_Junction_Table : failed"
    

# rollback Director_Junction_Table

is_success = rollback_Director_Junction_Table()

if is_success is True:
    print "rollback_Director_Junction_Table : successful"
else:
    print "rollback_Director_Junction_Table : failed"

# rollback Studio_Junction_Table()

is_success = rollback_Studio_Junction_Table()

if is_success is True:
    print "rollback_Studio_Junction_Table : successful"
else:
    print "rollback_Studio_Junction_Table : failed"

# rollback Movie table

is_success = rollback_Movie()
if is_success is True:
    print "rollback_Movie : successful"
else:
    print "rollback_Movie : failed"

# rollback Genre table

is_success = rollback_genre()
if is_success is True:
    print "rollback_Genre : successful"
else:
    print "rollback_Genre : failed"

 #rollback Dvd table

is_success = rollback_Dvd()

if is_success is True:
    print "rollback_Dvd : successful"
else:
    print "rollback_Dvd : failed"

# rollback Director table

is_success = rollback_director()
if is_success is True:
    print "rollback_director : successful"
else:
    print "rollback_director : failed"

# rollback Studio table

is_success = rollback_studio()
if is_success is True:
    print "rollback_studio : successful"
else:
    print "rollback_studio : failed"


# populate Movie table

is_success = import_Movie()
if is_success is True:
    print "import_Movie : successful"
else:
    print "import_Movie : failed"

# populate Genre table

is_success = import_genre()
if is_success is True:
    print "import_Genre : successful"
else:
    print "import_Genre : failed"

 #populate Dvd table

is_success = import_Dvd()

if is_success is True:
    print "import_Dvd : successful"
else:
    print "import_Dvd : failed"

#populate Director table

is_success = import_Director()
if is_success is True:
    print "import_Director : successful"
else:
    print "import_Director : failed"

# populate Studio table

is_success = import_Studio()
if is_success is True:
    print "import_Studio : successful"
else:
    print "import_Studio : failed"

###############

#populate Genre_Junction_Table

is_success = import_Genre_Junction_Table()

if is_success is True:
    print "import_Genre_Junction_Table : successful"
else:
    print "import_Genre_Junction_Table : failed"


# populate Director_Junction_Table

is_success = import_Director_Junction_Table()

if is_success is True:
    print "import_Director_Junction_Table : successful"
else:
    print "import_Director_Junction_Table : failed"


# populate Studio_Junction_Table()

is_success = import_Studio_Junction_Table()

if is_success is True:
    print "import_Studio_Junction_Table : successful"
else:
    print "import_Studio_Junction_Table : failed"
