import __init__
from database.db_utils import *
from database.db import *
import plotly.express as px
import pandas as pd
import datetime

def get_dic_beekeepers_name():
    """ Get the names of all the hives.
    Parameters
    ----------
    Returns
    -------
    List
        List of dic {"label" : "", "value" : ""} .

    """
    # Connects to the database.
    conn = sqlite3.connect('database/debug_db.db')
    # Enables the foreign key contraints support in SQLite.
    conn.execute("PRAGMA foreign_keys = 1")
    # Get the cursor for the connection. This object is used to execute queries 
    # in the database.
    cursor = conn.cursor()

    list_beekeepers = get_beekeepers_name(cursor)
    list_dic = []
    
    for element in list_beekeepers:
        dic = {}
        dic['label'] = element
        dic['value'] = element
        list_dic.append(dic)

    conn.commit()
    cursor.close()
    conn.close()

    return(list_dic)
    
def get_dic_hive_of_beekeeper(beekeeper_name : str):
    """ Get the names of the hives of a beekeeper.
    Parameters
    ----------
    beekeeper_name : str
        The name of the beekeeper
    Returns
    -------
    List
        List of dic {"label" : "", "value" : ""} 
    """
    # Connects to the database.
    conn = sqlite3.connect('database/debug_db.db')
    # Enables the foreign key contraints support in SQLite.
    conn.execute("PRAGMA foreign_keys = 1")
    # Get the cursor for the connection. This object is used to execute queries 
    # in the database.
    cursor = conn.cursor()

    list_hives = get_hives_of_beekeeper(beekeeper_name, cursor)
    list_dic = []
    
    for element in list_hives:
        dic = {}
        dic['label'] = element
        dic['value'] = element
        list_dic.append(dic)

    conn.commit()
    cursor.close()
    conn.close()

    return(list_dic)

def get_dic_measures(hive_name : str):
    """ Get measures from a sensor.
    Parameters
    ----------
    hive_name : str
        The name of the hive.
    measure : str
        the measure that the user wants.
    Returns
    -------
    List
        List of dic {"label" : "", "value" : ""} .
    """

    # Connects to the database.
    conn = sqlite3.connect('database/debug_db.db')
    # Enables the foreign key contraints support in SQLite.
    conn.execute("PRAGMA foreign_keys = 1")
    # Get the cursor for the connection. This object is used to execute queries 
    # in the database.
    cursor = conn.cursor()

    dic_measures = get_measure_and_unit(hive_name, cursor)
    list_dic = []

    
    for key in dic_measures:
        dic = {}
        dic['label'] = key + " (" + dic_measures[key] + ")"
        dic['value'] = key
        list_dic.append(dic)

    conn.commit()
    cursor.close()
    conn.close()

    return(list_dic)

def get_data_range(hive_name : str, measure : str):
    """ Get the min and the max from the date range of a measure.
    Parameters
    ----------
    hive_name : str
        The name of the hive.
    measure : str
        the measure that the user wants.
    Returns
    -------
    dt_min, dt_max : datetime.date, datetime.date
        the min and the max from the date range of a measure.
    """

    # Connects to the database.
    conn = sqlite3.connect('database/debug_db.db')
    # Enables the foreign key contraints support in SQLite.
    conn.execute("PRAGMA foreign_keys = 1")
    # Get the cursor for the connection. This object is used to execute queries 
    # in the database.
    cursor = conn.cursor()

    data = get_measures(hive_name, measure, cursor)
    dic_measures_and_unit = get_measure_and_unit(hive_name, cursor)

    conn.commit()
    cursor.close()
    conn.close()

    # Check if data is empty
    if len(data) == 0:
        return None, None


    # Compute the unit of the measure
    unit = dic_measures_and_unit[measure]

    # Process data

    list_x = []
    for d in data:
        list_x.append(d[0])

    # Compute the min and the max in a string format
    date_min, date_max = min(list_x), max(list_x)

    dt_min = datetime.datetime.strptime(date_min, '%Y-%m-%d %H:%M:%S.%f')
    dt_max = datetime.datetime.strptime(date_max, '%Y-%m-%d %H:%M:%S.%f')

    dt_min = dt_min.date()
    dt_max = dt_max.date()
    
    return dt_min, dt_max

def get_fig_for_graph(hive_name : str, measure : str, dt_min = None, dt_max = None):
    """ Get measures from a sensor to tronsform them into a plotly figure in the interval [dt_min, dt_max].
    Parameters
    ----------
    hive_name : str
        The name of the hive.
    measure : str
        The measure that the user wants.
    dt_min : str
        The min date.
    dt_max : str
        The max date.

    Returns
    -------
    A plotly figure.
    """

    # Connects to the database.
    conn = sqlite3.connect('database/debug_db.db')
    # Enables the foreign key contraints support in SQLite.
    conn.execute("PRAGMA foreign_keys = 1")
    # Get the cursor for the connection. This object is used to execute queries 
    # in the database.
    cursor = conn.cursor()

    data = get_measures(hive_name, measure, cursor)
    dic_measures_and_unit = get_measure_and_unit(hive_name, cursor)

    conn.commit()
    cursor.close()
    conn.close()

    # Check if data is empty
    if len(data) == 0:
        return px.line(x = [0], y = [0])


    # Compute the unit of the measure
    unit = dic_measures_and_unit[measure]

    # Process data
    list_y = []
    list_x = []
    for d in data:
        dt = datetime.datetime.strptime(d[0], '%Y-%m-%d %H:%M:%S.%f')
        dt = dt.date()

        if (dt_min != None and dt_max != None):

            if dt >= datetime.datetime.strptime(dt_min, '%Y-%m-%d').date() and dt <= datetime.datetime.strptime(dt_max, '%Y-%m-%d').date():
                list_x.append(d[0])
                list_y.append(d[1])
        else:
            list_x.append(d[0])
            list_y.append(d[1])


    y_label = measure + " (" + unit + ")"    

    # Transform data into a dataframe
    dic = {"Dates" : list_x, y_label : list_y}
    df = pd.DataFrame(dic)

    # Computation of the graph
    fig = px.line(df, x= "Dates", y = y_label)
    
    return fig

def get_last_data(hive_name : str, measure : str):
    """ Get the last data from a sensor .
    Parameters
    ----------
    hive_name : str
        The name of the hive.
    measure : str
        The measure that the user wants.
    Returns
    -------
    The last data.
    """

    # Connects to the database.
    conn = sqlite3.connect('database/debug_db.db')
    # Enables the foreign key contraints support in SQLite.
    conn.execute("PRAGMA foreign_keys = 1")
    # Get the cursor for the connection. This object is used to execute queries 
    # in the database.
    cursor = conn.cursor()

    data = get_measures(hive_name, measure, cursor)

    conn.commit()
    cursor.close()
    conn.close()

    # Check if data is empty
    if len(data) == 0:
        return 0
    else:
        return data[-1][1]

