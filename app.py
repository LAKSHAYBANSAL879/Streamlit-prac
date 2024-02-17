import streamlit as sc
sc.title("this is title")
sc.header("header tag")
sc.subheader("this is subheader")
sc.text("this is text")
sc.markdown('# Hi')
sc.markdown('## Hi')
sc.success('data is submitted')
sc.info('information!')
sc.warning("warning")
sc.error('404 errr')
sc.exception(ZeroDivisionError('Div not possible'))
sc.help(ZeroDivisionError)
sc.write("range(1,10)")
sc.write(range(1,10))
sc.subheader('Code')
sc.code('x = 10\n'                                      # Code
        'for i in range(x):\n'
        '\tprint(i)')

sc.color_picker('code')
sc.checkbox('male')
sc.checkbox('female')
if(sc.checkbox('adult')):
    sc.write("you are adult")
sc.subheader('Radio Button')                            # Radio Button
radioButton = sc.radio('Select : ', ('Male','Female','Other'))
if(radioButton == 'Male'):
    sc.write("You're a Male")
elif(radioButton == 'Female'):
    sc.write("You're a Female")
elif(radioButton == 'Other'):
    sc.write("You're an Other Gender")

sc.subheader('Select Box')                              # SelectBox
selectBox =  sc.selectbox("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])
sc.write("You've selected : ", selectBox )   
sc.subheader('MultiSelect Box')                         # MultiSelectBox
multiSelBox = sc.multiselect("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                    'Deep Learning','Natural Language Processing',
                                                    'Computer Vision','Image Processing'])
sc.write("You've selected : ", len(multiSelBox) , 'courses','Selected courses are',multiSelBox)

if(sc.button('i am button')):
    sc.write('you have clicked button')
    
sc.slider("select value",1,100,step=1 )

sc.subheader("Text Input")                              # Text-Input
username = sc.text_input('Username : ')
password = sc.text_input('Password : ', type = 'password')

sc.subheader("Text Area")                              # Text-Area
sc.text_area('Write something interesting about yourself')

sc.subheader("Input Number")                           # Input-Number
sc.number_input('Select your age',18,110)

sc.subheader("Input Date")                              # Input-Date
sc.date_input('Date')

sc.subheader("Input Time")                              # Input-Time
sc.time_input('Time')    