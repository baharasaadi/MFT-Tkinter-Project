import mysql.connector
from final_project.entity.room import Room


class RoomDb:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='root123',
                                                  database='final_project')
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, room):
        self.connect()
        self.cursor.execute(
            "insert into room (bed, tv, refrigerator, room_service, kitchen, phone) values (%s, %s, %s,%s, %s, %s)",
            [room.bed, room.tv, room.refrigerator, room.room_service, room.kitchen, room.phone])
        self.disconnect(commit=True)

    def edit(self, room):
        self.connect()
        self.cursor.execute(
            "update room set bed=%s,tv=%s,refrigerator=%s,room_service=%s,kitchen=%s,phone=%s where id=%s",
            [room.bed, room.tv, room.refrigerator, room.room_service, room.kitchen, room.phone,
             room.id])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from room where id=%s", [id])
        self.disconnect(commit=True)

    def fina_all(self):
        self.connect()
        self.cursor.execute("select * from room")
        room_list = self.cursor.fetchall()
        self.disconnect()
        return room_list

    def fina_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from room where id=%s", [id])
        room_list = self.cursor.fetchall()
        self.disconnect()
        return room_list

    def find_id(self):
        self.connect()
        self.cursor.execute("select id from room")
        ids = [row[0] for row in self.cursor.fetchall()]
        self.disconnect()
        return ids
