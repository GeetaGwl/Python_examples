d={1:"aaa",2:"bbb",3:"ccc"}
print(d[1])
d[4]="ddd"
print(d)

d2={"first":1000,"sec":2000,"thrd":3000}
print(d2["first"])
d3={"names":["ajay","suhani","prachi"],
    "city":["Gwalior","Mumbai","delhi"]
    }

d2.clear()
print(d2)
x=[1,2,3,4]
y={"a":"xyz","b":"abc"}
d4=dict.fromkeys(x,y)
print(d4)

d5={
    1:{"name":"xyz"},
    2:{"age":27},
    3:{"city","Delhi"}
}
print(d5)
d.popitem()
print(d)




