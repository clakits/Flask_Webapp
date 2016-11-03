from flask import Flask, render_template, redirect, url_for, request, flash, g
import re
import cobra.mit.access
import cobra.mit.session
import cobra.mit.request
import cobra.model.fv
from cobra.mit.access import MoDirectory
from cobra.mit.session import CertSession
from cobra.mit.session import LoginSession
from cobra.model.pol import Uni as PolUni
from cobra.model.aaa import UserEp as AaaUserEp
from cobra.model.aaa import User as AaaUser
from cobra.model.aaa import UserCert as AaaUserCert
from cobra.internal.codec.jsoncodec import toJSONStr, fromJSONStr
from cobra.internal.codec.xmlcodec import _toXMLStr, fromXMLStr
import json

from cobra.mit.naming import Dn
from cobra.mit.request import DnQuery
from cobra.mit.request import ClassQuery
from cobra.mit.request import TraceQuery

import re
import time
from tabulate import tabulate
app = Flask(__name__)
'''
@app.route('/')
def hello_world():
    return 'Hello World'
'''
#@app.route('/getTenant')
'''
@app.route('/hello')
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


@app.route('/')
def get_Tenant_info():
    tableList = []
    row = ('Tenant')
    tableList.append(row)
    ls = cobra.mit.session.LoginSession('https://10.29.198.36', 'admin', 'ins3965!')
    md = cobra.mit.access.MoDirectory(ls)
    md.login()
    q = ClassQuery('fvTenant')
    q.subtree = 'children'
    tenantMo = md.query(q)
    #tenantMo = md.lookupByClass('fvTenant')
    print tenantMo.totalCount
    for item in tenantMo:
        row = str(item.dn)
        print row
        tableList.append(row)
    md.logout()
    return render_template('result1.html', table=tableList)
    #return render_template('home.html', table=tableList)


if __name__ == '__main__':
    app.run(host='localhost',port=4444)
    #app.add_url_rule('/', 'hello', hello)