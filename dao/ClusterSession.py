from flask import jsonify
from cassandra.cluster import Cluster
import os
from datetime import datetime


def getSession():
    """ Try to establish Cassandra connection and return simple query results """
    cluster = Cluster()
    try:
        session = cluster.connect()
        session.execute('use wallet;')
        return session
    except Exception as error:
        message = "%s: %s" % (error.__class__.__name__, str(error))
        return jsonify(message=message, hostname=os.uname()[1],
                       current_time=str(datetime.now())), 500
