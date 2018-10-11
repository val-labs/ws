import os, sys, time, bottle, mimetypes
mimetypes.add_type('application/wasm','wasm')
ROOT='.'
@bottle.get('/')
@bottle.get('/<path:path>')
def _(path = ROOT):
    if os.path.isdir(path):
        bottle.redirect(os.path.join('/',path,'index.html'))
    return bottle.static_file(path, ROOT)
