import React, { useEffect, useState } from "react";
import axios from "axios";

function Home() {
  
  const [state, setState] = useState("");
  const [dealers, setDealers] = useState([]);

 useEffect(() => {

  let url = "http://127.0.0.1:8000/dealers";

  if (state) {

    url =
      `http://127.0.0.1:8000/dealersByState?state=${state}`;

  }

  axios
    .get(url)
    .then((response) => {

      setDealers(response.data);

    });

}, [state]);

 return (

  <div style={{padding:"20px"}}>

    <h1>Car Dealership Review System</h1>

    <h3>
      Welcome {
        localStorage.getItem("username")
          || "Guest"
      }
    </h3>
    <select
  value={state}
  onChange={(e) =>
    setState(e.target.value)
  }
>

  <option value="">
    All States
  </option>

  <option value="Kansas">
    Kansas
  </option>

  <option value="Texas">
    Texas
  </option>

</select>

    <h2>Dealers</h2>

    {
      dealers.map((dealer) => (

        <div
          key={dealer.id}
          style={{
            border:"1px solid black",
            padding:"10px",
            margin:"10px"
          }}
        >

          <h3>{dealer.name}</h3>

          <p>City: {dealer.city}</p>

          <p>State: {dealer.state}</p>

          <p>Address: {dealer.address}</p>

          <button>
            Review Dealer
          </button>

        </div>

      ))
    }

  </div>

);

}

export default Home;