from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from dotenv import load_dotenv

load_dotenv()

db = SQLDatabase.from_uri("sqlite:////Users/samarthgowda/Desktop/Chinook.db")
llm = OpenAI(temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True
)

#agent_executor.run("Describe the playlisttrack table")
agent_executor.run("List the total sales per country. Which country's customers spent the most?")