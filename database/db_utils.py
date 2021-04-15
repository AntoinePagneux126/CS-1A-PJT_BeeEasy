import sqlite3
import datetime


def add_beekeeper(name: str, cursor):
    """ Add a beekeeper into the database.
    Parameters
    ----------
    name : str
        The name of the beekeeper.
    cursor : 
        The object used to query the database.
    Returns
    -------
    bool
        True if no error occurs, False otherwise.

    """

    try:

        query = "SELECT  * FROM Beekeepers"
        cursor.execute(query)
        data = cursor.fetchall()

        if len(data) == 0:
            id = 1

        else:
            id = 1
            for d in data:
                # compute the id of bekeeper
                if d[0] > id:
                    id = d[0]
                # check if the name is not already used
                if d[1] == name:
                    print("Name already used, please use another beekeeper's name")
                    return False
            id += 1

        insert_query = "INSERT INTO Beekeepers (id_beekeeper, name) VALUES (?, ?)"
        query_values = (id, name)
        cursor.execute(
            insert_query,
            query_values
        )

    except sqlite3.IntegrityError as error:
        print("An integrity error occurred while inserting the beekeeper: {}".format(error))
        return False
    except sqlite3.Error as error:
        print("A database error occurred while inserting the beekeeper: {}".format(error))
        return False

    return True


def add_hive(hive_name: str, beekeeper_name: str, cursor):
    """ Add a hive into the database.
    Parameters
    ----------
    hive_name : str
        The name of the hive.
    beekeeper_name : str
        The beekeeper's name of the hive.
    cursor : 
        The object used to query the database.
    Returns
    -------
    bool
        True if no error occurs, False otherwise.

    """

    try:

        query = "SELECT  * FROM Beekeepers"
        cursor.execute(query)
        data = cursor.fetchall()

        # Find the beekeeper's id related to the beekeeper's name.
        id_beekeeper = 0
        for d in data:
            if d[1] == beekeeper_name:
                id_beekeeper = d[0]

        if id_beekeeper == 0:
            print("Invalid name, the beekeeper's name is not into the database")
            return False

        # Compute the id of the hive
        query = "SELECT  * FROM Beehives"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) == 0:
            id = 1
        else:
            id = 1
            for d in data:
                if d[0] > id:
                    id = d[0]
                # check if the name is not already used
                if d[1] == hive_name:
                    print("Name already used, please use another beehive's name")
                    return False
            id += 1

        insert_query = "INSERT INTO Beehives (id_hive, name, id_beekeeper) VALUES (?, ?, ?)"
        query_values = (id, hive_name, id_beekeeper)
        cursor.execute(
            insert_query,
            query_values
        )

    except sqlite3.IntegrityError as error:
        print("An integrity error occurred while inserting the hive: {}".format(error))
        return False
    except sqlite3.Error as error:
        print("A database error occurred while inserting the hive: {}".format(error))
        return False

    return True


def add_sensor(measure: str, unity: str, hive_name: str, cursor):
    """ Add a sensor into the database related to a hive.
    Parameters
    ----------
    measure : str
        The measure provided by the sensor.
    unity : str;
        The unit of the measure
    hive_name : str
        The name of the hive which embed the sensor.
    cursor : 
        The object used to query the database.
    Returns
    -------
    bool
        True if no error occurs, False otherwise.

    """

    try:

        query = "SELECT  * FROM Beehives"
        cursor.execute(query)
        data = cursor.fetchall()

        # Find the beekeeper's id related to the beekeeper's name.
        id_beehive = 0
        for d in data:
            if d[1] == hive_name:
                id_beehive = d[0]

        if id_beehive == 0:
            print("Invalid name, the beehive's name is not into the database")
            return False

        # Compute the id of the sensor
        query = "SELECT  * FROM Sensors "
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) == 0:
            id = 1
        else:
            id = 1
            for d in data:
                if d[0] > id:
                    id = d[0]
                # check if the name is not already used
                if (d[1] == measure) and (id_beehive == d[3]):
                    print("Measure already used")
                    return False
            id += 1

        insert_query = "INSERT INTO Sensors (id_sensor, measure, unity, id_hive) VALUES (?, ?, ?,?)"
        query_values = (id, measure, unity, id_beehive)
        cursor.execute(
            insert_query,
            query_values
        )

    except sqlite3.IntegrityError as error:
        print("An integrity error occurred while inserting the sensor: {}".format(error))
        return False
    except sqlite3.Error as error:
        print("A database error occurred while inserting the sensor: {}".format(error))
        return False

    return True


