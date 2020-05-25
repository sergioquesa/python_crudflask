from flask import Flask,jsonify,render_template,request,redirect
from claseconnect import *
import pymysql

app=Flask(__name__)

@app.route('/')
def presentacion():
    return render_template('inicio.html')

@app.route('/<name>')
def saludo(name):
    return "hola don/doña " + str(name)

@app.route('/add',methods=["POST"])
def add():
    try:
        nombre=request.form.get("nombre")
        apellido=request.form.get("apellido")
        cone=Claseconnect()
        cone.EjecutarSql("INSERT INTO personal (nombre,apellido) VALUES('"+nombre+"','"+apellido+"')")
        datos=cone.DevolverDatos()
        cone.RealizaCambios()
        print (datos)
    except Exception:
        cone.DeshacerCambios()
        print("error en las altas")
    return redirect("/all")

@app.route('/update',methods=["POST"])
def update():
    id=request.form.get("id")
    nombre=request.form.get("nombre")
    apellido=request.form.get("apellido")
    cone=Claseconnect()
    cone.EjecutarSql("UPDATE personal SET nombre='"+nombre+"',apellido='"+apellido+"' WHERE id="+id)
    cone.RealizaCambios()
    return redirect("/all")

@app.route('/delete',methods=["GET","POST"])
def delete():
    try:
        id=request.form.get('id')
        cone=Claseconnect()
        cone.EjecutarSql("DELETE FROM personal WHERE id="+id)
        cone.RealizaCambios()
    except Exception:
        cone.DeshacerCambios()
        print("error en las bajas")
    return redirect("/all")

@app.route('/list')
def listaralumnos():
    cone=Claseconnect()
    cone.EjecutarSql("SELECT * FROM personal")
    datos=cone.DevolverDatos()
    respu=jsonify(datos)
    cone.CerrarBasededatos()
    return render_template

@app.route('/view')
def listview():
    cone=Claseconnect()
    cone.EjecutarSql("SELECT * FROM personal")
    data=cone.DevolverDatos()
    cone.CerrarBasededatos()
    return render_template('listado.html',datos=data)

@app.route('/all')
def listall():
    cone=Claseconnect()
    cone.EjecutarSql("SELECT * FROM personal")
    data=cone.DevolverDatos()
    cone.CerrarBasededatos()
    return render_template('index.html',datos=data)

if __name__=="__main__":
    app.run()