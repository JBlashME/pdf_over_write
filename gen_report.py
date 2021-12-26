# %% 
from fpdf import FPDF

# %%
# x = 216 
# y = 279.5
class PDF(FPDF):
    black = [65, 65, 65]
    dark_blue = [47,66, 107]
    blue = [65, 95, 155]
    light_blue = [157,178, 220]
    
    def set_info(self,image_path):
        self.add_font("Ubuntu-B", "", "resources/fonts/Ubuntu-B.ttf", uni=True)  
        self.add_page()
        self.image(image_path,0, 0, 216, 279.5)
        
    def build_first_page(self):
        self.set_info('resources/pages/first_page.png')
        x_margin = 25
        blue = [65, 95, 155]
        black = [65, 65, 65]
        self.set_text_color(blue[0],blue[1],blue[2])
        self.set_font("Ubuntu-B",'', 36)
        self.set_xy(x_margin,180)
        h = 15
        self.cell(70,h,'Informe técnico',0,2,'L')
        self.cell(70,h,'Ide localización',0,2,'L')
        self.set_text_color(black[0],black[1],black[2])
        h = 6
        self.set_font("Ubuntu-B",'', 13)
        self.set_xy(x_margin,215)
        self.cell(70,h,'Calle Mayor 25, 28001 Madrid.',0,2,'L')
        self.cell(70,h,'Área de influencia a 10 minutos a pie.',0,2,'L')
        self.cell(70,24,'',0,2,'L')
        h = 8
        self.set_font("Ubuntu-B",'', 18)
        self.cell(70,h,'McDonalds',0,2,'L')
        self.cell(70,h,'25/11/2021',0,2,'L')
        self.image("resources/links/globe.png",52, 240, 50, 0)
    
    def build_second_page(self, content):
        x_margin = 65
        black = [65, 65, 65]
        blue = [65, 95, 155]
        light_blue = [157,178, 220]
        self.set_draw_color(light_blue[0],light_blue[1],light_blue[2])
        self.set_info('resources/pages/second_page.png')
        self.set_xy(x_margin, 80)
        self.set_text_color(blue[0],blue[1],blue[2])
        h = 12
        c1 = 10
        c2 = 70
        self.set_font_size(26)
        font1 = 22
        font2 = 16
        self.cell(70,h*2.5,'Content',0,2,'L')
        for ii in range(0,len(content)):
            self.set_x(x_margin)
            self.set_text_color(light_blue[0],light_blue[1],light_blue[2])
            self.set_font_size(font1)
            self.cell(c1,h,str(ii),'B',0,'L')
            self.set_text_color(black[0],black[1],black[2])
            self.set_font_size(font2)
            self.cell(c2,h,str(content[ii]),'B',2,'L')
            
            
    
# %%
pdf = PDF('P','mm','A4')
# Create teh page
# path = 'resources/pages/first_page.png'
# pdf.set_info('resources/pages/first_page.png')
pdf.build_first_page()
pdf.build_second_page(['test1', 'test2','test3','test4','test5'])
output_path = 'test'
pdf.output(output_path+'.pdf') 
# %%


# what size page do you use? 
# what text will need to be changed?