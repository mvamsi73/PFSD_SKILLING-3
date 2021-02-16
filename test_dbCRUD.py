import dbCRUD
dbobj=dbCRUD.db()
#initially we are dropping all the data from the database so that we can test the working of the project perfectly and so the row count will be zero initially
rowcount=0
def test_dbCRUDinsert():
    lst=[286,"Vamsi","EYE",770243999]
    ct=len(dbobj.insert("doctor",tuple(lst)))
    assert ct==rowcount+1
rowct=1
def test_dbCRUDread():
    assert rowct==len(dbobj.read("doctor"))
def test_dbCRUDupdate():
    assert rowct==len(dbobj.update("doctor",286,"doc_name","mohan"))
def test_dbCRUDdelete():
    ct=len(dbobj.delete("doctor",286))
    assert ct==rowct-1