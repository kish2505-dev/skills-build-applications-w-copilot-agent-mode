import React, { useEffect, useState } from 'react';


function Users() {
  const [users, setUsers] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const items = data.results ? data.results : data;
        setUsers(items);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, [endpoint]);

  return (
    <div className="card shadow mb-4">
      <div className="card-header bg-secondary text-white">
        <h2 className="card-title mb-0">Users</h2>
      </div>
      <div className="card-body">
        {users.length === 0 ? (
          <div className="text-center">No users found.</div>
        ) : (
          <div className="table-responsive">
            <table className="table table-striped table-bordered align-middle">
              <thead className="table-light">
                <tr>
                  {Object.keys(users[0]).map((key) => (
                    <th key={key}>{key.charAt(0).toUpperCase() + key.slice(1)}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {users.map((user, idx) => (
                  <tr key={user.id || idx}>
                    {Object.values(user).map((val, i) => (
                      <td key={i}>{typeof val === 'object' ? JSON.stringify(val) : val}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export default Users;
