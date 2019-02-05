# -*- coding: cp1252 -*-

import os
#from latex import build_pdf
#import latex

def Config():
    Out=r"\UseRawInputEncoding" + "\n"
    Out+=r"\documentclass[12pt]{report}" + "\n"
    Out+=r"\def \tab {\hspace*{2ex}}" + "\n"
    Out+=r"\usepackage{array}" + "\n"
    #Out+=r"\usepackage{hyperref}" + "\n"
    Out+=r"\usepackage[margin=0.5in]{geometry}" + "\n"
    Out+=r"\usepackage{graphicx}" + "\n"
    Out+=r"\begin{document}" + "\n"
    
    return Out

def Heading(Order,Client,Clave,Date):
    Out=r"\includegraphics[width=20em]{inmats.jpg}" + "\n"
    Out+=r"\textbf{Orden de Productci\'{o}n} \\" + "\n"
    Out+=r"\vspace{1cm}" + "\n"
    Out+=r" " + "\n"
    Out+=r"{\noindent" + "\n"
    Out+=r"C\'{o}digo orden: " + str(Order) + r"\\"+"\n"
    Out+=r"C\'{o}digo de cliente: "+ str(Client)+r"\\" + "\n"
    Out+=r"Clave de cotizaci\'{o}n: "+ str(Clave)+ r"\\" + "\n"
    Out+=r"Fecha de entrega: "+ str(Date)+ r"\\" + "\n"

    return Out

def Table(Material,Color,Res,Vel,Infill,Soports):
    Out=r" " + "\n"
    Out=r"\begin{center}" + "\n"
    Out+=r"\begin{large}" +"\n"
    Out+=r"\begin{tabular}{| >{\centering\arraybackslash}m{2cm} | >{\centering\arraybackslash}m{2cm} | >{\centering\arraybackslash}m{2cm} |  >{\centering\arraybackslash}m{2cm} |  >{\centering\arraybackslash}m{2cm} |  >{\centering\arraybackslash}m{2cm}|} " +"\n"
    Out+=r"\hline" +"\n"
    Out+=r"Material & Color & Resoluc\'{o}n & Velocidad & Infill & Soportes \\" +"\n"        
    Out+=r"\hline" +"\n"

    #Out+=str(Material)+ r" & \$"+str(Color)+ r" &" +str(Res)+ r" &" +str(Vel)+r" &" +str(Infill)+r" &" +str(Soports)+r" &  \\"   

    Out+=r" \hline" +"\n"
    Out+=r" \end{tabular}" +"\n"
    Out+=r" \end{large}" +"\n"
    Out+=r" " + "\n"
    Out+=r" \end{center}" +"\n"
    
    return Out

def Footer():
    Out=r"\end{document}" + "\n"

    return Out
    
import datetime
now = datetime.datetime.now()

def run(job_id, date):
    OutFile=Config()
    # OutFile+=Heading("00000000","00000000","00000000",now.strftime("%d/%m/%Y"))
    OutFile+=Heading(job_id,"00000000","00000000", date)
    OutFile+=Table("ABS","Blanco","0.01 mm","Turbo","20","30")
    OutFile+=Footer()


    with open("Job.tex", "w") as text_file:
        
        text_file.write(OutFile)
    os.system("pdflatex job.tex")
    #print latex.is_available()

