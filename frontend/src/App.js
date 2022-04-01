import React from "react";
import './App.css';
import UserList from "./components/User.js";
import axios from "axios";
import Footer from "./components/Footer.js";
import ProjectList from "./components/Project.js"
import TodoList from "./components/Todo.js"
import {HashRouter, Route, Link} from 'react-router-dom'


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
                    'projects': projects
                })
          const todos = response.data
            this.setState(
                {
                    'todos': todos
                })
        }).catch(error => console.log(error))
  }

  render() {
    return (
        <div className="App">
            <HashRouter basename='/'>
            <nav>
                <ul>
                    <li><Link to='/'>Users</Link></li>
                    <li><Link to='/projects'>Users</Link></li>
                    <li><Link to='/todos'>Users</Link></li>
                </ul>
            </nav>
                <Route exact path='/' component={() => <UserList users={this.state.users}/>} />
                <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>} />
                <Route exact path='/todos' component={() => <TodoList todos={this.state.todos}/>} />
            </HashRouter>
            <Footer/>
        </div>
    )
  }
}

export default App;