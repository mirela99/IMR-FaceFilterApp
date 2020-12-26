import SimpleHTTPServer
import SocketServer
import sqlite3 as sl

PORT = 8888
con = sl.connect('my-test.db')
with con:
    data = con.execute("SELECT * FROM USER")
    for row in data:
        print(row)

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    pass

Handler.extensions_map['.wasm'] = 'application/wasm'

httpd = SocketServer.TCPServer(("", PORT), Handler)


print ("serving at port") , PORT
httpd.serve_forever()

