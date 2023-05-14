from flask import Flask, request, render_template,url_for,flash,redirect,session
from image_recomend import Images

# Recomendation
import re

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('indexpage.html')
    
    
@app.route('/index')
def index():
    return render_template('indexpage.html')



@app.route('/search',methods=['POST','GET'])
def search():
    try:
      if request.method == 'POST':
          inputs = request.form['data']
          print(inputs)

          return render_template('search.html')
    except:
        return render_template('apology.html')
                

    
    
@app.route('/agra')
def agra():
    return render_template('tajmahal.html')
    
    
    
@app.route('/goa')
def goa():
    return render_template('goa.html')
    
    

@app.route('/mumbai')
def mumbai():
    return render_template('mumbai.html')
    
    
    
@app.route('/manali')
def manali():
    return render_template('manali.html')
    
    
    
@app.route('/delhi')
def delhi():
    return render_template('delhi.html')
    
    
    
@app.route('/jaipur')
def jaipur():
    return render_template('jaipur.html')



@app.route('/index_msg')
def index_msg():
    return render_template('index.html')
    
    
    
@app.route('/image')
def image():
    return render_template('imagesearch.html')
    
    

@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        recomend = Images()
        data = recomend.Upload()
        
        location = data
        location  = re.findall('([^\/]+$)',location)
        new_loc  = "queries/"+location[0]
        print(new_loc)
        print("Working")

        res_loc = recomend.predict(new_loc)

        print(res_loc)
        res_name = res_loc[:-7]
        if res_name == 'Taj_Mahal':
            return 	render_template('taj_mahal.html')
        elif res_name == 'qutub_minar':
            return 	render_template('qutub_minar.html')
        elif res_name == 'Mysore_Palace':
            return 	render_template('mysore.html')
       
        elif res_name == 'Jantar_mantar':
            return 	render_template('jantar mantar.html') 
        elif res_name == 'hawa_mahal':
            return 	render_template('hawa mahal.html') 
            
        elif res_name == 'red_fort':
            return 	render_template('red fort.html') 
            
        elif res_name == 'gateway':
            return 	render_template('gateway of india.html')
            
        elif res_name == 'lotus_temple':
            return 	render_template('lotus temple.html')  
            
        elif res_name == 'Virupaksha':
            return 	render_template('virupaksha temple.html')         
        elif res_name == 'gol_gumbaz':
            return 	render_template('gol gumbaz.html')  
        elif res_name == 'golden_temple':
            return 	render_template('golden temple.html') 
        
        elif res_name == 'Jama_Masjid':
            return 	render_template('jama masjid.html') 
        else:
   	        return 	render_template('apology.html')
    return render_template('indexpage.html')
    
    
    
@app.route('/about')
def about():
	return render_template('about.html')
	
	
if __name__ == "__main__":
    app.run(debug=True)
