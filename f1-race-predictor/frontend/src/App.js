// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
// Import your existing components
import HomePage from './HomePage'; // Adjust the import path if needed
import AnotherPage from './AnotherPage'; // Adjust the import path if needed
// Import the new F1Data component
import F1Data from './F1Data';

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
