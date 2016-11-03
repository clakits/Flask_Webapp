from flask import Flask, redirect, url_for, request, flash, g, render_template

from cobra.mit.access import MoDirectory
from cobra.mit.session import CertSession
from cobra.mit.session import LoginSession
from cobra.model.pol import Uni as PolUni
from cobra.model.aaa import UserEp as AaaUserEp
from cobra.model.aaa import User as AaaUser
from cobra.model.aaa import UserCert as AaaUserCert
from cobra.internal.codec.jsoncodec import toJSONStr, fromJSONStr
from cobra.internal.codec.xmlcodec import _toXMLStr, fromXMLStr
from cobra.mit.request import ClassQuery
from cobra.mit.request import TraceQuery
import json

app = Flask(__name__)

def createCertSession():
    certUser = 'Cisco_HelloAciStateful'
    pKeyFile = '/home/app/credentials/plugin.key'

    polUni = PolUni('')
    aaaUserEp = AaaUserEp(polUni)
    aaaUser = AaaUser(aaaUserEp, certUser)

    aaaUserCert = AaaUserCert(aaaUser, certUser + '-cert')

    with open(pKeyFile, "r") as file:
        pKey = file.read()

    apicUrl = 'https://172.17.42.1/'
    session = CertSession(apicUrl, aaaUserCert.dn, pKey, secure=False)
    return session

def respFormatJsonMos(mos, totalCount):
    jsonStr = '{"totalCount": "%s", "imdata": [' % totalCount
    first = True
    for mo in mos:
        if not first:
            jsonStr += ','
        else:
            first = False
        jsonStr += toJSONStr(mo, includeAllProps=True)
    jsonStr += ']}'
    jsonDict = json.loads(jsonStr)

    return json.dumps(jsonDict)

@app.route('/')
def hello_world():
    return 'Cisco HelloACI PlugIn Version 1.0.'

@app.route('/getTenant.json')
def get_tenant():
    with open("/Users/clakits/Documents/ACI/AppCenter/log/log.txt", "a") as log_file:
        log_file.write("==================================================" + "\n")
        log_file.write("Received API Request from Client. Sending Response" + "\n")
        log_file.write("==================================================" + "\n")

    tableList = []

    row = ('Tenant')

    tableList.append(row)
    apicUrl = 'https://10.22.47.171/'
    #loginSession = createCertSession()
    loginSession = LoginSession(apicUrl, 'admin', 'ins3965!')
    moDir = MoDirectory(loginSession)
    moDir.login()
    #tenantMo = moDir.lookupByClass('fvTenant');
    q = ClassQuery('fvTenant')
    q.subtree = 'children'
    tenantMo = moDir.query(q)
    moDir.logout()
    print tenantMo.totalCount
    for item in tenantMo:
        row = str(item.dn)
        print row
        tableList.append(row)
    #return respFormatJsonMos(tenantMo, tenantMo.totalCount)

    return render_template('result1.html', table=tableList)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4545)
