from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def helloworld():
    return render_template("index.html")


# @app.route("/upload", methods=["POST"])
# def upload():
#     # Check if the request contains a file
#     if "file" in request.files:
#         # Get the file from the request
#         file = request.files["file"]
#         # Read the file as a pandas dataframe
#         df = pd.read_excel(file)
#         # Convert the dataframe to a list of lists
#         data = df.values.tolist()
#         # Render the HTML template for displaying the data
#         return render_template("data_view.html", data=data)
#     else:
#         # Return an error message if no file was uploaded
#         return "No file was uploaded."


app.run(debug=True)