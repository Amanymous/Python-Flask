from mongoengine import connect
from model import Id,TITLE,Description,Done

connect(host="mongodb+srv://bootcamp:bootcamp@cluster0-r0lyg.mongodb.net/test?retryWrites=true&w=majority")

def initData():
    id = Id(name="32452343242")
    id.save()

    title = TITLE(name= "aman")
    title.save()

    description = Description(name="abcdefghijklmnopqrstuvwxyz")
    description.save()

    done = Done(name="true")
    done.save()





