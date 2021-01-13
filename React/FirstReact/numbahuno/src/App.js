import React from "react"
import Joke from "./components/Joke"



function App() {

  return (
    <div className="jokeHolder">
      <Joke
        question="What is suckus?"
        punchLine="Suckus deez nuts" />

      <Joke
        question="Something came in the mail today?"
        punchLine="Deez Nutz" />

      <Joke
        question="What school yall go to?"
        punchLine="ion know its only my 3rd day out here..." />

      <Joke
        question="Whats Ligma?"
        punchLine="Ligma nuts" />

      <Joke
        question="Whats Up Dog??"
        punchLine="Nothing Much" />

    </div>
  )
}


export default App  