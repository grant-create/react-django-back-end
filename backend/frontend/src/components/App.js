import React, { Component } from 'react'
import ReactDOM from 'react-dom'


import Header from './layout/Header'

export class App extends Component {
    render() {
        return (

            
            <div>
                <h1>React app from App.js</h1>
                {/* <Header/> */}
            </div>
        )
    }
}




ReactDOM.render(<App />, document.getElementById('app'))