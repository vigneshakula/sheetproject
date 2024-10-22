from flask import Flask, jsonify,request
import pandas as pd

app = Flask(__name__)


def getAssismentData(rollno) :
    rollno = rollno["Roll no"]
    df = pd.read_csv('assesmentecea.csv', storage_options=None)
    student = df[df["Roll.No"]==rollno].to_dict(orient='records')
    if len(student)>0 :
        return student[0]
    df = pd.read_csv('assesmenteceb.csv', storage_options=None)
    student = df[df["Roll.No"]==rollno].to_dict(orient='records')
    if len(student)>0 :
        return student[0]
    df = pd.read_csv('assesmentecec.csv', storage_options=None)
    student = df[df["Roll.No"]==rollno].to_dict(orient='records')
    if len(student)>0 :
        return student[0]
    return rollno

@app.post('/getstudents')
def getstudents():
        data = request.get_json()
        classname = data.get("classname")
        try:
            df = pd.read_csv('clgdata.csv', storage_options=None)
            studentsData =  df[df.columns.tolist()].to_dict(orient='records')
            ass =list(map(getAssismentData,studentsData))
            print(len(ass),len(studentsData))
            return jsonify({"data":ass})
        except Exception as e:
            print(e)
            return jsonify({"errormsg":"Something went wrong"})

@app.post("/getstudent")
def getStudent() :
     data = request.get_json()
     rollno = data["rollno"]
     try:
        df = pd.read_csv('clgdata.csv', storage_options=None)
        student = df[df["Roll no"]==rollno].to_dict(orient='records')[0]
        return jsonify({"data":student})
     except Exception as e:
        print(e)
        return jsonify({"errormsg":"something went wrong"})


if __name__ == '__main__':
    app.run(debug=True)
