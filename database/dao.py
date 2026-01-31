from database.DB_connect import DBConnect
from model.state import Stato

class DAO:
    @staticmethod
    def get_anno():
        conn = DBConnect.get_connection()

        if conn is None:
            print('Errore di connessione al database!!')
            return None

        result = []

        cursor = conn.cursor()
        query = """ SELECT DISTINCT(YEAR(s_datetime))
                    FROM sighting
                    ORDER BY YEAR(s_datetime) DESC"""
        try:
            cursor.execute(query)

            for row in cursor:
                result.append(row[0])

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_shape(anno):
        conn = DBConnect.get_connection()

        if conn is None:
            print('Errore di connessione al database!!')
            return None

        result = []

        cursor = conn.cursor()
        query = """ SELECT shape
                    FROM sighting
                    WHERE YEAR(s_datetime) = %s
                    GROUP BY shape ASC"""
        try:
            cursor.execute(query, (anno,))

            for row in cursor:
                result.append(row[0])

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_nodes_stati():
        conn = DBConnect.get_connection()

        if conn is None:
            print('Errore di connessione al database!!')
            return None

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT id, name
                    FROM state"""
        try:
            cursor.execute(query)

            for row in cursor:
                result.append(Stato(**row))

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_edges(anno, forma):
        conn = DBConnect.get_connection()

        if conn is None:
            print('Errore di connessione al database!!')
            return None

        result = []

        cursor = conn.cursor()
        query = """ SELECT n.state1, n.state2, COUNT(s.id) as peso
                    FROM sighting s, neighbor n
                    WHERE (n.state1 = s.state OR n.state2 = s.state)
                            AND YEAR(s.s_datetime) = %s
                            AND s.shape = %s
                    GROUP BY n.state1, n.state2"""

        try:
            cursor.execute(query, (anno, forma))

            for row in cursor:
                result.append(row)

        except Exception as e:
            print(e)

        cursor.close()
        conn.close()
        return result