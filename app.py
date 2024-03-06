from doctest import debug
from website import create_app

# Main Driver Function 

if __name__ == ("__main__"):
    app = create_app()
    app.run(debug=True)

    