#boolean

#var1 = True
#var2 = False
#print(var1,var2)
#print(type(var1),type(var2))


#list , array

#ls = [25,30,56,87,7.8,'harsh',True]
#print(ls)
#print(type(ls))

#ls = [10,20,30,40,50]
#print(ls[1:5])

#ls = [5,10,13,14,'upflairs',23]
#var = ls[4]
#print(var[4:7])
#print(ls[4][4:7])

#st = ['harsh','yash','aditya']
#st[1] = 'bittu'          #update or manipulation
#print(st)

#st.append('himanshu')    #insert at last position
#print(st)

#st.pop()                 #remove the last item
#print(st)

#st.insert(0,'abhi')      # insert at any position
#print(st)

#st.remove('bittu')       # delete at any position
#print(st)

#del st[2]                # delete at any position by indexing
#print(st)

#print(st.count('harsh'))

#ls1 = ['a','b','c','d']
#ls2 = [10,80,70,50,40]

#ls1.reverse()            # ls1[::-1]
#ls2.sort()               # ascending order
#print(ls1,ls2)

#ls2.sort(reverse=True)
#print(ls2)

#print(min(ls2))
#print(max(ls2))
#print(sum(ls2))

#ls1 = ['a','b','c','d']
#ls2 = ['e','f','g']

#ls = ls1 + ls2
#print(ls)

#ls1.append(ls2)
#print(ls1)

#ls1.extend(ls2)
#print(ls1)
#ls1.clear()
#print(ls1.index('d'))

#ls = [10,20,3.1,'upflairs pvt ltd',500, 400]

#ls[2] = 100
#print(ls)

#print(ls[3][0:7])

#ls[3] = 'flipkart pvt ltd'
#print(ls)

# tuple #  (unchangeble)

#tpl = (25,30,'harsh',True,25.2)
#print(tpl)
#print(type(tpl))

# set #

#st = {1,2,5,4,9,7,5,8,0}

#print(st)
#print(type(st))

#st.add(10)
#print(st)

#st.remove(0)       # present in set
#print(st)

#st.discard(40)     # don't care present in array or not
#print(st)

#st1 = {2,7,9,5,0,8}
#st2 = {2,6,89,65,45}

#st1.update(st2)    # st1 + st2
#print(st1)

#print(st1.intersection(st2))


# dictionary #
# pairs = (key:value)

#marks = {'mohit':56,'bittu':78,'harsh':65,'aditya':87}
#print(marks)
#print(type(marks))