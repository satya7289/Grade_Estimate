import os

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/' ,methods=["POST","GET"])
def index():
    alphabet = ['A','B','C','D', 'E', 'F']
    number = ['5','4','3','2','1','0']
    n = request.form.get('choose')
    if n is None:
        return render_template("index.html", alpha=alphabet, num=number, N=6)
    else:
      return render_template("index.html", alpha=alphabet, num=number,N=int(n))

    if __name__ == "__index__":
        index()


@app.route('/grades', methods=["POST", "GET" ])
def grades():
    i, t_cradit, s_cradit = 0, 0, 0
    grades, cradits, subject, ans = [], [], [], []
    dictionary = {'A': 10, 'B': 8, 'C': 6, 'D': 4, 'E':2, 'F': 0}
    result = request.form
    if result is None:
        return render_template("error.html",message='Complete the form')
    n = int(len(result)/3)
    for x in result:
        ans.append(x)

    while(i<=(len(result)-3)):
        subject.append(result.get(ans[i]))
        cradits.append(result.get(ans[i+1]))
        grades.append(result.get(ans[i+2]))
        i=i+3
    for cradit in cradits:
        t_cradit = t_cradit + int(cradit)

    if(t_cradit==0):
        return render_template("error.html",message='fill cradit carefully')
    i = 0
    for grade in grades:
        s_cradit += ( dictionary[grade]* int(cradits[i]) )
        i += 1
    f_cradit = s_cradit / t_cradit

    #print(ans,subject,cradits,grades,t_cradit,s_cradit,f_cradit,n)
    print(ans, subject, len(result), len(ans), n)
    return render_template("grade.html", Cradit=cradits, Grade=grades, cgpa=f_cradit, sub=subject, N=n)

    """
    print(ans,len(result),len(ans),n,result)
    return render_template('error.html')
    """









