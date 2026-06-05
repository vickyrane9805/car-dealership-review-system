import React, { useState } from "react";

function AddReview() {

  const [review, setReview] = useState("");

  return (

    <div style={{padding:"20px"}}>

      <h1>Post Review</h1>

      <input
        placeholder="Reviewer Name"
        defaultValue="Vivek"
      />

      <br /><br />

      <input
        placeholder="Purchase Date"
        defaultValue="2026-06-05"
      />

      <br /><br />

      <input
        placeholder="Car Make"
        defaultValue="Toyota"
      />

      <br /><br />

      <input
        placeholder="Car Model"
        defaultValue="Corolla"
      />

      <br /><br />

      <textarea
        rows="5"
        cols="40"
        placeholder="Write Review"
        value={review}
        onChange={(e)=>setReview(e.target.value)}
      />

      <br /><br />

      <button>
        Submit Review
      </button>

    </div>

  );
}

export default AddReview;