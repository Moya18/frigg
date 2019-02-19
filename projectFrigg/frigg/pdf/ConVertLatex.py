def LatStr(In):
    Out=r""
    for l in In:
        if l=="á":
            Out+=r"\'a"
        elif l=="é":
            Out+=r"\'e"        
        elif l=="í":
            Out+=r"\'i"
        elif l=="ó":
            Out+=r"\'o"
        elif l=="ú":
            Out+=r"\'u"
        elif l=="ñ":
            Out+=r"\~n"
        elif l=="_":
            Out+=r"\_"
        elif l=="%":
            Out+=r"\%"
        elif l=="Á":
            Out+=r"\'A"
        elif l=="É":
            Out+=r"\'E"        
        elif l=="í":
            Out+=r"\'i"
        elif l=="ó":
            Out+=r"\'o"
        elif l=="ú":
            Out+=r"\'u"
        elif l=="ñ":
            Out+=r"\~n"
        else:
          Out+=l
    return Out

print (LatStr("ñáéíóú_naeiou"))
