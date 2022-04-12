import React from "react";


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.created_at}</td>
            <td>{todo.updated_at}</td>
            <td>{todo.user}</td>
            <td>{todo.is_active}</td>
        </tr>
    )
}


const TodoList = ({todos}) => {
    return (
        <table className="table">
            <tr>
                <th>Project</th>
                <th>Text</th>
                <th>Created At</th>
                <th>Last Update</th>
                <th>User</th>
                <th>Activity</th>
            </tr>
            {todos.map((todo) => <TodoItem todo={todo}/>)}
        </table>
    )
}


export default TodoList;