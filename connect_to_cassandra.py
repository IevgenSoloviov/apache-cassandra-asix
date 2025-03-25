from cassandra.cluster import Cluster

# Connexió a Cassandra
cluster = Cluster(contact_points=['<server_IP>'], port=9042)
session = cluster.connect()

# Seleccionar el keyspace correcte
session.set_keyspace('<keyspace_name>')

# Insertar dades
session.execute("""
SELECT * FROM <table>
""")

# Tancar la connexió
cluster.shutdown()
