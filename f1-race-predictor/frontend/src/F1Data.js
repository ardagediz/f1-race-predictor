// frontend/src/F1Data.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const F1Data = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('/api/f1data?driver_number=55&session_key=9159&speed=315');
                setData(response.data);
            } catch (error) {
                console.error('Error fetching data', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            <h1>F1 Data</h1>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
};

export default F1Data;
