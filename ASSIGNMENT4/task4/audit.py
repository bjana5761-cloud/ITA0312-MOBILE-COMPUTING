def audit(app):
    findings=[]
    if 'READ_CONTACTS' in app['permissions'] and len(app['permissions'])>1:
        findings.append(('E','Over-privileged permissions','Repair: request only at feature use'))
    if app.get('plain_token'):
        findings.append(('I','Plaintext auth token','Repair: Keystore-backed key + encrypted storage'))
    if app.get('http'):
        findings.append(('T/I','Cleartext network','Repair: TLS 1.3 + certificate pinning'))
    if app.get('unverified_update'):
        findings.append(('T','Unverified update source','Repair: same-signer verified installation'))
    return findings

app={'permissions':['READ_CONTACTS','CAMERA','ACCESS_FINE_LOCATION'],'plain_token':True,'http':True,'unverified_update':True}
for f in audit(app): print(f)
