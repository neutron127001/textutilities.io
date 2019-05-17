from flask import Flask,render_template,request,redirect
import json
import re


with open('config.json','r') as f:
    params=json.load(f)['params']

app=Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html',params=params)

@app.route('/operate',methods=['POST','GET'])
def operation():
    if (request.method=='POST'):
        analyse=''
        text=request.form.get('text')
        punct=request.form.get('punct')
        caps=request.form.get('caps')
        line=request.form.get('line')
        extra_s=request.form.get('extra')
        char=request.form.get('char')
#removing various punctuations
        if (punct == "on"):
            a="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
            for i in text:
                if i not in a:
                    analyse+=i
            text=analyse
#making text into capital
        if (caps=="on"):
            analyse=text.upper()
            text=analyse
#removing line spaces            
        if (line == 'on'):
            analyse=''
            for i in text:
                if (i != "\n") and (i !="\r"):
                    analyse+=i
            text=analyse
#removing in middle space
        if (extra_s == 'on'):
            analyse=''
            analyse=re.sub(' +', ' ',text)
            text=analyse
#         
        if (char=='on'):
             count=0
             for i in text:
                 if i != ' ':
                     count+=1
             text=count
                
                
        return render_template('index.html',analyse=analyse,params=params,text=text)
            
            
    else:
        return redirect('/')

        

    
   
if __name__=="__main__":
    app.run(debug=True)
