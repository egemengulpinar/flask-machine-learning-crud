import os
import datetime
import crud
import model
import server

os.system('dropdb people-flask')
os.system('createdb people-flask')

model.connect_to_db(server.app)
model.db.create_all()


user1 = crud.create_user("Kim", "kim.possible@test.com",
                         datetime.date(2002, 1, 7), 81433)
user2 = crud.create_user(
    "Jake Long", "sunwoo_dragon@test.com", datetime.date(2005, 1, 21), 10022)
user3 = crud.create_user(
    "Olie", "rollin.cool@test.com", datetime.date(1998, 10, 4), 60412)
user4 = crud.create_user("Lilo", "alien_surf@test.com",
                         datetime.date(2001, 6, 16), 96816)
user5 = crud.create_user(
    "Hercules", "thee_strongest@test.com", datetime.date(1995, 1, 16), 90210)
