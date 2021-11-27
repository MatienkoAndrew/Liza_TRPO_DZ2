import psycopg2
from contextlib import closing

class PulseGateway:
    def __init__(self):
        self.entered_pulse = None
        self.processed_pulse = None
        pass

    def Insert(self):
        conn_string = "host='localhost' dbname='liza' user='a19053183' password=''"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO Pulse (entered_pulse, processed_pulse) 
                            VALUES ({self.entered_pulse}, {self.processed_pulse})
                            """)
        return

