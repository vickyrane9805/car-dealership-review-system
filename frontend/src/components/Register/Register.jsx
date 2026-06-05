import React from "react";

function Register() {

  return (
    <div>
      <h1>Register</h1>

      <input placeholder="Username" />
      <br />

      <input placeholder="First Name" />
      <br />

      <input placeholder="Last Name" />
      <br />

      <input placeholder="Email" />
      <br />

      <input
        type="password"
        placeholder="Password"
      />
      <br />

      <button>
        Register
      </button>
    </div>
  );
}

export default Register;