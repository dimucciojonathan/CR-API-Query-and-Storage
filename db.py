import sqlite3
import Query


# My tag is 'YYRVLLUV'
def insert_data(tag):
    tag, user, expLevel, trophies, wins, losses, best = Query.player_info(tag)

    conn = sqlite3.connect("cr.db")
    c = conn.cursor()

    c.execute("INSERT INTO profile VALUES (:tag, :name, :expLevel, :trophies, :wins, :losses, :bestTrophies)",
          {'tag': tag, 'name': user, 'expLevel': expLevel, 'trophies': trophies, 'wins': wins, 'losses': losses, 'bestTrophies': best})

    conn.commit()
    conn.close()






# c.execute("""CREATE TABLE profile (
#            tag text,
#            name text,
#            expLevel text,
#            trophies integer,
#            wins integer,
#            losses integer,
#            bestTrophies integer
#    )""")


