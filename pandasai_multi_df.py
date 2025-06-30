import pandasai as pai
from pandasai_docker import DockerSandbox
from pandasai_openai.openai import OpenAI

# Initialize the sandbox
sandbox = DockerSandbox()
sandbox.start()

employees_data = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Name": ["John", "Emma", "Liam", "Olivia", "William"],
    "Department": ["HR", "Sales", "IT", "Marketing", "Finance"],
}

salaries_data = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Salary": [5000, 6000, 4500, 7000, 5500],
}

llm = OpenAI("OPEN_AI_API_KEY")

pai.config.set({"llm": llm})

employees_df = pai.DataFrame(employees_data)
salaries_df = pai.DataFrame(salaries_data)

pai.chat("Who gets paid the most?", employees_df, salaries_df, sandbox=sandbox)

# Don't forget to stop the sandbox when done
sandbox.stop()
