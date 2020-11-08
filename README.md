## 线装书页码编排

线装书的页码编排和胶装书有很大的区别，处理页面顺序是个问题。下面的方法是通过 Python 实现线装书页码一键编排（只针对 PDF 文件，Word 可以直接用“书籍折页”打印）。

### 提示：

***保险起见，在文件生成后最好检查下第一册和最后一册的页码顺序是否正确。***

### 准备：

1. Python
2. 已经排版好的 PDF 文件。***请注意：页数必须是 4 的倍数！***

### 步骤：

#### 1. 安装 PyPDF2

```bash
pip install PyPDF2
```

#### 2. 执行以下代码

```pyth
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
            
            for w in range(0,pl):        
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
```

完成！执行完毕后您会看到一个新的 PDF 文件。打印时只需要选择“一张多页”+“双面打印”+“短边翻转”（默认长边，需要修改）就能打印出线装书了！
