from PyPDF2 import PdfFileReader, PdfFileWriter

def xianzhuang_pdf(origin_file,new_file):
    
    pread = PdfFileReader(origin_file)            
    pwrite = PdfFileWriter()                     
    numpages = pread.getNumPages()     
    
    if numpages%4 == 0:
        sp = int(input('请输入每一小册的页数（需是4的倍数）：'))
        cp = numpages/sp
        cs = int(cp)
        pl = int(sp/4)
        k = 0
        
        for i in range(0,cs):      
            z = 1
            y = 0
            
            for w in range(0,pl):  # 每一册里执行次          
                pageObj1 = pread.getPage(sp*k+sp-z) 
                pwrite.addPage(pageObj1)
                
                pageObj2 = pread.getPage(sp*k+y) 
                pwrite.addPage(pageObj2)
                
                pageObj3 = pread.getPage(sp*k+z) 
                pwrite.addPage(pageObj3)
                
                pageObj4 = pread.getPage(sp*k+sp-y-2) 
                pwrite.addPage(pageObj4)
                               
                if w == pl:
                    z = 1
                    y = 0
                else:
                    z = z+2
                    y = y+2
            k = k+1        
             
        pwrite.write(open(new_file, 'wb'))
        

if __name__ == '__main__':
    origin_file = '请在这里输入您要处理的PDF文件路径'
    new_file = '请在这里输入您生成的PDF的文件存储路径' 
    xianzhuang_pdf(origin_file,new_file)
