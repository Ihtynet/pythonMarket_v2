"""
Интернет магазин
 """
from flask import Flask, render_template,request
import sqlite3


app = Flask(__name__)

@app.route('/')
def startpage():
    title = "Каталог магазина"

    conn    = sqlite3.connect("mamarket.db")
    cursor  = conn.cursor()
    select_query = """SELECT * from tovary"""
    cursor.execute(select_query)
    records = cursor.fetchall()
    print(records)
    res_list = []
    for s in  records:
        d1 = {"name":s[0], "price":s[1], "image":s[2]}
        res_list.append(d1)        

    print(res_list)


    return render_template("catalog.html", title=title, res_list = res_list)


if __name__ == '__main__':
    app.run()
