// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import F1Data from './F1Data';
// Import other components if any

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route exact path="/" component={HomePage} />
                    <Route path="/another" component={AnotherPage} />
                    <Route path="/f1data" component={F1Data} /> {/* New route for F1 data */}
                </Switch>
            </div>
        </Router>
    );
}

export default App;
