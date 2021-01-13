import React from "react"

function ToDoItem(props){ //we add the param props so we can use the props we created in App.js in the function below
    console.log(props)
    return(
       <div className = "todo-item">
            <p>{props.itemName}<span><input type ="checkbox" /></span></p>
       </div>
       //using props.itemName we can use the prop data placeed in itemName from App.js or where ever it is located
    )
}

export default ToDoItem