import mysql.connector
from final_project.entity.client import Client


class ClientDb:
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='root123',
                                                  database='final_project')
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, client):
        self.connect()
        self.cursor.execute(
            "insert into client (name, family, birth_date, gender, nationality, national_id,"
            " start_date, end_date) values "
            "(%s, %s, %s,%s, %s, %s, %s, %s)",
            [client.name, client.family, client.birth_date, client.gender, client.nationality,
             client.national_id, client.start_date, client.end_date])
        self.disconnect(commit=True)

    def edit(self, client, id):
        self.connect()
        self.cursor.execute(
            "update client set name=%s,family=%s,birth_date=%s,gender=%s,nationality=%s, national_id=%s where id=%s",
            [client.name, client.family, client.birth_date, client.gender, client.nationality, client.national_id, id])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from client where id=%s", [id])
        self.disconnect(commit=True)

    def fina_all(self):
        self.connect()
        self.cursor.execute("select * from client")
        client_list = self.cursor.fetchall()
        self.disconnect()
        return client_list

    def fina_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from client where id=%s", [id])
        client_list = self.cursor.fetchall()
        self.disconnect()
        return client_list

    def find_by_family(self, family):
        self.connect()
        self.cursor.execute("select * from client where family like %s", [family + "%"])
        client_list = self.cursor.fetchall()
        self.disconnect()
        return client_list

    def find_id(self):
        self.connect()
        self.cursor.execute("select id from client")
        ids = [row[0] for row in self.cursor.fetchall()]
        self.disconnect()
        return ids
