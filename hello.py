from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'
	
@app.route('/products/')
def products_list():
  return 'Listing of all products we have.'

@app.route('/products/<product_id>/')
def product_detail(product_id):
  return 'Detail of product     #{}.'.format(product_id)

@app.route( 
  '/products/<product_id>/edit/',
  methods=['GET', 'POST'])
def product_edit(product_id):
  return 'Form to edit product #.'.format(product_id)

@app.route( '/products/create/', methods=['GET', 'POST'])
def product():
  return 'Form to create a new product.'

@app.route('/products/<product_id>/delete/', methods=['DELETE'])
def product_delete(product_id):
    raise NotImplementedError('DELETE')

from flask import Flask, make_response,request 


@app.route('/string/')
def return_string():
  dump = dump_request_detail(request)
  return 'Hello, world!'

@app.route('/object/')
def return_object():
  dump = dump_request_detail(request)
  headers = {'Content-Type': 'text/plain'}
  return make_response(Response('Hello, world! \n' + dump, status=200,
    headers=headers))

@app.route('/tuple/<path:resource>')
def return_tuple(resource):
  dump = dump_request_detail(request)
  return 'Hello, world! \n' + dump, 200, {'Content-Type':
    'text/plain'}


def dump_request_detail(request):
  request_detail = """
## Request INFO ##
request.endpoint: {request.endpoint}
request.method: {request.method}
request.view_args: {request.view_args}
request.args: {request.args}
request.form: {request.form}
request.user_agent: {request.user_agent}
request.files: {request.files}
request.is_xhr: {request.is_xhr}

## request.headers ##
{request.headers}
  """.format(request=request).strip()
  return request_detail

if __name__ == '__main__':
    app.run()