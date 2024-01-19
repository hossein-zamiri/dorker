from flask import Flask, render_template
from urllib.parse import quote as encode
app = Flask(__name__, template_folder='templates')

@app.route("/<d>")
def home(d):
    domain = d
    dorks = [
    'inurl:&',
    'ext:php | ext:aspx | ext:asp | ext:jsp | ext:html | ext:htm',
    'ext:log | ext:txt | ext:conf | ext:cnf | ext:ini | ext:env | ext:sh | ext:bak | ext:backup | ext:swp | ext:old | ext:~ | ext:git | ext:svn | ext:htpasswd | ext:htaccess | ext:xml',
    'inurl:url= | inurl:return= | inurl:next= | inurl:redir= inurl:http',
    'inurl:http | inurl:url= | inurl:path= | inurl:dest= | inurl:html= | inurl:data= | inurl:domain= | inurl:page= inurl:&',
    'inurl:config | inurl:env | inurl:setting | inurl:backup | inurl:admin | inurl:php',
    'inurl:email= | inurl:phone= | inurl:password= | inurl:secret= inurl:&',
    'inurl:apidocs | inurl:api-docs | inurl:swagger | inurl:api-explorer',
    'inurl:cmd | inurl:exec= | inurl:query= | inurl:code= | inurl:do= | inurl:run= | inurl:read= | inurl:ping= inurl:&',
    'inurl:(unsubscribe|register|feedback|signup|join|contact|profile|user|comment|api|developer|affiliate|upload|mobile|upgrade|password)',
    'intitle:"Welcome to Nginx"',
    'site:http://ideone.com | site:http://codebeautify.org | site:http://codeshare.io | site:http://codepen.io | site:http://repl.it | site:http://justpaste.it | site:http://pastebin.com | site:http://jsfiddle.net | site:http://trello.com',
    'site:groups.google.com',
    'site:docs.google.com/spreadsheets',
    'ext:pdf intext:confidential',
    f"intitle:{domain} apikey or ApiKey",
    'intext:"Powered by" & intext:Drupal & inurl:user',
    'inurl:/wp-admin/admin-ajax.php',
    'site:*/server-status apache',
    'site:*/joomla/login',
    '"choose file"',
    'inurl:apidocs | inurl:api-docs | inurl:swagger | inurl:api-explorer',
    'inurl:email= | inurl:phone= | inurl:password= | inurl:secret= inurl:&',
    'inurl:config | inurl:env | inurl:setting | inurl:backup | inurl:admin | inurl:php',
    'inurl:cmd | inurl:exec= | inurl:query= | inurl:code= | inurl:do= | inurl:run= | inurl:read= | inurl:ping= inurl:&',
    'inurl:include | inurl:dir | inurl:detail= | inurl:file= | inurl:folder= | inurl:inc= | inurl:locate= | inurl:doc= | inurl:conf= inurl:&',
    'inurl:http | inurl:url= | inurl:path= | inurl:dest= | inurl:html= | inurl:data= | inurl:domain= | inurl:page= inurl:&',
    'inurl:id= | inurl:pid= | inurl:category= | inurl:cat= | inurl:action= | inurl:sid= | inurl:dir= inurl:&',
    'inurl:url= | inurl:return= | inurl:next= | inurl:redir= inurl:http',
    'inurl:q= | inurl:s= | inurl:search= | inurl:query= inurl:&',
    'site:s3.amazonaws.com',
    'site:blob.core.windows.net',
    'site:googleapis.com',
    'site:drive.google.com',
    'site:dev.azure.com',
    'site:onedrive.live.com',
    'site:digitaloceanspaces.com',
    'site:sharepoint.com',
    'site:s3-external-1.amazonaws.com',
    'site:s3.dualstack.us-east-1.amazonaws.com',
    'site:dropbox.com/s',
    'site:box.com/s',
    'site:docs.google.com inurl:"/d/"',
    'site:jfrog.io',
    'site:firebaseio.com'


    ]
    dorks_with_domain =[]
    for dork in dorks:
        if "site:" in dork:
            encoded = f"{encode(dork)} \"{encode(domain)}\""
            dorks_with_domain.append(encoded)

        elif "apikey" in dork:
            encoded = f"{encode(dork)}"
            dorks_with_domain.append(encoded)
    
        else:
            encoded = f"{encode(dork)} site:{encode(domain)}"
            dorks_with_domain.append(encoded)
    return render_template('sest.html', dorks=dorks_with_domain,domain=domain)
if __name__ == "__main__":
    app.run()



