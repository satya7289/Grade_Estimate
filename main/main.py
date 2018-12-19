import os

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    alphabet = ['A','B','C','D','F']
    number = ['5','4','3','0']
    return render_template("index.html", alpha=alphabet, num=number)

    if __name__ == "__index__":
        index()


@app.route('/grade', methods=["POST", "GET" ])
def Grade():
    result = request.form
    grades = []
    cradits = []
    subject = []
    t_cradit,s_cradit,i = 0, 0, 0
    for ans in result:
        if (i%2!=0):
            grades.append(result.get(ans))
        else:
            cradits.append(result.get(ans))
        i=i+1
        print(ans)

    for cradit in cradits:
        t_cradit += int(cradit)

    dictionary = {'A':10, 'B':8, 'C':6, 'D':4,'F':0}
    i = 0
    for grade in grades:
        s_cradit += dictionary[grade]*int(cradits[i])
        i += 1
    f_cradit = s_cradit/t_cradit
    print(f_cradit)
    return render_template("grade.html",Cradit=cradits,Grade=grades,cgpa=f_cradit, sub=subject)
