import React from "react";


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.project_name}
            </td>
            <td>
                {project.repo_url}
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )
}


const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                Project Name
            </th>
            <th>
                Repository
            </th>
            <th>
                Users
            </th>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}


export default ProjectList;