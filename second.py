from flask import json, send_file ,request
from flask.app import Flask 
from os import name, path
import re
from flask import Flask , request ,redirect ,url_for,render_template
from flask import jsonify
from app import app
import numpy as np
from queue import PriorityQueue
from collections import defaultdict
from pprint import pprint
import cv2 
from collections import deque
import os
import base64


stringofimage = " String "
A= np.loadtxt(r"C:\Users\user\Downloads/coordinates.txt",delimiter=',')
Edges = np.loadtxt(r"C:\Users\user\Downloads/edges.txt",delimiter=',')
spl=[]
dictt = {1: (347, 611), 2: (378, 587), 3: (347, 574), 4: (381, 557), 5: (383, 425), 6: (400, 375), 7: (440, 342), 8: (482, 332), 9: (539, 295), 10: (580, 281), 11: (613, 273), 12: (573, 263), 13: (602, 247), 14: (591, 217), 15: (564, 212), 16: (529, 201), 17: (502, 177), 18: (465, 158), 19: (451, 146), 20: (442, 130), 21: (414, 117), 22: (373, 101), 23: (350, 81), 24: (306, 82), 25: (230, 82), 26: (207, 80), 27: (202, 38), 28: (171, 30), 29: (207, 62), 30: (125, 60), 31: (13, 65), 32: (13, 106), 33: (15, 139), 34: (18, 185), 35: (23, 272), 36: (51, 299), 37: (127, 306), 38: (123, 361), 39: (113, 408), 40: (108, 460), 41: (158, 476), 42: (212, 475), 43: (206, 553), 44: (229, 576), 45: (251, 567), 46: (242, 593), 47: (264, 607), 48: (272, 590)}

########################
def  H (n,end):
        return np.sqrt(np.sum((A[n-1]-A[end-1])**2))


class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
    def get_neighbors(self, v):
        return self.adjac_lis[v]  
    # This is heuristic function which is having equal values for all nodes
    def  h (self,n,end):
        return np.sqrt(np.sum((A[n-1]-A[end-1])**2))   
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
  #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v,stop) < poo[n] + self.h(n,stop):
                    n = v;
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    spl.append(n)
                    n = par[n]
 
                reconst_path.append(start)
                spl.append(start) 
                
 
                reconst_path.reverse() 
                spl.reverse()
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            # for all the neighbors of the current node do
            for m in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                l=list(m)
                weight=m.get(l[0])
                m=l[0]
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m) 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None  



def draw (path , img) : 
    for i in range (0,len(path)-1) : 

        id_1 = path[i] 
        id_2 = path[i+1] 
        p1 = dictt[id_1] 
        p2 = dictt[id_2] 
        cv2.line(img , p1 ,p2 , (255,0,0) , thickness = 15 ) 
        
    cv2.imshow("img" , img) 
    #cv2.waitKey(0)
    imagepathD=r'D:\flutterprojects\flask\static'
    os.chdir(imagepathD)
    filename='localmap.jpg'
    cv2.imwrite(filename, img)
    imagepathD2=r'D:\self_d_c\images'
    os.chdir(imagepathD2)
    filename2='localmap.jpg'
    cv2.imwrite(filename2, img)
    #data["img"] = base64.b64encode(img.read()).decode('ascii')
    #with open(filename, "rb") as img_file:
    #    b64string = base64.b64encode(img_file.read())
    #print(" The String IS without b::: ",b64string.decode('utf-8'))

    #stringofimage=str(b64string.decode('utf-8'))



    return img 

def funstring():
    with open("localmap.jpg", "rb") as img_file:
        b64string = base64.b64encode(img_file.read())
    print(" The String IS without b::: ",b64string.decode('utf-8'))

    stringofimage=str(b64string.decode('utf-8'))
    return stringofimage
        

#Login
#app=Flask(__name__)
#@app.route('/',methods=['POST','GET'])
#def login():

##########################
   #d={}
    #d['Query']= str(request.args['Query'])
    #return jsonify(d)
 

app=Flask(__name__,template_folder='templates')
picfolder=os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picfolder
@app.route('/<int:node>',methods = ['GET'])
def sucess(node):
    AdjacencyMatrix=np.zeros((48,48))
    for i in range(47):

        AdjacencyMatrix[int(Edges[i][0])][int(Edges[i][1])]=Edges[i][2]

    #The AdjacencyMatrix is not zerobased
    AdjacencyMatrix

    AdjacencyList = defaultdict(list)
    edges = set()

    for i, v in enumerate(AdjacencyMatrix, 0):
        for j, u in enumerate(v, 0):
            if u != 0 and frozenset([i, j]) not in edges:
                edges.add(frozenset([i, j]))
                AdjacencyList[i].append({j: u})
    graph1 = Graph(AdjacencyList)
    img = cv2.imread(r'C:\Users\user\Desktop/map.jfif')   
    path = graph1.a_star_algorithm(1, node)              
    ###################
    
    #os.chdir(imagepathD)
    #filename='localmap.jpg'
    #cv2.imwrite(filename, draw(path,img))
    #imag1=draw(path,img)
    
 
    #with open("static\localmap.jpg", "rb") as img_file:
    #    b64string = base64.b64encode(img_file.read())
    #print(" The String IS without b::: ",b64string.decode('utf-8'))

    

    return jsonify({"Path":draw(path,img),"Path" : path ,"imagestring": funstring()})

    "{'Id1':'2','Id2':'2'}"
    "{'Id1':'2'},{'Id2':'2'}"

  


@app.route('/index' , methods=['GET', 'POST'])
def index():
    name= "localmap.jpg"
    return  render_template('index.html')      
################################################################# ##Get ##
#######################################################################
#@app.route('/image',methods=['GET'])
#def image():
#    img = cv2.imread(r'C:\Users\user\Desktop/map.jfif')
#    return draw (path , img )  
# // lazem check el ip_address  

#with open("static\localmap.jpg", "rb") as img_file:
#    b64string = base64.b64encode(img_file.read())
#print(" The String IS without b::: ",b64string.decode('utf-8')) 

if __name__== '__main__':
    app.run(host='192.168.1.100',port=5000,debug=True)  




 ####################################################################     
