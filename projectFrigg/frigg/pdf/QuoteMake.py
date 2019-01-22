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

def Heading(Client_Name,Client_Email,Quote_Number,Date):
    Out=r"\begin{flushright} \textbf{Clave de Cotizacon} "+ str(Quote_Number) +r"\end{flushright}" + "\n"
    Out+=r"\includegraphics[width=20em]{inmats.jpg}" + "\n"
    Out+=r"\hrule" + "\n"
    Out+=r"\vspace{1cm}" + "\n"
    Out+=r" " + "\n"
    Out+=r"{\noindent" + "\n"
    Out+=r"inMateriis S.A de C.V \hfill \textbf{Cliente} \hspace{10em} \\" + "\n"
    Out+=r"Jos\'e Guadalupe Montenegro 2312 \hfill "+str(Client_Name)+r"\hspace{"+str(8.5)+r"em} \\" + "\n"
    Out+=r"Americana C.P 44160 \hfill "+ str(Client_Email)+ r"\hspace{"+str(8)+r"em} \\" + "\n"
    Out+=r"Guadalajara, Jalisco Mexico \\" + "\n"
    Out+=r" " + "\n"
    Out+=r"\noindent" + "\n"
    Out+=r"R.F.C. INM130913762 \hfill \textbf{Clave de Cotizaci\'on} "+ str(Quote_Number) +r" \\" + "\n"
    Out+=r"\textbf{Fecha:} " +str(Date)+ r" \\" + "\n"
    Out+=r" " + "\n"
    Out+=r"\noindent" + "\n"
    Out+=r"\textbf{Recoger en}  \hfill \textbf{Condiciones de Pago} \hspace{4em} \\" + "\n"
    Out+=r"inMateriis S.A de C.V  \hfill 100\% contra entrega \hspace{5.5em} \\" + "\n"
    Out+=r"Lerdo de Tejada No. 2334 \\" + "\n"
    Out+=r"Lafayette C.P 44150  \hfill \textbf{Entrega} \hspace{10.5em} \\" + "\n"
    Out+=r"Guadalajara, Jalisco Mexico   \hfill 5 dias h\'abiles \hspace{8.5em} \\" + "\n"
    Out+=r"Tel: (33) 18126679\\" + "\n"    
    return Out

def Table(Info1,Info2,Single,Prints,IVA,Total):
    Out=r" " + "\n"
    Out=r"\begin{center}" + "\n"
    Out+=r"\begin{large}" +"\n"
    Out+=r"\begin{tabular}{| >{\centering\arraybackslash}m{3cm} | >{\centering\arraybackslash}m{4cm} | >{\centering\arraybackslash}m{2cm} |  >{\centering\arraybackslash}m{4cm}|} " +"\n"
    Out+=r"\hline" +"\n"
    Out+=r"Descripci\'on & Costo Unitario & Cantidad & subtotal \\" +"\n"        
    Out+=r"\hline" +"\n"
    Out+=str(Info1)+r" & & &\\" +"\n"
    if (Info2!=""):
        Out+=+str(Info2)+r" & & &\\" +"\n"
    Out+=r"& & &\\ " +"\n"
    
    if (Single):
        Out+=str(Prints[0])+ r" & \$"+str(Prints[2])+ r" &" +str(Prints[1])+ r" &  \\"
    else:
        for n in range (len(Prints)):
            Out+=str(Prints[n][0])+ r" & \$"+str(Prints[n][2])+ r" &" +str(Prints[n][1])+ r" &  \\"   
    Out+=r"& & & +IVA \\ " +"\n"
    Out+=r"& & & \$" +str(IVA)+ r"\\ " +"\n"
    Out+=r"& & & Total: \\ " +"\n"
    Out+=r"& & & \$" +str(Total)+ r"\\ " +"\n"
    Out+=r" \hline" +"\n"
    Out+=r" \end{tabular}" +"\n"
    Out+=r" \end{large}" +"\n"
    Out+=r" " + "\n"
    Out+=r" \end{center}" +"\n"
    
    return Out

def Footer():
    Out=r" " + "\n"
    Out+=r"\textbf{Pol�ticas de Venta:} \\" + "\n"
    Out+=r"- Los horarios de entrega y recepc�on de pedidos son de lunes a viernes de 10 a.m. a 8 p.m. \\" + "\n"
    Out+=r"- Las urgencias se cobran con un 30\% adicional y se entregan lo antes posible (el tiempo de entrega se determina a disponibildad de las impresoras). \\" + "\n"
    Out+=r"- La fecha de entega se determina despu�s de que el cliente notifica por correo elera anticipo. La fecha se determina al momento de recibir el anticipo o comprobante de transferencia del anticipo. \\" + "\n"
    Out+=r"- Esta cotizaci�n s�lo es v�lida por 30 d�as naturales.\\" + "\n"
    Out+=r" " + "\n"
    Out+=r"\begin{center}" + "\n"
    Out+=r"inMateriis S.A. de C.V - Jos\'e Guadalupe Montenegro 2312 - Guadalajara, Jalisco - Mexico \\" + "\n"
    Out+=r"http://www.inmateriis.com - info@inmateriis.com - Tel. 18126679" + "\n"
    Out+=r"\end{center}" + "\n"
    Out+=r"\end{document}" + "\n"

    return Out
    
OutFile=Config()
OutFile+=Heading("Bob Smith","Alan@Blam.com","1231111139","03/12/2018")
OutFile+=Table("Information","",True,["Print 1","1","100.00"],"5.00","55.00")
OutFile+=Footer()
min_latex = (r"\documentclass{article}"
             r"\begin{document}"
             r"Hello, world!"
             r"\end{document}")

with open("Quote.tex", "w") as text_file:
    
    text_file.write(OutFile)
os.system("pdflatex Quote.tex")
#print latex.is_available()

