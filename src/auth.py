# Private Environment Info:
_info = {
  "db_url": "mongodb://admin:password@imaddsdb:27017/events"
}

# Fetch Data from Environment Info:
def fetch(key):
  return _info[key]

# Gets Credentials:
def get_creds():
  username, password = '', ''
  with open('.auth', 'r') as file:
    contents = file.read()
    lines = contents.split('\n')

    for line in lines:
      if 'USERNAME' in line:
        username = line.replace('USERNAME=', '')
      
      if 'PASSWORD' in line:
        password = line.replace('PASSWORD=', '')
  return username, password