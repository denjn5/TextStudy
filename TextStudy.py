"""
The simplest of web servers.
 
"""
import bottle as web
import os


# Memory Game
@web.route('/')
@web.route('/<filename>')
def index(filename):
    res_path = os.path.dirname(os.path.realpath(__file__)) + r'\Apps'
    print('res_path: ' + res_path)
    return web.static_file(filename, root=res_path)


# External files (may get via cdn or store here for times when I'm disconnected)
@web.route('/External/<filename>')
def index(filename):
    res_path = os.path.dirname(os.path.realpath(__file__)) + r'\External'
    #print('res_path: ' + res_path)
    return web.static_file(filename, root=res_path)

web.run(host='localhost', port=8080, debug=True)
