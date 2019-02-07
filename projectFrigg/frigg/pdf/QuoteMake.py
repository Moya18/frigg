# -*- coding: cp1252 -*-

import os
#from latex import build_pdf
#import latex

def Config():
    Out=r"\UseRawInputEncoding" + "\n"
    Out+=r"\documentclass[11pt]{report}" + "\n"
    Out+=r"\usepackage[T1]{fontenc}" + "\n"
    Out+=r"\usepackage{uarial}" + "\n"
    Out+=r"\renewcommand{\familydefault}{\sfdefault}" + "\n"
    Out+=r"\usepackage{blindtext}" + "\n"
    Out+=r"\def \tab {\hspace*{2ex}}" + "\n"
    Out+=r"\usepackage{array}" + "\n"
    Out+=r"\usepackage{hyperref}" + "\n"
    Out+=r"\usepackage[margin=0.5in]{geometry}" + "\n"    
    Out+=r"\usepackage{graphicx}" + "\n"
    Out+=r"\begin{document}" + "\n"
    
    return Out

def Heading(Quote_Number,Day,Month,Year,Deadline,Name,Company,Email,RFC,Address,Tel):
    Out=r"\begin{tabular}{ >{\arraybackslash}m{8cm}  >{\arraybackslash}m{3.5cm} >{\arraybackslash}m{7cm} }" + "\n"
    Out+=r"\includegraphics[width=20em]{inmats.jpg} &&\textbf{Clave de Cotizaci\'on} " + str(Quote_Number) +r" \\" + "\n"
    Out+=r"\end{tabular}" + "\n"
    Out+=r"\hrule" + "\n"
    Out+=r"\noindent" + "\n"
    Out+=r"\begin{center}" + "\n"
    Out+=r"\begin{tabular}{ >{\arraybackslash}m{12.5cm}  >{\arraybackslash}m{1cm} >{\centering\arraybackslash}m{1cm} |>{\centering\arraybackslash}m{1cm} |>{\centering\arraybackslash}m{1cm} >{\centering\arraybackslash}m{1cm} }" + "\n" 
    Out+=r"inMateriis S.A de C.V &\\" + "\n"
    Out+=r"Jos\'e Guadalupe Montenegro 2312&&D\'ia&Mes&A\~no\\" + "\n"
    Out+=r"Americana C.P. 44160 &\textbf{Fecha}&"+ str(Day) +r"&"+ str(Month) +r"&"+ str(Year) +r"\\" + "\n"
    Out+=r"Guadalajara, Jalisco, M\'exico &\\" + "\n"
    Out+=r"R.F.C. INM130913762 &\\" + "\n"
    Out+=r"\end{tabular}" + "\n"
    Out+=r"\end{center}" + "\n"
    Out+=r"\begin{center}" + "\n"
    Out+=r"\begin{tabular}{ >{\arraybackslash}m{5.5cm}  >{\arraybackslash}m{5cm}  >{\arraybackslash}m{7cm} }" + "\n" 
    Out+=r"\textbf{Recoger en} & \textbf{Tiempo de entrega} & \textbf{Cliente} \\" + "\n" 
    Out+=r"inMateriis S.A de C.V &"+ str(Deadline) +r" d\'ias h\'abiles& "+ str(Name) +r"\\" + "\n"
    Out+=r"Lerdo de Tejada No. 2334& & "+ str(Company) +r"\\" + "\n" 
    Out+=r"Lafayette C.P. 44150 &\textbf{Condiciones de pago}  &"+ str(Email) +r"    \\" + "\n" 
    Out+=r"Guadalajara, Jalisco, M\'exico &100\% contra entrega &"+ str(RFC) +r"  \\" + "\n" 
    Out+=r"Tel: (33) 18126679& & "+ str(Address) +r"  \\" + "\n" 
    Out+=r"& & "+ str(Tel) +r" \\" + "\n" 
    Out+=r"\end{tabular}" + "\n"
    Out+=r"\end{center}" + "\n"


    return Out

