#only need to run this to run the site!
from website import create_app #this is possible because the file in website is initialised as __init__, website becomes a package

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #automatically reruns the website
