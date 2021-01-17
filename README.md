# Pastin

Pastin is a pastebin service written in Python 3 using Flask.

## Dev setup

1. Clone repository to local computer and go into it
```bash
git clone https://github.com/pastebin-fi/pastin.git
cd pastin/
```
2. Install required packages `pip install -r requirements.txt`
3. Copy file `defconfig.ini` to `config.ini` and make required changes
4. Database configuration is in Environment variables. Here is an example `.env`-file:
```env
DB_USER = root
DB_PASSWORD = password
DB_HOST = localhost
DB_DB = pastin
```
5. Run the following command (run this also when updating pastin):
```bash
flask db upgrade
```
6. Run the server `flask run`

### Branching

In order to easily switch between branches, there is the script checkout.sh.
This script modifies config.ini to use a database called pastin_branch, where
branch is the name of the branch to which you are switching. The name of the
database of the master branch is just pastin. You must yourself create the
databases and grant your database user privileges to them.

To switch to another branch, use
`./checkout.sh <branch>`
