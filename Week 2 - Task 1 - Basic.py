def m_Poly(P1,P2,Degree1,Degree2):

    try:
        degree = Degree1 + Degree2      #degree 1 , degree two 
    #P1 = [3,1,9]
    #P2 = [2,1,2,1]
        res = [0]*(degree+1)    #both degrees added then add one for size of result list
                            #is also initialised as all zeros
        for i in range(0,2 + 1):                #performs multiplication of polynomials
            for j in range(0,3 + 1):
                res[i+j] += P1[i] * P2[j]

        return list(res)

    except:
        print("please enter correct input values")      #input validation
