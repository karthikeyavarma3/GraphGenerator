import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import time
from PIL import Image
import cv2


lst = []

print(''' 
                    Enter 0 : UNDIRECTED GRAPH 
                    Enter 1 : DIRECTED GRAPH
        ''')


c = int(input('''
                    Type of graph : '''))


ver = int(input('''
                    Enter no of vertices in the matrix : ''')
                    )


for i in range(1 , ver+1):
    a=[]

    print("Row : " , i ,)

    for j in range(1 , ver+1):

        a.append(int(input()))
        
    lst.append(a)

#print(lst)


lst = np.array(lst)
#print(lst)


print('''
                    Converting .... 
            ''')


time.sleep(3)


try:
    if c==0:

        lx = nx.from_numpy_array(lst , create_using=nx.MultiGraph)
        

    elif c==1:
        lx = nx.from_numpy_array(lst , create_using=nx.MultiDiGraph)

    else:
        print('''
                            Invalid
                        
                ''')
        quit()

except Exception as e:
    print(''' 
                        Failure!

                ''')
    time.sleep(1)

    print('''
                        Problem detected : ''', e
            )
    

obj = nx.draw_circular(lx , with_labels = True)

fig = plt.gcf()
fig.canvas.draw()
image = np.array(fig.canvas.renderer.buffer_rgba())
print(image)
plt.show()






while True:
        if c==0:

            print('''           
                            Do you want to find the degree of the nodes ? 
                                -Enter 1 to continue and 0 to exit- 
            ''')
            a = int(input(''' 
                            Enter choice : ''')
                            )

            if a==1:
                
                node = eval(input('''
                            Enter the node : 
                            '''))
                
                print(''' 
                            Degree : ''', lx.degree[node]
                )
        
            elif a==0:
                break

            else:
                print('''
                            Wrong input''')
                break

        elif c==1:
            print('''           
                            Do you want to find the degree of the nodes ? 
                                -Enter 1 to continue and 0 to exit-
            ''')
            a = int(input())

            if a==1:
                print('''
                            Enter the node :
                    ''')
            

                node = eval(input('''
                            Enter the node : '''))

                print('''
                            
                            In-Degree = ''',lx.in_degree[node],
                    '''
                            Out-Degree = ''',lx.out_degree[node]
                 )

            elif a==0:
                break

            else:
                print('''
                            Wrong input''')
                break

        

while True:
    print(''' 
                            Do you want to find tthe shortest path between 2 nodes : 
                                    ---Enter 1 to continue and 0 to exit---
                            ''')

    ans = int(input('''
                            Choice  : 
                            '''))

    if ans==1:
        
        node_a = eval(input(''' 
                            Enter first node : '''))    

        node_b = eval(input('''
                            Enter the second node : '''))   

        shortest_path = nx.shortest_path(lx , node_a , node_b)           

        print('''
                            The shortest path is : ''' , shortest_path)    

    
    elif ans==0:

        break

    else:
        print('''  
                            Wrong Input
                            ''')


print('''
                            Thank You :)
    
                       ---Please Visit Again---  
    ''')





            

