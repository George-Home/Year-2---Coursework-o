def m_Poly():


    degree = 2 + 3      #degree 1 , degree two 
    P1 = [3,1,9]
    P2 = [2,1,2,1]
    res = [0]*(degree+1)    #both degrees added then add one for size of result list
                            #is also initialised as all zeros
    for i in range(0,2 + 1):                #performs multiplication of polynomials
        for j in range(0,3 + 1):
            res[i+j] += P1[i] * P2[j]

    print(res)

m_Poly()
