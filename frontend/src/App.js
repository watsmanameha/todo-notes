import React from "react";
import './App.css';
import UserList from "./components/User.js";
import axios from "axios";
import Footer from "./components/Footer.js";
import ProjectList from "./components/Project.js"
import TodoList from "./components/Todo.js"


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users' : [],
      'projects' : [],
      'todos': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users/',
    'http://127.0.0.1:8000/api/projects/',
    'http://127.0.0.1:8000/api/todos/')
        .then(response => {
          const users = response.data
            this.setState(
                {
                  'users': users
                }
            )
          const projects = response.data
            this.setState(
                {
                    'projects' : projects
                })
          const todos = response.data
            this.setState(
                {
                    'todos' : todos
                })
        }).catch(error => console.log(error))
  }

  render() {
    return (
        <div>
            <UserList users={this.state.users}/>
            <ProjectList projects={this.state.projects}/>
            <TodoList todos={this.state.todos}/>
            <Footer/>
        </div>
    )
  }
}

export default App;