from flask import Flask
import re
import cobra.mit.access
import cobra.mit.session
import cobra.mit.request
import cobra.model.fv
app = Flask(__name__)
'''
@app.route('/')
def hello_world():
    return 'Hello World'
'''
#@app.route('/getTenant')
'''
@app.route('/')
def hello_america():
    return "Hello America"
'''

@app.route('/hello/<name>')
def hello_america(name):
    return "Hello America %s!" % name


'''
def get_tenant():
     apicUrl = 'https://172.17.42.1/'
     loginSession = createCertSession()
     moDir = MoDirectory(loginSession)
     moDir.login()
     tenantMo = moDir.lookupByClass('fvTenant');
     moDir.logout()
     return respFormatJsonMos(tenantMo, tenantMo.totalCount)
'''


@app.route('/getTenant')
def get_Tenant_info():
    ls = cobra.mit.session.LoginSession('https://10.201.35.211', 'admin', 'C1sc0123')
    md = cobra.mit.access.MoDirectory(ls)
    md.login()
    tenantMo = md.lookupByClass('fvTenant')
    for item in tenantMo:
        tenantName = str(item.dn)
        return tenantName
    md.logout()




if __name__ == '__main__':
    app.run(host='localhost',port=5454,debug = True)
    #app.add_url_rule('/', 'hello', hello)