def add_measure(hive_name: str, measure: str, date: str, value: float, cursor):
    """ Add a sensor into the database related to a hive.
    Parameters
    ----------
    hive_name : str
        The name of the hive.
    measure : str
        The measure.
    date : str
        The date of the measure.
    value : float;
        The value measured by the sensor.
    cursor : 
        The object used to query the database.
    Returns
    -------
    bool
        True if no error occurs, False otherwise.

    """

    try:

        # Search the sensor's id related to the hive and the measure
        query = """SELECT id_sensor FROM Sensors 
                    JOIN Beehives ON Beehives.id_hive = Sensors.id_hive
                    WHERE Beehives.name = ? and Sensors.measure = ? """

        cursor.execute(query, (hive_name, measure))
        data = cursor.fetchall()

        if len(data) < 1:
            print("Error, the sensor related to the beehive does not exist")
            return False

        id_sensor = data[0][0]

        query = "SELECT  * FROM Sensors"
        cursor.execute(query)
        data = cursor.fetchall()

        list_sensor = []
        if len(data) > 0:
            for d in data:
                list_sensor.append(d[0])
        # Check if the sensor exists
        if id_sensor not in list_sensor:
            print("Invalid sensor, it does not exist")
            return False

        # Compute the id of the measure
        query = "SELECT  * FROM Measures "
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) == 0:
            id = 1
        else:
            id = 1
            for d in data:
                if d[0] > id:
                    id = d[0]
            id += 1

        insert_query = "INSERT INTO Measures (id_measure, date_measure, value, id_sensor) VALUES (?, ?, ?,?)"
        query_values = (id, date, value, id_sensor)
        cursor.execute(
            insert_query,
            query_values
        )

    except sqlite3.IntegrityError as error:
        print("An integrity error occurred while inserting the Measures: {}".format(error))
        return False
    except sqlite3.Error as error:
        print("A database error occurred while inserting the Measures: {}".format(error))
        return False

    return True


def get_hives_name(cursor):
    """ Get the names of all the hives.
    Parameters
    ----------
    cursor : 
        The object used to query the database.
    Returns
    -------
    List
        List of hives if no error occurs, an empty list otherwise.

    """
    try:
        query = "SELECT name FROM Beehives"
        cursor.execute(
            query
        )

        data = cursor.fetchall()

        list_hives = []

        for d in data:
            list_hives.append(d[0])

    except sqlite3.IntegrityError as error:
        print("An integrity error occurred : {}".format(error))
        return []
    except sqlite3.Error as error:
        print("A database error occurred : {}".format(error))
        return []
    return(list_hives)


def get_beekeepers_name(cursor):
    """ Get the names of all the hives.
    Parameters
    ----------
    cursor : 
        The object used to query the database.
    Returns
    -------
    List
        List of beekeepers if no error occurs, an empty list otherwise.

    """
    try:
        query = "SELECT name FROM Beekeepers"
        cursor.execute(
            query
        )

        data = cursor.fetchall()

        list_beekeepers = []

        for d in data:
            list_beekeepers.append(d[0])

    except sqlite3.IntegrityError as error:
        print("An integrity error occurred : {}".format(error))
        return []
    except sqlite3.Error as error:
        print("A database error occurred : {}".format(error))
        return []
    return(list_beekeepers)


def get_hives_of_beekeeper(beekeeper_name: str, cursor):
    """ Get the names of the hives of a beekeeper.
    Parameters
    ----------
    beekeeper_name : str
        The name of the beekeeper
    cursor : 
        The object used to query the database.
    Returns
    -------
    List
        List of hives of the beekeeper if no error occurs, an empty list otherwise.

    """
    try:
        query = """SELECT Beehives.name FROM Beehives JOIN Beekeepers ON Beehives.id_beekeeper = Beekeepers.id_beekeeper WHERE (Beekeepers.name = {})""".format(
            "'" + beekeeper_name + "'")
        cursor.execute(
            query
        )

        data = cursor.fetchall()

        list_hives = []

        for d in data:
            list_hives.append(d[0])

    except sqlite3.IntegrityError as error:
        print("An integrity error occurred : {}".format(error))
        return []
    except sqlite3.Error as error:
        print("A database error occurred : {}".format(error))
        return []
    return(list_hives)


