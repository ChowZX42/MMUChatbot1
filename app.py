from flask import Flask, render_template, request
#import os
import aiml
# from autocorrect import spell
from autocorrect import Speller
spell = Speller()
import re

app = Flask(__name__)

BRAIN_FILE ="./pretrained_model/aiml_pretrained_model.dump"
k = aiml.Kernel()

'''
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)
    '''

#print("Parsing aiml files")
#k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")

@app.route("/")
def home():
    k.learn("std-startup.xml")
    k.respond("load aiml b")
    
    return render_template("index.html")

'''
def common_data(list1, list2):
    result = False
  
    # traverse in the 1st list
    for x in list1:
  
        # traverse in the 2nd list
        for y in list2:
    
            # if one common
            if x == y:
                result = True
                return result 
                  
    return result
'''

@app.route("/get")
def get_bot_response():
    specialWord = ['Hello','Enquiries','FIST', 'AI', 'BIT', 'BCS', 'BS']
    query = request.args.get('msg')
    removePunc = re.sub(r'[^\w\s]','',query)
    querySplit = removePunc.split()
#    print('querySplit = ')
    print(querySplit)

    '''
    for sW in specialWord:
        if query == sW:
            response = k.respond(query)
        else:
            continue
    query = [spell(w) for w in (query.split())]
    print(query)
    question = " ".join(query)
    print(question)
    response = k.respond(question)
#   response = k.respond(query)


    if common_data(querySplit, specialWord):
        commonElement = list(set(querySplit).intersection(specialWord))
        response = k.respond(query)
    else:
        query = [spell(w) for w in querySplit if not commonElement]
        print(query)
        question = " ".join(query)
        print(question)
        response = k.respond(question)
'''
    commonElement = list(set(querySplit).intersection(specialWord))
#    print('Common Element: ', commonElement)
    queryExclude = [i for i in querySplit if i not in commonElement]
#    queryExclude = [w for i,w in enumerate(querySplit) if w != sW for sW in commonElement]
#    print('queryExclude = ')
    print(queryExclude)
    query = [spell(w) for w in queryExclude]
#    print('query = ')
    print(query)

#    for ct, i in enumerate(commonElement):
#        print(ct)
#        index = querySplit.index(i) + ct
#        query.insert(index, i)
#        print('The index of', i, 'in the list is:', index)

    for i in commonElement:
        index = querySplit.index(i)
        query.insert(index, i)
        print('The index of', i, 'in the list is:', index)  

        
#    query.insert(querySplit.index('FIST'), 'FIST')
#    print(query)
    question = " ".join(query)
#    print('question = ')
    print(question)
    response = k.respond(question)
#    response = k.respond(query)
    
    responseFinal = response.replace('\\n', '<br/>')
#    responseSplit = response.split() 
#    responseExclude = ['\n' for i in responseSplit if i!= '\\n']
#    for i in responseSplit:
#        responseExclude = i.replace('\\n', '\n' ) 
#    responseFinal = " ".join(query)
 
    if response:
#        print('responseFinal = ')
#        print (str(responseFinal))
#        print('responseExclude = ')
#        print (responseExclude)
        return (str(responseFinal))
        #return (str(response))
    else:
        return (str('What you are saying is out of my understanding! You can ask me the question regarding MMU FIST <br/> For more enquiry regarding the the topic outside MMU FIST, please type "More Enquiries" to get more details.'))
    


if __name__ == "__main__":
    app.run()
    # app.run(host='127.0.0.1', port='5000')


