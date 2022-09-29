from indexer import *
from search_func import *
from testlogin import *

alpha_value = 0.005 #0.005
raw_query = input("masukkan query : ")
alpha_value = 0.005 #0.005
result_vsm = runn(raw_query)
result_pi = runn2(raw_query)



print('result vsm: ',result_vsm)
print('result pi : ',result_pi)


result_namevsm = []
result_bobotvsm = []

for i in result_vsm:
    result_namevsm.append(i[0])
    result_bobotvsm.append(i[1])

print(result_namevsm)
print(result_bobotvsm)

print(len(result_namevsm))
print(len(result_pi))


result_irisanname = []
result_irisanindeks = []

for i in range(len(result_namevsm)):
    for j in range(len(result_pi)):
        if result_namevsm[i] == result_pi[j]:
            result_irisanname.append([result_namevsm[i], result_bobotvsm[i]])
            if len(result_irisanname) == 10:
                break

print(result_irisanname)
