# roam-research-to-sqlite

Save data from Roam Research's JSON expot file to a SQLite database.

## Install

```console
foo@bar:~$ pip install -e git+https://github.com/myles/roam-research-to-sqlite.git#egg=roam-research-to-sqlite
```

## Usage

You'll first need to export your Roam Research graph as a JSON format. You 
can do that by clicking the three dots, _Share, export and more_ icon, on 
the top right hand side and going to _Export All_. Make sure you use the 
export format JSON and export the Zip file.

You can then run the command using:

```console
foo@bar:~$ roam-research-to-sqlite roam-research.db Roam-Export-1672368714467.zip
```
