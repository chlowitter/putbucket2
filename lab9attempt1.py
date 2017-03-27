#!/usr/bin/env python
import pymysql
import web
import xml.etree.ElementTree as ET

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user'
    '/students', 'list_students',
    '/users/(.*)', 'get_students'
)

app = web.application(urls, globals())
conn = pymysql.connect(host='35.184.178.227', user='root', passwd='', db='lab9' )
class list_students:        
    def GET(self):
     cur = conn.cursor()
     self=entries
     cur.execute("SELECT * FROM entries")
     print(cur.description)
     output+='student:[';
     for name, lastName in cur.fetchall() :
        output = output + name +',' + lastName + ','
        return output

if __name__ == "__main__":
    app.run()