def Table(Prints,IVA):
    Out=r"\begin{center}" + "\n"
    Out+=r"\begin{tabular}{| >{\centering\arraybackslash}m{10cm} | >{\centering\arraybackslash}m{3cm} | >{\centering\arraybackslash}m{2cm} |  >{\centering\arraybackslash}m{2cm}|}" + "\n"
    Out+=r"\hline" + "\n"
    Out+=r"\textbf{Descripci\'on} & \textbf{Costo Unitario} & \textbf{Cantidad} & \textbf{Subtotal} \\" + "\n"
    Out+=r"\hline" + "\n"
    Out+=r"& & & \\" + "\n"
    #For each Setting
    Total=0
    for Setting in range (len(Prints)):        
        Out+=r"\item[$\bullet$] Impresi\'on "+str(Prints[Setting][0])+r" Resoluci\'on "+str(Prints[Setting][1])+r"mm "+str(Prints[Setting][2])+r" & & &\\" + "\n"
        for Item in range (len(Prints[Setting][3])):
            Total+=Prints[Setting][3][Item][1]*Prints[Setting][3][Item][2]
            Out+=r"\item[$\circ$] "+str(Prints[Setting][3][Item][0])+r" &\$"+str(Prints[Setting][3][Item][1])+r" &"+str(Prints[Setting][3][Item][2])+r" &\$"+str(Prints[Setting][3][Item][1]*Prints[Setting][3][Item][2])+r"\\" + "\n" 
        Out+=r"& & & \\" + "\n" 

    Out+=r"& & & \\" + "\n" 
    Out+=r"& & &\$"+str(Total)+r" \\ " + "\n"
    Out+=r"\hline" + "\n"
    Out+=r"\end{tabular}" + "\n"
    Out+=r"\end{center} " + "\n"
    Out+=r"\begin{center}" + "\n"

    Out+=r"\begin{tabular}{ >{\centering\arraybackslash}m{10cm}  >{\centering\arraybackslash}m{3cm}  >{\arraybackslash}m{2cm}   >{\arraybackslash}m{2cm}}" + "\n" 
    Out+=r"& &  \textbf{Subtotal:} &\$"+str(Total)+r" \\" + "\n" 
    Out+=r"& &  \textbf{IVA:} &\$"+str(Total*IVA)+r"\\" + "\n" 
    Out+=r"& &  \textbf{Total:} &\$"+str(Total+Total*IVA)+r"\\" + "\n" 
    Out+=r"\end{tabular}" + "\n" 
    Out+=r"\end{center}" + "\n" 
    
    return Out

def Footer():
    Out=r"\mbox{}"+"\n"
    Out+=r"\vfill"+"\n"
    Out+=r"\scriptsize{"+"\n"
    Out+=r"\textbf{Pol\'iticas de Venta:} \\"+"\n"
    Out+=r"- Esta cotizaci\'on s\'olo es v\'alida por 30 d\'ias naturales.\\"+"\n"
    Out+=r"- Los horarios de entrega y recepc\'i\'on de pedidos son de lunes a viernes de 10 a.m. a 8 p.m. \\"+"\n"
    Out+=r"- Las urgencias se cobran con un 30\% adicional y se entregan lo antes posible (el tiempo de entrega se determina a disponibildad de las impresoras). \\"+"\n"
    Out+=r"- La fecha de entega se determina despu\'es de que el cliente notifica por correo electr\'onico que aprueba la cotizaci\'on y en caso de que se requiera anticipo. La fecha se determina al momento de recibir el anticipo o comprobante de transferencia del anticipo. \\"+"\n"
    Out+=r"\begin{center}"+"\n"
    Out+=r"inMateriis S.A. de C.V - Jos\'e Guadalupe Montenegro 2312 - Guadalajara, Jalisco - M\'exico \\"+"\n"
    Out+=r"http://www.inmateriis.com - info@inmateriis.com - Tel. 18126679"+"\n"
    Out+=r"\end{center}"+"\n"
    Out+=r"}"+"\n"
    Out+=r"\end{document}"+"\n"

    return Out

def run(quote_id, date, company, material, layers, infill, supports, speed, print_time, weight, number_copies, date_due):
    #Quote_Number="00000001"
    Quote_Number = quote_id
    # Day="31"
    # Month="01"
    # Year="19"
    Day = str(date).split('-')[2]
    Month = str(date).split('-')[1]
    Year = str(date).split('-')[0]
    Name="Bob Smith"
    # Company="Smith Inc"
    Company = company
    Email="B.Smith@SInc.com"
    RFC="ROSX989232"
    Address="The House, TownsVile, Mexico"
    Tel="3311110102"
    Deadline="14"

    Prints=[["Peek","0.1","Default",[["Cage",200,2],["Skull Plate",2500,1]]],[material,"0.05","Blue",[["Handle",50,10]]]]

    OutFile=Config()
    OutFile+=Heading(Quote_Number,Day,Month,Year,Deadline,Name,Company,Email,RFC,Address,Tel)
    OutFile+=Table(Prints,0.16)
    OutFile+=Footer()


    with open("Quote.tex", "w") as text_file:
        
        text_file.write(OutFile)
    os.system("pdflatex Quote.tex")
    #print latex.is_available()
