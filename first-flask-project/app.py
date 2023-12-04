from flask import Flask, render_template, jsonify
import pandas as pd


app = Flask(__name__)


@app.route("/")
def helloworld():
    return render_template("index.html")


@app.route("/upload", methods=["GET"])
def upload():
    try:
        file_path = 'todo_tasks_data.xlsx'
        df = pd.read_excel(file_path)
        raw_data = df.values.tolist()
    
        to_do_list = []
    

        
        for i in raw_data:
            task_split = i[0].split(", ")
    
            task_map = {
                "Task Name": task_split[0],
                "Date Created": task_split[1],
                "Date Completed": task_split[2],
                "Completion Status": task_split[3],
                "Priority": task_split[4],
                "Time to Complete": task_split[5]
            }
    
            to_do_list.append(task_map)
        

        return jsonify(to_do_list)
    
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render_template('index.html', error=error_message)
    

app.run(debug=True)