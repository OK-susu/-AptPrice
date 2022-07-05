def StrGrab(aStr, prefix, surfix, aIndex):
    if aStr == "": return ""
    
    count = aIndex
    
    start = 0
    end = 0
    i = 0    
    while i < count: 
        if prefix == "": 
            start=0
        else :
            start = aStr.find(prefix)
            if start >= 0:
                start += len(prefix)
            else:
                return ""
        
        aStr = aStr[start:]
        if start == 0: break
        i+= 1
        
    if surfix == "":
        return aStr
    else:
        end = aStr.find(surfix)
        if end >= 0:
            return aStr[0:end]
        else:
            return ""