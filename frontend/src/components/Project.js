import React from 'react'
import {
  Link,
  useParams
} from "react-router-dom";


const ProjectItem = ({project}) => {
    let link_to = '/project/${item.id}'
    return (
        <tr>
            <td>{project.project_name}</td>
            <td>{project.repo_url}</td>
            <td>{project.users}</td>
            <td><Link to={link_to}>Detail</Link></td>
        </tr>
    )
}


const ProjectList = ({projects}) => {
    return (
        <table className="table">
            <tr><th>Project Name</th>
                <th>Repository</th>
                <th>Users</th>
                <th></th>
            </tr>
            {projects.map((project) => <ProjectList project={project}/>)}
        </table>
    )
}

const ProjectUserItem = ({item}) => {
    return (
        <li>
        {item.username} ({item.email})
    </li>
    )
}

const ProjectDetail = ({getProject, project}) => {
    let { id } = useParams();
    getProject(id)
    let users = project.users ? project.users : []
    console.log(id)
    return (
        <div>
            <h1>{project.name}</h1>
            Repository: <a href={project.repo_url}>{project.repo_url}</a>
            <p></p>
            Users:
            <ol>
            {users.map((user) => <ProjectUserItem item={user} />)}
            </ol>
        </div>
    )
}




export {ProjectDetail, ProjectList}