def get_measure_and_unit(hive_name: str, cursor):
    """ Get the names of all the hives.
    Parameters
    ----------
    hive_name : str
        The name of the hive.
    cursor : 
        The object used to query the database.
    Returns
    -------
    Set
        Association {measure : unity} of all the sensors related to the hive.

    """
    try:
        query = """SELECT measure, unity FROM Sensors 
                    JOIN Beehives ON Beehives.id_hive = Sensors.id_hive
                    WHERE Beehives.name = {}
        """.format('''"''' + hive_name + '''"''')
        cursor.execute(
            query
        )

        data = cursor.fetchall()

        if len(data) == 0:
            "Error, the sensor does not exist"
            return {}

        measures_and_units = {}
        for d in data:
            measures_and_units[d[0]] = d[1]

    except sqlite3.IntegrityError as error:
        print("An integrity error occurred : {}".format(error))
        return {}
    except sqlite3.Error as error:
        print("A database error occurred : {}".format(error))
        return {}

    return(measures_and_units)


def get_measures(hive_name: str, measure: str, cursor):
    """ Get measures from a sensor.
    Parameters
    ----------
    hive_name : str
        The name of the hive.
    measure : str
        the measure that the user wants.
    cursor : 
        The object used to query the database.
    Returns
    -------
    List
        List of tuples (date, value) if no error occurs, an empty list otherwise.

    """

    try:
        query = """SELECT  Measures.date_measure, Measures.value  FROM Measures
                    INNER JOIN Sensors ON Sensors.id_sensor = Measures.id_sensor 
                    INNER JOIN Beehives ON Beehives.id_hive = Sensors.id_hive 
                    WHERE Beehives.name =  ? and  Sensors.measure = ? """
        cursor.execute(
            query,
            (hive_name, measure)
        )

        data = cursor.fetchall()

    except sqlite3.IntegrityError as error:
        print("An integrity error occurred : {}".format(error))
        return []
    except sqlite3.Error as error:
        print("A database error occurred : {}".format(error))
        return []
    return(data)


if __name__ == '__main__':

    # DEBUG PLAYGROUND

    # Connects to the database.
    conn = sqlite3.connect('database/debug_db.db')

    # Enables the foreign key contraints support in SQLite.
    conn.execute("PRAGMA foreign_keys = 1")

    # Get the cursor for the connection. This object is used to execute queries
    # in the database.
    cursor = conn.cursor()

    print(add_beekeeper("Antoine", cursor))
    print(add_beekeeper("Jeremy", cursor))
    print(add_hive("La Ruche d'Antoine", "Antoine", cursor))
    print(add_hive("Jeremyshive", "Jeremy", cursor))
    print(add_hive("Jeremyshive 2", "Jeremy", cursor))
    print(add_hive("Jeremyshive 3", "Jeremy", cursor))
    print(add_hive("MyHive2", "Daniel", cursor))
    print(add_sensor("Masse", "kg", "La Ruche d'Antoine", cursor))
    print(add_sensor("Pression", "Pa", "La Ruche d'Antoine", cursor))
    print(add_sensor("Temperature", "°C", "La Ruche d'Antoine", cursor))
    print(add_sensor("Humidite", "%", "La Ruche d'Antoine", cursor))
    print(add_sensor("Miel", "kg", "La Ruche d'Antoine", cursor))
    print(add_sensor("Masse", "kg", "Jeremyshive", cursor))
    print(add_sensor("Pression", "Pa", "Jeremyshive", cursor))

    for i in range(12):
        print(add_measure("La Ruche d'Antoine", "Pression", str(
            datetime.datetime.now()), 985 + i, cursor))
        print(add_measure("La Ruche d'Antoine", "Masse", str(
            datetime.datetime.now()), 15 + 2*i, cursor))
        print(add_measure("La Ruche d'Antoine", "Temperature", str(
            datetime.datetime.now()), 10 + i, cursor))
        print(add_measure("La Ruche d'Antoine", "Miel", str(
            datetime.datetime.now()), i*2, cursor))
        print(add_measure("La Ruche d'Antoine", "Humidite", str(
            datetime.datetime.now()), 50 + i, cursor))

        print(add_measure("Jeremyshive", "Pression",
                          str(datetime.datetime.now()), i, cursor))
        print(add_measure("Jeremyshive", "Masse", str(
            datetime.datetime.now()), i**2, cursor))

    print(get_hives_name(cursor))
    print(get_beekeepers_name(cursor))
    print(get_hives_of_beekeeper("Jeremy", cursor))
    print(get_measures('MyHive', 'Masse', cursor))
    print(get_measures("Jeremy's hive", "Masse", cursor))
    print(get_measure_and_unit("Jeremy's hive", cursor))
    conn.commit()

    cursor.close()
    conn.close()
