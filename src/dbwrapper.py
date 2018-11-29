import mysql.connector
from mysql.connector import errorcode
import datetime
import time

class Convert_bytearray2string (mysql.connector.conversion.MySQLConverter):
    """
        by default mysql.connector return string as bytearray, which can't json.dumps()
        got the solution from:
         https://stackoverflow.com/questions/27566078/how-return-str-from-mysql-using-mysql-connector
    """
    def row_to_python(self, row, fields):
        row = super(Convert_bytearray2string, self).row_to_python(row, fields)
        def to_unicode(col):
            if type(col) == bytearray:
                return col.decode('utf-8')
            if type(col) == datetime.datetime:
                return time.mktime(col.timetuple())
            return col
        return[to_unicode(col) for col in row]
        

class DB:
    """
    This class is tool for application to do handy mysql operation, since it's generic,
    we have to handle all error conditions when call mysql, so that if application want
    to make derive their own handy class, they don't need worry fundamental mysql stuffs
    """
    def __init__(self, h, u, p, d, buffer_cursor=True):
        try:
            self._conn = mysql.connector.connect(converter_class=Convert_bytearray2string, user=u, password=p,host=h,database=d)
        except mysql.connector.Error as err: 
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                msg="username/password error"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                msg="Database <%s> does not exist" % d
            else:
                msg=str(err)
            raise Exception('Fail MYSQL: %s' % msg)
        try:
            self._cursor = self._conn.cursor (buffered=buffer_cursor)
        except mysql.connector.Error as err: 
            raise Exception('Fail get cursor: %s' % str(err))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        try:
            self.connection.commit()
        except mysql.connector.Error as err: 
            raise Exception('commit error: %s' % str(err))

    def query(self, sql, params=None):
        try:
            self.cursor.execute(sql, params or ())
        except mysql.connector.Error as err: 
            raise Exception('execut SQL error: %s' % str(err))

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchmany(self,size):
        return self.cursor.fetchmany(size)

    def fetchone(self):
        return self.cursor.fetchone()

    def query_and_fetchall_raw (self, sql, parames=None, exclude_column=None):
        self.query(sql,parames)
        rows= self.fetchall()
        return rows

    def query_and_fetchall_json(self, sql, parames=None, exclude_column=None):
        rows = self.query_and_fetchall_raw (sql, parames, exclude_column)
        hdr = [x[0] for x in self.cursor.description]
        if len(rows) == 0:
            return None
        dict_array = []
        for r in rows:
            dict_array.append(dict(zip(hdr,r)))
        if exclude_column:
            for d in dict_array:
                for i in exclude_column:
                    d.pop(i,None)
        return dict_array
