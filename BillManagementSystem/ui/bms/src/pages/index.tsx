import React, { useState } from 'react';
import { useSession } from 'next-auth/react';

function Home() {
    const { data: session, status } = useSession();

    let result: string;
    if (status == 'authenticated') {
        result = 'Login d';
    } else {
        result = 'Not Yet Login';
    }
    return (
        <div>
            <h1>{result}</h1>
        </div>
    );
}

export default Home;