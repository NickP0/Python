import os
from dotenv import load_dotenv
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.client_context import ClientCredential

load_dotenv()

client_id = os.getenv("CLIENTID")
client_secret = os.getenv("CLIENTSECRET")

site_url = "" #put appropriate url

client_credentials = ClientCredential(client_id, client_secret)


ctx = ClientContext(site_url).with_credentials(client_credentials, environment='') #put appropriate environment

#Load 
files = ctx.web.lists.get_by_title("Documents").root_folder.files
ctx.load(files)
ctx.execute_query()

for file in files: #load file versions
    file_with_versions = file.expand(["Versions"]).get()
    ctx.load(file_with_versions)
    ctx.execute_query()

    for version in file_with_versions.versions: #delete file versions
        version.delete_object().execute_query()
        print(f"File: {file.properties['Name']}, Version: {version.version_label} deleted.")
