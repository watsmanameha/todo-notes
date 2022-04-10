import React from "react";
import './App.css';
import UserList from "./components/User.js";
import axios from "axios";
import Footer from "./components/Footer.js";
import ProjectList from "./components/Project.js"
import TodoList from "./components/Todo.js"
import {HashRouter, Link, Route} from "react-router-dom"


const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
        users: [],
        projects: [],
        todos: []
    }
  }

  componentDidMount() {
    axios.get(get_url('users/'))
        .then(response => {
            this.setState(
                {
                  users: response.data
                }
            )
        }).catch(error => console.log(error))

        axios.get(get_url('projects/'))
        .then(response => {
            this.setState(
                {
                  projects: response.data
                }
            )
        }).catch(error => console.log(error))

        axios.get(get_url('todos/'))
        .then(response => {
            this.setState(
                {
                  todos: response.data
                }
            )
        }).catch(error => console.log(error))
  }

 render() {
    return (
        <div className="App">
            <HashRouter>
            <nav>
                <ul>
                    <li><Link to='/users'>Users</Link></li>
                    <li><Link to='/projects'>Users</Link></li>
                    <li><Link to='/todos'>Users</Link></li>
                </ul>
            </nav>
                <Route exact path='/users' component={() => <UserList users={this.state.users}/>} />
                <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>} />
                <Route exact path='/todos' component={() => <TodoList todos={this.state.todos}/>} />
            </HashRouter>
            <Footer/>
        </div>
    )
  }
}

export default App;