import sqlite3

def create_datatable(conn, cursor):
    """ Create BeeEasy database
    Parameters
        ----------
        conn : 
            The object used to manage the database connection.
        cursor : 
            The object used to query the database.

        Returns
        ----------
        bool
            True if the database could be created, False otherwise.
        
        """

    cursor.execute("BEGIN")

    try:
        
        print("creating the table Beekeepers...")
        cursor.execute('''

            CREATE TABLE IF NOT EXISTS Beekeepers(
                id_beekeeper INTEGER PRIMARY KEY,
                name TEXT
            )
            '''
        )


        print("creating the table Beehives...")
        cursor.execute('''

            CREATE TABLE IF NOT EXISTS Beehives(
                id_hive INTEGER PRIMARY KEY,
                name TEXT,
                id_beekeeper REFERENCES Beekeepers(id_beekeeper)
            )
            '''
        )

        print("creating the table Sensors...")
        cursor.execute('''

            CREATE TABLE IF NOT EXISTS Sensors(
                id_sensor INTEGER PRIMARY KEY,
                measure TEXT,
                unity TEXT,
                id_hive REFERENCES Beehives(id_hive)
            )
            '''
        )

        print("creating the table Measures...")
        cursor.execute('''

            CREATE TABLE IF NOT EXISTS Measures(
                id_measure INTEGER PRIMARY KEY,
                date_measure DATETIME,
                value DOUBLE,
                id_sensor REFERENCES Sensors(id_sensor)
            )
            '''
        )





    # Exception raised when something goes wrong while creating the tables.
    except sqlite3.Error as error:
        print("An error occurred while creating the tables: {}".format(error))
        # We rollback the transaction! No table is created in the database.
        conn.rollback()
        # Return False to indicate that something went wrong.
        return False
    
    # If no error occurred.
    # We must COMMIT the transaction, so that all tables are actually created in the database.
    conn.commit()    
    print("Database created successfully")
    # Returns True to indicate that everything went well!
    return True


def create_data_base(name:str, folder:str = ""):

    db_file = ""
    if folder != "":
        db_file += folder + "/"
    
    db_file += name + ".db"

    # Open a connection to the database.
    conn = sqlite3.connect(db_file)

    # The cursor is used to execute queries to the database.
    cursor = conn.cursor()

    # Creates the database. THIS IS THE FUNCTION THAT YOU'LL NEED TO MODIFY
    create_datatable(conn, cursor)

    # Closes the connection to the database
    cursor.close()
    conn.close()  

if __name__ == '__main__':
    create_data_base("database/debug_db")