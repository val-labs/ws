import os, bottle, mimetypes

mimetypes.add_type('application/wasm','.wasm')

def make_static_mount(root):
    def static_file(path):
        if os.path.isdir(path):
            bottle.redirect(os.path.join('/',path,'index.html'))
        return bottle.static_file(path, root)
    return static_file

static_mount = make_static_mount('.')

@bottle.get('/')
@bottle.get('/<path:path>')
@bottle.get('/<path:path>/')
def _(path = ''):
    return static_mount(path)
